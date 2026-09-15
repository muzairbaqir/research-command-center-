# PHASE 2 ADVERSARIAL SUMMARY

## 1. What previous analysis got right
The previous analysis correctly identified the Trailing Stop Path Dependence as a HIGH/CRITICAL risk due to the reliance on 1-minute OHLC boundaries, causing optimistic execution bias.

## 2. What previous analysis overstated
The previous analysis overstated the C1 Fixed Hurdle as a methodological bias. It is a predefined constraint. While it may underestimate extreme volatile slippage, it is a valid assumption for backtesting, not a data leakage risk. It also incorrectly stated Pandas `.shift(-h)` was a leakage risk, when it is securely isolated to the label pipeline.

## 3. What previous analysis missed
The previous analysis missed the Multiple Testing degradation caused by iterating up to Phase 5 on the same test sets (`2022`, `2023`, `2024`).

## 4. What remains genuinely unknown
The exact millisecond sync between WebSocket L2 ticks and REST API 1-minute kline closes remains unknown and requires live operational logging to verify.

## 5. Findings affecting research validity
- Trailing Stop Path Dependence (CRITICAL - Optimistic MFE/MAE).
- Multiple Testing (MEDIUM - Reduced OOS Confidence).

## 6. Findings affecting only production reliability
- Adaptive Volatility Barrier (Live logic divergence).
- Shutdown Orphans (In-memory state management).

## 7. Findings that can be controlled by protocol
All identified valid research findings (Trailing stops, Multiple testing) can be mitigated by strict rules in `EI-PROTOCOL-v1.0` (e.g., demanding tick-level simulations and declaring fresh holdouts).

## 8. Findings requiring remediation before Phase 3
None require immediate *code remediation* before protocol design, but the protocol itself MUST mandate the remediations be applied during Phase 3 execution.

## 9. Evidence coverage limitations
Analysis was limited to static code structures and historical parquet file definitions. Live event architectures could not be proven.
