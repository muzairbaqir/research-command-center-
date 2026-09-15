# MASTER TWO-REPOSITORY INTEGRATION MATRIX

**Audit Date:** 2026-09-15  
**Auditor:** Antigravity  
**Governance Authority:** Research Command Center  

---

## 1. Master Integration Matrix

| Research Item | Binance Evidence Path | Command Center Evidence Path | Protocol Governing | Independent Review Status | Adjudication Status | Final Consolidated Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CFG-06 Adaptive Barrier (+16.38% Net PnL)** | `reports/phase6_final_live_readiness_report.md` | `audit/adjudication/VOLATILITY_BARRIER_AUDIT.md` | Unapproved (`phase6_frozen_config.json`) | Antigravity Phase 2 review | Rejected by Protocol Blockers PB-01/PB-02 | **REJECTED / BLOCKED** |
| **Trailing Stop 1m Resolution** | `src/engine/youtube_master_scalper.py` | `audit/adjudication/TRAILING_STOP_RESOLUTION_AUDIT.md` | Pre-protocol | Antigravity Phase 2 review | Protocol Blocker PB-01 | **BLOCKED** |
| **Purged K-Fold & Multiple Testing** | `validation/phase3_walk_forward.py` | `audit/adjudication/SPLIT_PURGE_EMBARGO_AUDIT.md` | Pre-protocol | Antigravity Phase 2 review | Protocol Blocker PB-02 | **BLOCKED** |
| **Phase 1E-R.4 Egress & Rate-Limit Hardening** | `audit/phase1e_r/phase1er4_trade_ledger.csv` | `audit/phase6/TRADE_LEVEL_RECONCILIATION.md` | `PHASE1ER4_EXECUTION_CONTRACT.md` | Antigravity Phase 6 review | Reconciled (5 trades, -$0.0993 USDT) | **PLAUSIBLE (DESCRIPTIVE)** |
| **Phase 1E-R.5 Test Ledger Pollution** | `audit/phase1e_r/phase1er5_trade_ledger.csv` | `audit/phase6/R5_LEDGER_POLLUTION_FORENSICS.md` | `PHASE1ER5_EXECUTION_CONTRACT.md` | Antigravity Phase 6 review | Quarantined; 7 genuine trades recovered | **VALIDATED (DEFECT CONFIRMED)** |
| **Phase 1E-R.6A Maker Decay Mechanism** | `audit/phase1e_r/phase1er6a_trade_ledger.csv` | `audit/phase6/TRADE_LEVEL_RECONCILIATION.md` | R6-A Post-Remediation Spec | Antigravity Phase 6 review | Reconciled (4 trades, -$0.4556 USDT) | **PLAUSIBLE (MECHANISM ONLY, N=4)** |
| **Phase 5.3 Entry Intelligence Edge Analysis** | `audit/phase5_3/PHASE5_3_FINAL_DECISION.md` | `audit/phase6/PHASE5_3_DEPENDENCY_ASSESSMENT.md` | 15-Task Protocol (`6ecc79f`) | Claude Haiku 4.5 / Antigravity | NO Entry Intelligence justified | **VALIDATED** |
| **Phase 6 Forensics Suite (28 Pass, 4 Fail)** | `tests/test_phase6_forensics.py` | `audit/phase6/TEST_FAILURE_DIAGNOSIS.md` | 27 Forensic Specs | Antigravity Phase 6 review | Submitted in HF-0001 | **VALIDATED WITH LIMITATIONS** |
| **Phases 7–9 Simulated Paper Trading** | `reports/phase7_final_paper_trading_report.md` | `audit/integration/LATER_PHASE_GOVERNANCE_AUDIT.md` | Legacy unapproved | None | None | **UNADJUDICATED / CONTAMINATED** |
| **Live RCCD Data Ingestion (PIDs 13504, 6331)** | `data/live_l2/{symbol}_depth5.jsonl` | `audit/phase6/LIVE_RCCD_DATA_LINEAGE.md` | Continuous Live Stream | Antigravity Live Audit | Verified continuous append, unpolluted | **VALIDATED** |
