# AUDIT CHECKLIST: LEAKAGE & TEMPORAL INTEGRITY

Auditor: Claude (Red Team)

## Mandatory Verification Items

1. **Information Availability Horizon**:
   * Verify every feature's timestamp $t_{avail} \le t_{decision}$.
   * Verify exchange timestamp vs local clock arrival time (latency gap).
2. **Global Preprocessing Contamination**:
   * Verify scalers (MinMaxScaler, StandardScaler) are fit solely on walk-forward historical training folds, never full-sample.
   * Verify PCA, rolling quantiles, or mean encodings do not leak future information.
3. **Label Contamination**:
   * Verify target return calculation starts strictly at or after execution fill timestamp ($t_{fill} \ge t_{decision}$).
   * Verify overlapping trade/signal periods are purged and embargoed.
4. **Order Book & Microstructure Leakage**:
   * Confirm book state snapshot used corresponds to pre-trade state, not post-trade execution tick.
