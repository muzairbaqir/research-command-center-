# PHASE 2 INDEPENDENT RISK MATRIX

| ID | Finding | Evidence | Source File | Relevant Function/Class | Why it matters | Severity | Confidence | Reproducibility | Recommended Next Action |
|---|---|---|---|---|---|---|---|---|---|
| IND-01 | Trailing stop path-dependence lacking tick resolution | Trailing checks against 1-min OHLC | `src/engine/youtube_master_scalper.py` | Trailing SL Blocks | MFE/MAE are skewed; false TP hits assumed. | HIGH | HIGH | 100% | Run tick-level simulation to measure variance vs 1-min baseline. |
| IND-02 | Static execution hurdle ($C_1$) underestimates volatility slippage | `cost_friction=0.00061` | `src/validation/phase3_walk_forward.py` | `Phase3WalkForwardEngine` | Skews Edge-to-Cost metrics during extreme breakouts. | MEDIUM | HIGH | 100% | Integrate dynamic L2 volume-weighted slippage modeling. |
| IND-03 | Adaptive volatility barrier not enforced in walk-forward execution | Barrier used as post-hoc diagnostic filter | `experiments/phase5_cost_aware_engine.py` | `run_phase5a_diagnostics()` | Live trading behavior will diverge from backtest if deployed. | MEDIUM | HIGH | 100% | Refactor `PortfolioEngine` to explicitly reject trades when `volatility_60 < threshold_move`. |
