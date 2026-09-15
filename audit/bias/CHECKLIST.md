# AUDIT CHECKLIST: BIAS & SAMPLING ANOMALIES

Auditor: Claude (Red Team)

## Mandatory Verification Items

1. **Selection Bias**:
   * Verify candidate universe filtering was not conditioned on future variables or post-event volume/volatility spikes.
   * Verify all qualifying opportunities at $t_{decision}$ are evaluated without post-hoc culling.
2. **Survivorship Bias**:
   * Verify that delisted instruments, liquidated assets, or defunct symbols during the test period are included.
3. **Clustering & Independence**:
   * Check for repeated concurrent signals in short windows and verify effective degrees of freedom.
4. **Regime Balance**:
   * Audit whether the evaluated window is biased toward a single market regime (e.g. exclusively low-volatility trending markets).
