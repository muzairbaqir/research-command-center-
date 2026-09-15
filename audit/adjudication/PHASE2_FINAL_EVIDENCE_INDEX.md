# PHASE 2 FINAL EVIDENCE INDEX

| CLAIM | SOURCE FILE | FUNCTION / CLASS | LINE RANGE | EVIDENCE TYPE | CONFIDENCE |
|---|---|---|---|---|---|
| Split is chronologically safe | `src/validation/phase3_walk_forward.py` | `run_walk_forward_validation` | ~L50-80 | DIRECT_CODE | HIGH |
| Features are causally safe | `scratch/generate_entry_features.py` | Global Fetch | ~L50 | DIRECT_CODE | HIGH |
| Trailing stops are path-dependent on 1m OHLC | `src/engine/youtube_master_scalper.py` | Signal loops | ~L14-480 | DIRECT_CODE | HIGH |
| C1 Hurdle is a static predefined $0.061\%$ | `src/validation/phase3_walk_forward.py` | `PortfolioEngine` | ~L86 | DIRECT_CODE | HIGH |
| Target Labels `.shift(-60)` are isolated | `experiments/phase5_cost_aware_engine.py` | `run_phase5a_diagnostics` | ~L102 | DIRECT_CODE | HIGH |
| Volatility filter is diagnostic only, not active | `experiments/phase5_cost_aware_engine.py` | `run_phase5a_diagnostics` | ~L120 | DIRECT_CODE | HIGH |
| Multiple Testing Risk via sequential phases | Project Directory | Iterative versioning | N/A | INFERENCE | MEDIUM |
| API boundary is strict `<= t_entry` | `scratch/generate_entry_features.py` | Global Fetch | ~L50 | DIRECT_CODE | HIGH |
