# DEEP RESEARCH INTEGRITY REVIEW

## Finding 1: API Boundary Fetching (Timestamp Alignment)
**Finding**: Klines fetched dynamically restrict closure time exactly at `t_entry`.
**Severity**: MEDIUM
**Confidence**: HIGH
**Exact File**: `scratch/generate_entry_features.py`
**Function/Class**: Global scope feature fetch
**Relevant Code Behavior**: `closed_klines = [k for k in res if k[6] <= t_entry]` where `k[6]` is the close time.
**Evidence**: If `t_entry` is in the middle of a minute, `k[6] <= t_entry` correctly excludes the current forming candle. However, millisecond matching relies on Binance API internal clocks being perfectly synchronized with the event generator's `entry_time_ms`.
**Why it matters**: A millisecond discrepancy could either drop the previous valid candle or accidentally include a partially formed future candle if time definitions differ.
**Potential Consequence**: Minor data drift or look-ahead bias at the micro-structural level.
**Recommended Next Investigation**: Verify how `t_entry` is originally stamped in the upstream execution log.

## Finding 2: Pandas Shift for Target Returns
**Finding**: Target returns for backtest evaluation are generated using Pandas `.shift(-60)`.
**Severity**: LOW (Assuming purely evaluative)
**Confidence**: HIGH
**Exact File**: `experiments/phase5_cost_aware_engine.py`
**Function/Class**: `run_phase5a_diagnostics()`
**Relevant Code Behavior**: `move_60m_2023 = (df_2023["close"].shift(-60) / df_2023["close"] - 1.0).fillna(0.0) * 100`
**Evidence**: Found explicitly via AST AST deep scan.
**Why it matters**: `shift` is extremely dangerous if these target columns ever leak into a feature matrix or if training occurs on this same DataFrame.
**Potential Consequence**: Severe target leakage (look-ahead bias) if used for model training.
**Recommended Next Investigation**: Confirm that `run_phase5a_diagnostics()` only consumes the predictions of the Walk Forward engine and does not feed `move_60m` back into the training or feature pipeline.

## Finding 3: Hardcoded Fixed Slippage/Fee Assumptions
**Finding**: Execution cost is hardcoded as exactly $0.0610\%$ ($C_1$).
**Severity**: MEDIUM
**Confidence**: HIGH
**Exact File**: `experiments/phase5_cost_aware_engine.py`
**Function/Class**: `run_phase5a_diagnostics()`
**Relevant Code Behavior**: `c1_pct = 0.061`
**Evidence**: The entire Phase 5 redesign benchmarks edge against this static $0.061\%$ hurdle. 
**Why it matters**: Real market impact and slippage are dynamic. A fixed assumption ignores liquidity constraints on large trades or highly volatile jumps.
**Potential Consequence**: The backtest Sharpe of $+1.05$ could degrade substantially in live conditions if slippage exceeds the $0.061\%$ threshold.
**Recommended Next Investigation**: Integrate dynamic order book (L2) sweeping to model actual volume-weighted slippage instead of a flat hurdle.

## Finding 4: Multiple Take-Profit / Stop-Loss Logic Trailing
**Finding**: The strategy logic employs multi-stage trailing stops that rely on intra-candle price action.
**Severity**: HIGH
**Confidence**: HIGH
**Exact File**: `src/engine/youtube_master_scalper.py`
**Function/Class**: Scalper logic blocks
**Relevant Code Behavior**: Multi-stage profit locking logic checks dynamic RR SL distances.
**Evidence**: `take_profit = current_close + (dynamic_rr * sl_dist)`
**Why it matters**: If this trailing logic is simulated on 1-minute OHLCV data without tick-level resolution, it suffers from intra-candle path dependence ambiguity (did the high hit the TP before the low hit the SL?).
**Potential Consequence**: Highly optimistic backtest results that cannot be replicated live.
**Recommended Next Investigation**: Verify that the Walk Forward engine uses tick data or pessimistic assumptions for intra-candle execution.
