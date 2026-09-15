# PHASE 2 PROTOCOL BLOCKERS

| BLOCKER ID | ISSUE | WHY IT MATTERS | REQUIRED CONTROL | MUST BE RESOLVED BEFORE PHASE 3? | CAN IT BE HANDLED BY PROTOCOL? | EVIDENCE |
|---|---|---|---|---|---|---|
| PB-01 | Trailing Stop Path Dependence | 1-minute OHLC cannot resolve intra-candle order of TP vs SL execution, leading to optimistic simulated returns. | Mandate tick-level evaluation or pessimistic bounding (assume SL is hit first if both are in range) for all trailing stops. | YES | YES | `src/engine/youtube_master_scalper.py` uses OHLC boundaries for dynamic +6bps profit locks. |
| PB-02 | Multiple Testing Vulnerability | Repeatedly selecting strategy thresholds on the 2021-2024 test sets degrades OOS statistical validity. | Protocol must enforce strict hyperparameter locking or declare an explicit holdout (e.g., 2025 data or unobserved altcoins) for final scoring. | YES | YES | Phase 5 represents the 5th iteration on the same chronological expanding window. |
| PB-03 | Volatility Barrier Live Divergence | Volatility filtering is diagnostic, not active. | Protocol must mandate the barrier is embedded in the `PortfolioEngine` class before moving to live execution. | NO (Not for Phase 3 Research) | YES | `experiments/phase5_cost_aware_engine.py` L120. |

### Summary
The protocol (EI-PROTOCOL-v1.0) can handle these blockers without immediate code modification by establishing strict rules for the upcoming Phase 3 experiments (e.g., "All future simulations must use `tick` mode").
