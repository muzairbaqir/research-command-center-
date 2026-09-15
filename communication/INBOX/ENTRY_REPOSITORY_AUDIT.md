# ENTRY INTELLIGENCE EXECUTION REPOSITORY AUDIT

Date: 2026-09-15

Repository: binance

Absolute Path: /Users/uzair/Documents/binance

Git Branch: main

Latest Commit: aa1f08ad52f3e3cf17269dfa82ac26df38d7ba0a

Working Tree: Clean (unmodified by Command Center)

## 1. Repository Overview
The repository contains the canonical Entry Intelligence Phase 5 execution environment, modeling Binance Spot & USD-M Futures. The repository focuses on cost-aware economic signal redesign for an AI trading platform.

## 2. Current Phase
Improvement Phase 5 is complete. The system is ready for review before Phase 6 (Independent Live-Readiness Verification).

## 3. Phase 5.1
Status: Complete
Evidence: Documented in `reports/phase5_final_report.md`
Files: `reports/phase5_final_report.md`

## 4. Phase 5.2
Status: Complete (Engine Replay)
Evidence: Engine replay files exist.
Files: `phase5_2_engine_replay.py`, `audit/phase5_2/`

## 5. Phase 5.3
Status: Unknown/Folded into main Phase 5 timeline
Evidence: Final report mentions Volatility-Aware Economic Filtering.
Files: `reports/phase5_final_report.md`

## 6. Phase 5.4
Status: Unknown/Folded into main Phase 5 timeline
Evidence: Final report covers all Phase 5.
Files: `reports/phase5_final_report.md`

## 7. Phase 5.5
Status: Unknown/Folded into main Phase 5 timeline
Evidence: Final report confirms Phase 5 is fully complete and ready for Phase 6.
Files: `reports/phase5_final_report.md`, `walkthrough_phase5.md`

## 8. Dataset Inventory
- Raw Datasets: `data/raw/`, `data/realtime/`
- Processed Datasets: `data/cleaned/`, `data/parquet/`
- Generated Datasets: `data/bootstrap_klines_cache.json`, `data/quality_reports/`
- Other: `data/captures/`, `data/checksums/`, `data/manifests/`

## 9. Feature Inventory
- Exponential Moving Averages (EMA 9, 20, 200)
- Distance to EMA200 (bps)
- Choppiness Index
- Volume SMA and Volume Ratio
- Break of Structure (BOS)
- Fair Value Gap (FVG) size (bps)

## 10. Label Inventory
- Target Horizon: 120 minutes (Adaptive Volatility Barrier)
- Scaling: 1.5x volatility multiplier
- Target is designed to expand the expected gross move to +0.1450%, covering friction.

## 11. Validation Methodology
- Out-of-sample multi-year validation (2021–2024)
- 4-year canonical dataset v2.0.0 (2,103,840 candles)
- Trade count filtered from 1,494 to 195.

## 12. Execution / Cost Model
- Standard C1 Friction / Trade: 0.0610% (Binance fee + slippage hurdle)
- Edge-to-Cost Ratio (E[Gross] / C1) modeled at 2.38

## 13. Existing Experiments
- Phase 5A.1: Cost-Aware Trade Economic Distribution
- Phase 5A.3: Volatility-Aware Economic Filtering
- Phase 5A.5 & 5A.6: Adaptive Target Redesign (CFG-06)

## 14. Existing Tests
- `tests/test_phase5_cost_aware.py`
- `tests/test_phase28_entry_reconciliation.py`
- `tests/test_phase1er4_order_lifecycle.py`
- `tests/test_phase1er4_rate_limit.py`

## 15. Research Integrity Risks

| Risk | Location | Severity | Evidence | Investigation |
|------|----------|----------|----------|---------------|
| Look-ahead leakage | `scratch/generate_entry_features.py` | Medium | Kline fetch uses exact `t_entry` timestamp to filter `k[6] <= t_entry`. | Ensure `t_entry` matches strict market availability and isn't preempting actual trade execution bounds. |
| Overlapping labels | 120m target horizon | Low | 120-minute forward horizon means close trades could share future data. | Investigate if any of the 195 trades occurred within 120m of each other, violating IID assumption. |
| Unrealistic execution | `walkthrough_phase5.md` | Medium | Fixed C1 friction modeled at 0.0610%. | Validate whether 0.061% accurately bounds both taker fees and slippage on low liquidity jumps. |

## 16. Missing Information
- Specifics on Phase 5.3 to 5.5 standalone outputs (they appear merged into the final Phase 5 report).
- The exact mechanism for the "1.5x volatility scaling" logic for labels.

## 17. Recommended Next Actions
- ChatGPT review of this execution repository audit.

## 18. Files Inspected
- `walkthrough_phase5.md`
- `reports/phase5_final_report.md`
- `scratch/generate_entry_features.py`
- `data/` directory listing
