# PHASE 2 EVIDENCE PACKAGE INDEX

| Filename | Purpose | Evidence Type | Primary Source Files | Primary Findings | Confidence | Known Limitations |
|---|---|---|---|---|---|---|
| `TRAILING_STOP_RESOLUTION_AUDIT.md` | Audit trailing stop mechanics | DIRECT_CODE | `src/engine/youtube_master_scalper.py`, `Phase3WalkForwardEngine` | Path-dependence on 1-min OHLC causes ambiguous order of TP/SL triggers. | HIGH | Exact divergence requires tick-level re-simulation to quantify. |
| `TIMESTAMP_SYNCHRONIZATION_AUDIT.md` | Audit API timestamps | DIRECT_CODE | `scratch/generate_entry_features.py` | Strict `<=` logic cleanly isolates past/future data. | HIGH | Cannot test live network millisecond drift statically. |
| `C1_HURDLE_AUDIT.md` | Audit fixed cost friction | DIRECT_CODE | `src/validation/phase3_walk_forward.py` | Valid static assumption ($0.061\%$), but underestimates high-volatility slippage. | HIGH | - |
| `VOLATILITY_BARRIER_AUDIT.md` | Audit adaptive filter | DIRECT_CODE | `experiments/phase5_cost_aware_engine.py` | Filter is applied offline post-hoc, not actively inside the `PortfolioEngine` simulation loop. | HIGH | - |
| `FEATURE_CAUSALITY_AUDIT.md` | Audit look-ahead bias in features | DIRECT_CODE | `scratch/generate_entry_features.py` | Features generated strictly on closed data prior to `t_entry`. | HIGH | - |
| `LABEL_CONSTRUCTION_AUDIT.md` | Audit target variables | DIRECT_CODE | `experiments/phase5_cost_aware_engine.py` | Forward labels (`.shift(-60)`) are securely isolated from training features. | HIGH | - |
| `SPLIT_PURGE_EMBARGO_AUDIT.md` | Audit cross-validation | DIRECT_CODE | `src/validation/phase3_walk_forward.py` | Expanding walk-forward implements chronological splitting with a 75-candle purge gap. | HIGH | - |
| `EXECUTION_MODEL_AUDIT.md` | Audit simulator fidelity | INFERENCE | `src/validation/phase3_walk_forward.py` | Simulator assumes immediate fill and lacks tick-level partial fill logic. | HIGH | - |
| `PHASE2_INDEPENDENT_RISK_MATRIX.md` | Synthesize risks | SYNTHESIS | All above | Trailing stop lacks tick resolution (HIGH). | HIGH | - |
| `ANTIGRAVITY_VS_INDEPENDENT_FINDINGS.md` | Dispute original findings | SYNTHESIS | All above | Downgraded Pandas leakage and timestamp sync to NOT-A-RISK. | HIGH | - |
| `EVIDENCE_INDEX.md` | Map claims to code | SYNTHESIS | All above | Correlates assertions to source files. | HIGH | - |
| `ADJUDICATION_COVERAGE.md` | Scope of review | SYNTHESIS | All above | 100% structural, 4 critical files semantically verified. | HIGH | - |
| `PHASE2_ADJUDICATION_PACKAGE.md` | Final executive summary | SYNTHESIS | All above | System is CONDITIONAL_READY for protocol design. | HIGH | - |
| `EVIDENCE_QUALITY_REVIEW.md` | Verification of evidence | SYNTHESIS | All above | Validates all claims are backed by direct code. | HIGH | - |
| `INTERNAL_CONSISTENCY_CHECK.md` | Ensure no contradictions | SYNTHESIS | All above | No contradictions found. | HIGH | - |
