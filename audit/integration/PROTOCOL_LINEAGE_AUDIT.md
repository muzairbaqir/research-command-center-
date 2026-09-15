# PROTOCOL LINEAGE AUDIT

**Audit Date:** 2026-09-15  
**Auditor:** Antigravity  

---

## 1. Protocol Inventory Across Repositories

```text
[GOVERNANCE PROTOCOL LINEAGE]
Command Center:
  ├── EI-PROTOCOL-v0.1 (DRAFT, initial scaffolding in protocols/)
  └── EI-PROTOCOL-v1.0 (BLOCKED pending Phase 2/6 adjudication)

[UNGOVERNED INTERNAL EXPERIMENT CONFIGS]
Binance Repo:
  ├── research/phase6_frozen_configuration.json (Legacy Phase 6 CFG-06 spec)
  ├── audit/phase1d/experiment_contract.json (Mode 07 4-arm testnet contract)
  ├── audit/phase1e_r/PHASE1ER4_EXECUTION_CONTRACT.md (R4 egress/rate-limit contract)
  ├── audit/phase1e_r/PHASE1ER5_EXECUTION_CONTRACT.md (R5 extended validation contract)
  └── scripts/phase5_3_*.py (Phase 5.3 15-task empirical protocol)
```

---

## 2. Chain of Custody Trace: Experiment → Protocol → Commit → Result

### Trace A: Phase 5.3 Entry Intelligence Edge Analysis
* **Experiment:** `EXP-PHASE5-3-EI`
* **Protocol Version:** Phase 5.3 15-Task Protocol
* **Protocol Commit:** Implemented directly in commit `6ecc79f` (Co-authored with Claude Haiku 4.5).
* **Execution Commit:** `6ecc79f`
* **Result Commit:** `6ecc79f`
* **Result Artifacts:** `audit/phase5_3/*.md` (15 task documents, 2,366 rows).
* **Chain Status:** **COMPLETE BUT RETROSPECTIVE / LOCAL.** All components committed atomically in a single commit without prior Command Center registration.

### Trace B: Phase 1E-R Extended Validation (R4, R5, R6-A)
* **Experiment:** Mode 07 Master Scalper Egress & Execution Hardening
* **Protocol Version:** `PHASE1ER4_EXECUTION_CONTRACT.md` / `PHASE1ER5_EXECUTION_CONTRACT.md`
* **Protocol Commit:** `7005277` / `aa1f08a`
* **Execution Commit:** `aa1f08a`
* **Result Commit:** `aa1f08a` (Untracked local CSVs in `audit/phase1e_r/`)
* **Chain Status:** **BROKEN AT PERSISTENCE.** Primary execution ledgers (`phase1er5_trade_ledger.csv`) remained uncommitted/untracked, allowing a unit test to overwrite R5.

### Trace C: Legacy Phase 6–9
* **Experiment:** CFG-06 Adaptive Volatility Barrier Walk-Forward
* **Protocol Version:** `phase6_frozen_configuration.json`
* **Protocol Commit:** `fe4579d`
* **Execution Commit:** `fe4579d`
* **Result Commit:** `fe4579d`
* **Chain Status:** **ATOMIC LEGACY DUMP.** An entire 42-phase research program was committed in bulk (`fe4579d`) without step-by-step governance provenance.

---

## 3. Silent Methodology Changes Identified

1. **Intra-candle Execution Assumption:** Legacy Phase 6 assumed limit/stop orders fill favorably at candle high/low boundaries. Phase 2 adjudication revealed that 1m OHLC bars cannot resolve intra-candle sequencing, injecting an optimistic bias.
2. **OBI Reclassification:** In Phase 5.3, `cluster_signals` and `cluster_end_ts` were initially treated as metadata features, causing artificial edge detection. When reclassified as `FUTURE_INFORMATION` and barred, the apparent edge vanished completely.
3. **Quarantine of R5 Ledger:** Phase 6 forensics detected that `phase1er5_trade_ledger.csv` contained test-fixture outputs, shifting the authoritative data source to `R5_TRADE_FORENSICS.csv`.
