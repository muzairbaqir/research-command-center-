# ACTUAL RESEARCH TIMELINE RECONSTRUCTION

**Audit Date:** 2026-09-15  
**Source Repository:** `/Users/uzair/Documents/binance`  
**Auditor:** Antigravity  

---

## 1. Longitudinal Research Phase Chronology

The Binance repository exhibits **two distinct historical research lineages**:
* **Lineage A: Legacy Global AI Platform (Phases 1–42)**: Conducted August 2026 (commits `fe4579d` through `166a136`), testing macroeconomic walk-forwards, PBO/DSR, and CFG-06 adaptive volatility barrier.
* **Lineage B: Microstructure Scalper & Entry Intelligence (Phase 1B–1E-R, Phase 5.3, Phase 6)**: Conducted September 2026 (commits `e1ec1f8` through `6ecc79f`), focused on L2 order book imbalance (OBI), sub-second execution, maker decay, and entry predictability.

---

## 2. Research Phase Summary Table

| Phase / Campaign | Commit / Date | Primary Objective | Dataset Used | Methodology | Result / Finding | Formal Governance Status | Evidence Classification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1–5 (Legacy)** | `fe4579d`<br>(2026-08-26) | Walk-forward validation, cost hurdle ($0.061\%$), feature selection | 2,103,840 1m candles (2021–2024) | Walk-forward split, Purged K-Fold | Identified CFG-06 Adaptive Barrier (H=120m, 1.5x vol) | `NOT_ADJUDICATED` (Legacy prior to Command Center) | DOCUMENTED_ONLY / HISTORICAL |
| **Phase 6 (Legacy)** | `fe4579d`<br>(2026-08-26) | 16-Category Live Readiness Scorecard | 2,103,840 1m candles (2021–2024) | DSR ($N=15$), PBO ($4.12\%$), 10k Block Bootstrap | Reported Gate A: "Independently Verified" (+16.38% Net PnL) | `NOT_ADJUDICATED` (Pre-dates RCCD) | DOCUMENTED_ONLY / HISTORICAL |
| **Phase 7 (Legacy)** | `fe4579d`<br>(2026-08-26) | Simulated Paper Trading on 2025-H1 | 259,200 1m candles (2025-H1) | Synthetic execution, latency scenarios | Reported Gate A: +2.02% Net PnL, Sharpe 1.02, $N=24$ trades | `NOT_ADJUDICATED` | DOCUMENTED_ONLY / HISTORICAL |
| **Phase 8 (Legacy)** | `fe4579d`<br>(2026-08-26) | Prospective Paper Trading Validation | 259,200 1m candles (2025-H1) | Failure injection, dual reproducibility | Reported Gate A: +2.02% Net PnL, $N=24$ trades | `NOT_ADJUDICATED` | DOCUMENTED_ONLY / HISTORICAL |
| **Phase 9 (Legacy)** | `fe4579d`<br>(2026-08-26) | Full-year 2025 Unseen Paper Trading | 524,160 1m candles (2025 Full Year) | Continuous 1m streaming simulation | Reported Gate A: +4.08% Net PnL, $N=48$ trades | `NOT_ADJUDICATED` | DOCUMENTED_ONLY / HISTORICAL |
| **Phase 10–29** | `fe4579d`–`166a136`<br>(2026-08-27) | Extensive holdout evaluation, CFG06 remediation | Historical backtests & synthetic streams | Iterative remediation campaigns (R1–R18) | Iterative tuning across holdouts | `METHODOLOGY_UNVERIFIED` / `NOT_ADJUDICATED` | RECONSTRUCTED |
| **Phase 1B–1D (Scalper)**| `e1ec1f8`–`a454622`<br>(2026-09-08) | Mode 07 Master Scalper Multi-Symbol L2 capture | Real-time Binance Futures WS | Controlled multi-arm experiments | Multi-arm testnet execution (49 trades) | `NOT_ADJUDICATED` | ACTUAL (Level 1) |
| **Phase 1E-R.4** | `aa1f08a`<br>(2026-09-08) | Egress hardening & rate-limit testing | Live Testnet Binance USD-M | Oracle VM egress gate, dedicated IP | 5 completed trades, gross -$0.0053 USDT | `NOT_ADJUDICATED` | ACTUAL (Level 1) |
| **Phase 1E-R.5** | `aa1f08a`<br>(2026-09-14) | Extended validation candidate daemon | Live Testnet Binance USD-M | Passive maker TP + adverse OBI kill | 7 completed trades, gross +$0.0580 USDT | `NOT_ADJUDICATED` (Polluted by unit test) | ACTUAL (Level 1) |
| **Phase 1E-R.6A** | `aa1f08a`<br>(2026-09-15) | Post-remediation clean live run | Live Testnet Binance USD-M | Maker decay mechanism | 4 completed trades, gross -$0.3062 USDT | `NOT_ADJUDICATED` | ACTUAL (Level 1) |
| **Phase 5.3 (EI)** | `6ecc79f`<br>(2026-09-15) | Entry Intelligence conditional edge analysis | 2,366 2026 opportunities (`entry_opportunities_2026.jsonl`) | 4 cost models, 15 causal features, 109 hypotheses | **DECISION: NO** — No conditional entry edge found | `NOT_ADJUDICATED` (Completed in binance, awaiting RCCD) | RECONSTRUCTED / ACTUAL |
| **Phase 6 (Forensics)**| Untracked<br>(2026-09-15) | Live-readiness forensic suite & ledger reconciliation | 16 actual trades + 2,366 opportunities | 27 forensic specs, dual ledger audit | 28 pass, 4 fail (all 4 diagnosed) | `NOT_ADJUDICATED` (Submitted in HF-0001) | ACTUAL / RECONSTRUCTED |
