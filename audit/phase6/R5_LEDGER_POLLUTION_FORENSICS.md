# PHASE 6 — R5 LEDGER POLLUTION FORENSIC AUDIT

**Audit Date:** 2026-09-15  
**Investigated Target:** `audit/phase1e_r/phase1er5_trade_ledger.csv` & `.json`  
**Baseline Repository:** `/Users/uzair/Documents/binance`  
**Author:** Antigravity (Research Engineer / Forensic Evidence Tracer)  
**Evidence Classification:** CODE TRACE & FILE SYSTEM FORENSICS

---

## 1. Executive Summary

A critical forensic defect occurred when running unit tests in the Binance repository: `tests/test_phase1er5_mechanisms.py` directly instantiated `Phase1ER5ValidationRunner`, which had module-level hardcoded output paths pointing to production audit files. As a result, running `pytest` overwrote the real R5 ledger with mock unit-test data (`TEST1` and `TEST2`).

The genuine 7 live/testnet R5 trades were **NOT lost**: they were independently captured with complete tick and order telemetry in `audit/phase1e_r/R5_TRADE_FORENSICS.csv` and `evidence/phase1er5_telemetry.jsonl`.

---

## 2. Ten Forensic Questions & Conclusive Verdicts

### Q1: What exact file/path was polluted?
* `audit/phase1e_r/phase1er5_trade_ledger.csv`
* `audit/phase1e_r/phase1er5_trade_ledger.json`

### Q2: When was it created / polluted?
* **Pollution Timestamp:** `2026-09-15 20:27:33` (Timestamp recorded in the two synthetic rows).
* File system metadata indicates this occurred during automated test execution.

### Q3: Which process created it?
* A `pytest` test-runner execution process running `tests/test_phase1er5_mechanisms.py:test_r5_fee_accounting_maker_vs_taker`.

### Q4: Was it created by RCCD live execution or by a test?
* **100% Confirmed created by a TEST.**
* The rows contain `symbol: "TEST1"` and `symbol: "TEST2"`, with synthetic `$100.0` entry prices and mocked responses from `unittest.mock.patch`.

### Q5: Does the live RCCD process currently write to the same path?
* **NO.** The currently active live processes are `scripts/capture_all_l2_depth.py` (PID 13504) and `scripts/capture_l2_depth.py` (PID 6331). They write strictly to `data/live_l2/`. The R5 execution experiment was completed on September 14, 2026, and is no longer running.

### Q6: Can test execution overwrite live evidence?
* **Historically YES, for R5.** Because `phase1er5_extended_validation.py` lines 76–77 defined `ledger_csv = PROJECT_ROOT / "audit" / "phase1e_r" / "phase1er5_trade_ledger.csv"` at the module scope, any test calling `runner.reconcile_completed_trade()` without mocking disk writes overwrote this file.
* In contrast, R6-A (`scripts/phase1er6a_extended_validation.py`) hardened this by pointing tests to `.test_artifacts/`.

### Q7: Are the 7 R5 trades genuine live trades?
* **YES.** All 7 R5 trades are genuine live executions conducted on Binance USD-M Futures testnet on September 14, 2026, between 21:15:51 UTC and 21:49:24 UTC.

### Q8: Which source independently confirms each trade?
Each trade is independently corroborated across four separate evidence sources:
1. `audit/phase1e_r/R5_TRADE_FORENSICS.csv` (contains full order IDs, client order IDs, and exact fill times).
2. `audit/phase1e_r/evidence/phase1er5_telemetry.jsonl` (contains real-time JSON event logs).
3. `audit/phase1e_r/R5_FINAL_FORENSIC_POSTMORTEM.md` (authoritative experiment report).
4. Real Binance Exchange Order IDs:
   * Trade 1 (XRP): Entry `3502193985`, TP `3502194000`
   * Trade 2 (ETH): Entry `16794641337`, Exit `16794641834`
   * Trade 3 (BNB): Entry `2642801527`, TP `2642801534`
   * Trade 4 (BTC): Entry `28585790738`, Exit `28585797529`
   * Trade 5 (BNB): Entry `2642806157`, Exit `2642808541`
   * Trade 6 (SOL): Entry `4203840439`, Exit `4203843914`
   * Trade 7 (BNB): Entry `2642815355`, Exit `2642815491`

### Q9: Why do 5/7 trades have `exit_price == entry_price`?
* **Root Cause:** Degenerate price logging in `scripts/phase1er5_extended_validation.py:726`:
  ```python
  exit_px = pos_info.get("exit_price", entry_px)
  ```
  When an emergency exit (OBI persistent pressure or 300s time-cap) fired, a `MARKET` `reduceOnly` order was dispatched to the exchange, but the script did not wait to query the fill price from the WebSocket before recording the trade, defaulting to `entry_px`.
* Gross PnL was recorded as $0.0$, but full taker commission ($4.0\text{ bps}$) was charged, yielding a net loss of $-6.0\text{ bps}$ per trade.
* This is an identified telemetry limitation documented in Phase 6, flagged as `EXIT_PRICE_EQUALS_ENTRY_PRICE`.

### Q10: Are these actual exchange executions, reconstructed trades, or fixtures?
* **Classification:** **LEVEL 1 ACTUAL TRADES** with genuine exchange order IDs and verified commission debits. They are neither reconstructed opportunities nor synthetic fixtures.
