# CRITICAL FILE MAP

| Priority | File | Component | Why Critical | Dependencies | Risk |
|----------|------|-----------|--------------|--------------|------|
| 1 | `scratch/generate_entry_features.py` | Feature Generation | Directly translates raw market data into predictive model inputs at millisecond precision. | `youtube_master_scalper.py`, Binance API | Timestamp Leakage (if API boundary conditions are mishandled) |
| 1 | `experiments/phase5_cost_aware_engine.py` | Engine / Labels / Validation | Drives the Phase 5 baseline evaluation. Contains pandas forward-shift label logic and walk-forward validation integration. | `Phase3WalkForwardEngine`, `parquet` datasets | Target Leakage (if `shift(-h)` metrics bleed into features), Multiple Testing |
| 1 | `src/engine/youtube_master_scalper.py` | Engine | Contains the deterministic trade logic, indicator calculation (EMA, BOS, FVG), and dynamic trailing stop logic. | `numpy`, `pandas` | Look-ahead Bias (if indicators compute over global future scopes), Overfitting |
| 1 | `phase5_2_engine_replay.py` | Backtest Integration | Governs simulated execution over the Phase 5 engine logic. | Internal frameworks | Execution Realism (fees, slippage assumptions) |
| 2 | `src/infrastructure/egress_gate.py` | Execution | Handles egress flow and possibly live trade routing. | None directly | Information asymmetry between backtest and live egress. |
| 2 | `tests/test_phase5_cost_aware.py` | Validation | Validates the integrity of the cost-aware engine. | `phase5_cost_aware_engine.py` | Test coverage gaps |
