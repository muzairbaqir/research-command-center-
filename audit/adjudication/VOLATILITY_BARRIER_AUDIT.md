# VOLATILITY BARRIER AUDIT

## Trace of Adaptive Volatility Barrier
- **Definition**: The volatility barrier requires `volatility_60 > threshold_move` where `threshold_move = mult * c1_pct`. (e.g., $1.5 \times 0.061\%$).
- **Inputs**: `vol_2023 = df_2023[vol_col]`. The column is `volatility_60`.
- **Timestamp Availability**: If `volatility_60` is calculated using past 60 minutes of rolling standard deviation of returns, it is available at `t_entry`. 
- **Enforcement**: In `phase5_cost_aware_engine.py`, the barrier is tested strictly as a filter (`filter_mask = vol_2023 > threshold_move`). It is a diagnostic post-hoc analysis (`run_phase5a_diagnostics`), *not* currently embedded in the primary `Phase3WalkForwardEngine` execution logic.
- **Code Paths / Divergence**: Because it is analyzed in `experiments/phase5_cost_aware_engine.py` over an already-executed walk-forward output (`df_2023`), it is *not* actively enforced during the actual `PortfolioEngine` simulation loop. Therefore, live and historical simulations *will* diverge if the live system expects this barrier to reject trades, but the walk-forward validation did not reject them during model scoring.

## Conclusion
**CONFIRMED ISSUE / UNKNOWN LIVE STATE.** The adaptive volatility barrier is evaluated as an offline diagnostic filter. There is no evidence in `youtube_master_scalper.py` or `phase3_walk_forward.py` that it is actively enforced during the entry prediction pipeline. If deployed live, the system will execute trades in low-volatility regimes that the Phase 5 diagnostic claims are filtered out.
