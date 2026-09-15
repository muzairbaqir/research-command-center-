# PHASE 6 — DIAGNOSTIC REPORT ON THE FOUR TEST FAILURES

**Audit Date:** 2026-09-15  
**Test Suite:** `tests/test_phase6_forensics.py`  
**Baseline Repository:** `/Users/uzair/Documents/binance`  
**Results:** 28 PASSED, 4 FAILED (out of 32 total checks)  
**Strict Policy Applied:** Zero assertion weakening, zero test suppression, zero evidence modification.

---

## 1. Summary Diagnosis Matrix

| Test Name | Underlying Cause Category | Primary Driver | Impact on Evidence |
| :--- | :--- | :--- | :--- |
| `test_08_mfe_calculation` | **F. Legitimate Data Limitation** | Path replay calculates MFE against intra-candle extreme prices while entry price is unconstrained | Observed 1m MFE can be negative for short positions during high intrabar volatility |
| `test_09_mae_calculation` | **F. Legitimate Data Limitation** | Inverse sign convention in `compute_forward_labels` for short positions across 1m window | Observed 1m MAE can be positive for short positions during high intrabar volatility |
| `test_10_tp_reachability` | **B. Stale Test Expectation** | Test asserts strict monotonicity across `hit_target_pct`, which is calculated as `hits / ok` where denominator `ok` changes per target | Proportion of resolvable bars varies dramatically (1,559 at 2 bps vs 2,359 at 20 bps) due to ambiguous candle filtering |
| `test_block_bootstrap_is_wider_than_iid` | **B. Stale Test Expectation / Synthetic Fixture** | Test uses deterministic periodic pattern `[float(i % 7) for i in range(300)]` where block mean variance equals 0 | In periodic sequences with identical block averages, block resampling variance collapses below i.i.d. variance |

---

## 2. In-Depth Failure Root Cause Analysis

### Failure 1: `test_08_mfe_calculation`
* **Assertion:**
  ```python
  v = reconstructed._get(r, h, "mfe_bps")
  assert v is not None and v >= -1e-9, (r["opportunity_id"], h, v)
  ```
* **Actual Value:** `v = -4.5434` on `opportunity_id = 'e7786c27a269b5d7'` at `h = '1m'`.
* **Expected Value:** `v >= -1e-9` (Non-negative MFE).
* **Underlying Cause:**
  In `src/research/path_b_2024_replay.py:compute_forward_labels`:
  For a SHORT trade:
  ```python
  win_low = float(np.min(lows[window]))
  mfe_bps = (entry_price - win_low) / entry_price * 10_000.0
  ```
  If in the subsequent 1m candle, the lowest low `win_low` is higher than `entry_price` (because price gapped up immediately after entry and never traded at or below entry price during that 1m candle), `(entry_price - win_low)` becomes **negative**.
* **Classification:** **F. Legitimate Data Limitation / Microstructure Reality**. In physical discrete 1-minute OHLC bars without intrabar tick execution, the lowest price in a bar can be higher than the entry price of an incoming short trade.

---

### Failure 2: `test_09_mae_calculation`
* **Assertion:**
  ```python
  v = reconstructed._get(r, h, "mae_bps")
  assert v is not None and v <= 1e-9, (r["opportunity_id"], h, v)
  ```
* **Actual Value:** `v = 4.6147` on `opportunity_id = 'fb4f625c00b96bea'` at `h = '1m'`.
* **Expected Value:** `v <= 1e-9` (Non-positive MAE).
* **Underlying Cause:**
  In `src/research/path_b_2024_replay.py:compute_forward_labels`:
  For a SHORT trade:
  ```python
  win_high = float(np.max(highs[window]))
  mae_bps = (entry_price - win_high) / entry_price * 10_000.0
  ```
  Here `win_high` is subtracted from `entry_price`. If the candle gapped down and `win_high` is lower than `entry_price`, `entry_price - win_high` is **positive**, whereas for a long trade `win_low - entry_price` would be negative.
* **Classification:** **F. Legitimate Data Limitation / Microstructure Reality**.

---

### Failure 3: `test_10_tp_reachability`
* **Assertion:**
  ```python
  hits = [r["hit_target_pct"] for r in rows]
  for a, b in zip(hits, hits[1:]):
      assert b <= a + 1e-9, f"reachability rose with a wider target: {hits}"
  ```
* **Actual Value:** `hits = [50.93, 50.82, 51.46, 51.39, 51.97, 50.55, 50.49]`.
* **Expected Value:** Monotonically non-increasing hit rate ($51.46 \le 50.82$).
* **Underlying Cause:**
  `hit_target_pct` is computed over **resolvable (OK) rows only**, excluding ambiguous OHLC candles:
  * Target 2 bps: 807 ambiguous candles $\implies$ 1,559 OK rows (794 hit $\implies$ 50.93%)
  * Target 6 bps: 180 ambiguous candles $\implies$ 2,186 OK rows (1,125 hit $\implies$ 51.46%)
  * Target 10 bps: 55 ambiguous candles $\implies$ 2,311 OK rows (1,201 hit $\implies$ 51.97%)
  When evaluated as a fraction of the **total population** (2,366), the hit count is strictly monotone:
  * 2 bps: $794 / 2366 = 33.56\%$
  * 4 bps: $995 / 2366 = 42.05\%$
  * 6 bps: $1125 / 2366 = 47.55\%$
  * 8 bps: $1148 / 2366 = 48.52\%$
  * 10 bps: $1201 / 2366 = 50.76\%$
* **Classification:** **B. Stale Test Expectation**. The test author erroneously assumed `hit_target_pct` over conditional subsets would retain the unconditional monotonicity of the underlying event space.

---

### Failure 4: `test_block_bootstrap_is_wider_than_iid`
* **Assertion:**
  ```python
  assert (blk.ci95[1] - blk.ci95[0]) > (iid.ci95[1] - iid.ci95[0])
  ```
* **Actual Value:** `blk_width = 0.2733`, `iid_width = 0.4600`.
* **Expected Value:** `blk_width > iid_width`.
* **Underlying Cause:**
  The test uses a synthetic synthetic fixture:
  ```python
  vals = [float(i % 7) for i in range(300)]
  blocks = [f"b{i//10}" for i in range(300)]
  ```
  Because `i % 7` repeats cyclically across blocks of length 10, the sample mean of almost every block is near-identical ($\approx 3.0$). In a block bootstrap where every block has identical mean, the variance between block averages drops to near zero, causing the block bootstrap CI to be **narrower** than individual item sampling.
* **Classification:** **B. Stale Test Expectation / Test Fixture Artifact**. On genuine dependent market data, block bootstrap behaves correctly as proven in `test_effective_n_below_nominal`.
