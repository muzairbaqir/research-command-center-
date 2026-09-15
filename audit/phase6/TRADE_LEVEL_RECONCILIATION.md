# PHASE 6 — INDIVIDUAL TRADE-LEVEL RECONCILIATION DOSSIER

**Audit Date:** 2026-09-15  
**Baseline Repository:** `/Users/uzair/Documents/binance`  
**Total Usable Executed Trades:** 16  
**Excluded Polluted Fixtures:** 2 (`TEST1`, `TEST2` quarantined from `phase1er5_trade_ledger.csv`)  
**Excluded Archive Runs:** 1 (`phase1er6a_trade_ledger_run2_archived.csv` known-defective pre-remediation)

---

## 1. Complete Trade-by-Trade Reconciliation Matrix

| Trade ID | Arm | Symbol | Dir | Entry TS | Exit TS | Entry Px | Exit Px | Qty | Gross PnL ($) | Fees ($) | Net PnL ($) | Exchange Order IDs | Telemetry Evidence Source | Provenance Class | Rec. Diff | Status / Flags |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **R4-1** | R4 | XRPUSDT | LONG | 2026-09-08 17:14:18 | 2026-09-08 17:15:33 | 1.46710 | 1.46832 | 19.7 | +$0.0240 | $0.0173 | +$0.0067 | Entry: 3501240182 | `phase1er4_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | CONFIRMED |
| **R4-2** | R4 | XRPUSDT | LONG | 2026-09-08 17:16:43 | 2026-09-08 17:17:21 | 1.47030 | 1.47090 | 25.0 | +$0.0150 | $0.0221 | -$0.0071 | Entry: 3501242194 | `phase1er4_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | CONFIRMED |
| **R4-3** | R4 | XRPUSDT | LONG | 2026-09-08 17:19:03 | 2026-09-08 17:19:35 | 1.47120 | 1.47110 | 25.0 | -$0.0025 | $0.0221 | -$0.0246 | Entry: 3501245012 | `phase1er4_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | CONFIRMED |
| **R4-4** | R4 | BNBUSDT | SHORT| 2026-09-08 17:22:24 | 2026-09-08 17:23:12 | 726.540 | 727.410 | 0.05 | -$0.0435 | $0.0218 | -$0.0653 | Entry: 2641982103 | `phase1er4_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | CONFIRMED |
| **R4-5** | R4 | SOLUSDT | LONG | 2026-09-08 17:28:37 | 2026-09-08 17:29:44 | 104.420 | 104.430 | 0.17 | +$0.0017 | $0.0107 | -$0.0090 | Entry: 4202941084 | `phase1er4_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | CONFIRMED |
| **R5-1** | R5 | XRPUSDT | LONG | 2026-09-14 21:15:51 | 2026-09-14 21:16:25 | 1.45020 | 1.45136 | 25.0 | +$0.0290 | $0.0145 | +$0.0145 | Entry: 3502193985 / TP: 3502194000 | `R5_TRADE_FORENSICS.csv` | ACTUAL (L1) | 0.00000000 | CONFIRMED (Maker TP Hit) |
| **R5-2** | R5 | ETHUSDT | LONG | 2026-09-14 21:17:32 | 2026-09-14 21:18:37 | 2551.77 | 2551.77 | 0.02 | $0.0000 | $0.0306 | -$0.0306 | Entry: 16794641337 / Exit: 16794641834 | `R5_TRADE_FORENSICS.csv` | ACTUAL (L1) | 0.00000000 | DEGENERATE_EXIT_PX |
| **R5-3** | R5 | BNBUSDT | SHORT| 2026-09-14 21:19:10 | 2026-09-14 21:19:14 | 725.770 | 725.189 | 0.05 | +$0.0290 | $0.0145 | +$0.0145 | Entry: 2642801527 / TP: 2642801534 | `R5_TRADE_FORENSICS.csv` | ACTUAL (L1) | 0.00000000 | CONFIRMED (Maker TP Hit) |
| **R5-4** | R5 | BTCUSDT | LONG | 2026-09-14 21:16:05 | 2026-09-14 21:20:59 | 78934.4 | 78934.4 | 0.0007 | $0.0000 | $0.0332 | -$0.0332 | Entry: 28585790738 / Exit: 28585797529 | `R5_TRADE_FORENSICS.csv` | ACTUAL (L1) | 0.00000000 | DEGENERATE_EXIT_PX |
| **R5-5** | R5 | BNBUSDT | SHORT| 2026-09-14 21:26:11 | 2026-09-14 21:31:17 | 724.860 | 724.860 | 0.05 | $0.0000 | $0.0217 | -$0.0217 | Entry: 2642806157 / Exit: 2642808541 | `R5_TRADE_FORENSICS.csv` | ACTUAL (L1) | 0.00000000 | DEGENERATE_EXIT_PX (300s Cap) |
| **R5-6** | R5 | SOLUSDT | SHORT| 2026-09-14 21:38:10 | 2026-09-14 21:43:22 | 103.260 | 103.260 | 0.35 | $0.0000 | $0.0217 | -$0.0217 | Entry: 4203840439 / Exit: 4203843914 | `R5_TRADE_FORENSICS.csv` | ACTUAL (L1) | 0.00000000 | DEGENERATE_EXIT_PX (300s Cap) |
| **R5-7** | R5 | BNBUSDT | SHORT| 2026-09-14 21:49:04 | 2026-09-14 21:49:24 | 723.830 | 723.830 | 0.05 | $0.0000 | $0.0217 | -$0.0217 | Entry: 2642815355 / Exit: 2642815491 | `R5_TRADE_FORENSICS.csv` | ACTUAL (L1) | 0.00000000 | DEGENERATE_EXIT_PX |
| **R6A-1**| R6A| BNBUSDT | LONG | 2026-09-15 10:02:48 | 2026-09-15 10:07:53 | 718.040 | 718.040 | 0.08 | $0.0000 | $0.0230 | -$0.0230 | Entry: 2643169765 | `phase1er6a_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | NORMAL_MAKER_EXIT |
| **R6A-2**| R6A| DOGEUSDT| LONG | 2026-09-15 10:04:23 | 2026-09-15 10:09:27 | 0.08273 | 0.08267 | 400.0 | -$0.0240 | $0.0132 | -$0.0372 | Entry: 2343695636 | `phase1er6a_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | NORMAL_MAKER_EXIT |
| **R6A-3**| R6A| BTCUSDT | SHORT| 2026-09-15 10:22:14 | 2026-09-15 10:24:14 | 76895.1 | 76921.3 | 0.001 | -$0.0262 | $0.0461 | -$0.0723 | Fallback: 28586381264 | `phase1er6a_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | EMERGENCY_OBI_EXIT |
| **R6A-4**| R6A| XRPUSDT | SHORT| 2026-09-15 11:51:42 | 2026-09-15 11:56:50 | 1.39540 | 1.39860 | 80.0 | -$0.2560 | $0.0671 | -$0.3231 | Maker: 3502642249 / Fallback: 3502642313 | `phase1er6a_trade_ledger.csv` | ACTUAL (L1) | 0.00000000 | NORMAL_FALLBACK_EXIT |

---

## 2. Aggregate Arm Reconciliation

* **R4 (5 trades):** Gross: -$0.0053 USDT | Net: -$0.0993 USDT | Rec Diff: `0.00000000` (PASS)
* **R5 (7 trades):** Gross: +$0.0580 USDT | Net: -$0.0999 USDT | Rec Diff: `0.00000000` (PASS)
* **R6A (4 trades):** Gross: -$0.3062 USDT | Net: -$0.4556 USDT | Rec Diff: `0.00000000` (PASS)
* **Total Portfolio Net PnL (16 trades):** -$0.6548 USDT.
