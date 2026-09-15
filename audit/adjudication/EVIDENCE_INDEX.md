# EVIDENCE INDEX

| Claim | Evidence File | Source File | Function/Class | Evidence Type | Confidence |
|---|---|---|---|---|---|
| Split is chronologically safe | `SPLIT_PURGE_EMBARGO_AUDIT.md` | `src/validation/phase3_walk_forward.py` | `run_walk_forward_validation` | DIRECT_CODE | HIGH |
| Feature generation is causally safe | `FEATURE_CAUSALITY_AUDIT.md` | `scratch/generate_entry_features.py` | Global Fetch | DIRECT_CODE | HIGH |
| Trailing stops are path-dependent | `TRAILING_STOP_RESOLUTION_AUDIT.md` | `src/engine/youtube_master_scalper.py` | Signal loops | DIRECT_CODE | HIGH |
| C1 Hurdle is static | `C1_HURDLE_AUDIT.md` | `src/validation/phase3_walk_forward.py` | `PortfolioEngine` init | DIRECT_CODE | HIGH |
| Label leakage is isolated | `LABEL_CONSTRUCTION_AUDIT.md` | `experiments/phase5_cost_aware_engine.py` | `run_phase5a_diagnostics` | DIRECT_CODE | HIGH |
