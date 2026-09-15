# ENTRY INTELLIGENCE RISK REGISTER

| ID | Category | Finding | Evidence | Severity | Confidence | Affected Component | Affected Files | Protocol Implication | Status |
|---|---|---|---|---|---|---|---|---|---|
| RISK-01 | Timestamp | Millisecond synchronization reliance on API boundary | `closed_klines = [k for k in res if k[6] <= t_entry]` | MEDIUM | HIGH | Feature Pipeline | `generate_entry_features.py` | Need strict definition of `t_entry` provenance | OPEN |
| RISK-02 | Leakage | Pandas `.shift(-60)` for target returns | `df["close"].shift(-60)` in diagnostic code | LOW (if eval only) | HIGH | Evaluation Pipeline | `phase5_cost_aware_engine.py` | Must guarantee strict separation of evaluation vs feature generation | OPEN |
| RISK-03 | Execution | Hardcoded static friction hurdle ($0.061\%$) | `c1_pct = 0.061` | MEDIUM | HIGH | Backtest Assumptions | `phase5_cost_aware_engine.py` | Must incorporate dynamic order book liquidity | OPEN |
| RISK-04 | Execution | Intra-candle path dependence on trailing stops | `take_profit = current_close + (dynamic_rr * sl_dist)` | HIGH | HIGH | Model / Entry Logic | `youtube_master_scalper.py` | Requires tick-level replay for walk-forward validation | OPEN |
