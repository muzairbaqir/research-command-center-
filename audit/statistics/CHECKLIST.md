# AUDIT CHECKLIST: STATISTICAL RIGOR & CONTROLS

Auditor: Claude (Red Team)

## Mandatory Verification Items

1. **Multiple Testing & Data Snooping**:
   * Count total historical parameter sweeps and prior model iterations.
   * Apply False Discovery Rate (FDR) / Benjamini-Hochberg or Deflated Sharpe corrections.
2. **Sample Size & Statistical Power**:
   * Confirm effective sample size $N_{eff}$ is sufficient to reject null hypothesis $H_0$ at pre-specified $\alpha$.
3. **Overfitting & Degrees of Freedom**:
   * Audit ratio of parameters/rules to independent events.
   * Verify performance does not hinge on extreme outliers (evaluate winsorized / trimmed returns).
4. **Bootstrap & Stability Analysis**:
   * Review block bootstrap distributions and confidence intervals across folds.
