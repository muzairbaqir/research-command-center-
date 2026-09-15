# INDEPENDENT RED-TEAM RESEARCH AUDIT

Experiment ID:
EXP-XXX

Protocol Version:
EI-PROTOCOL-vX.X

Auditor:
Claude (Independent Research Validator)

Audit Date:
YYYY-MM-DD HH:MM UTC

---

> **PRIMARY AUDIT INQUIRY**: *"What could make this conclusion wrong?"*

---

## 1. Executive Summary & Audit Recommendation

Overall Assessment:
[PASS | CONCERNS_NOTED | REJECT_RECOMMENDED]

Highest Finding Severity:
[CRITICAL | HIGH | MEDIUM | LOW | PASS]

Summary:
[Concise synthesis of methodological soundness and key vulnerabilities]

---

## 2. Leakage & Temporal Audit

* [ ] **Look-Ahead Leakage**: Did any feature access data with $t > t_{decision}$?
* [ ] **Normalization Leakage**: Were scalers or encoders fit on full datasets rather than expanding historical windows?
* [ ] **Label Contamination**: Did any target calculation leak backward into feature space?
* [ ] **Overlapping Labels**: Were overlapping event horizons purged and embargoed?

*Findings*:
[Detail findings with line numbers / artifact references, or record PASS]

---

## 3. Bias & Sampling Audit

* [ ] **Selection Bias**: Were opportunities filtered using post-entry knowledge?
* [ ] **Survivorship Bias**: Are delisted, halted, or inactive instruments properly accounted for?
* [ ] **Duplicate / Clustered Events**: Were repeated concurrent signals artificially treated as independent?
* [ ] **Regime Imbalance**: Did sample concentration coincide with an anomalous macroeconomic/market regime?

*Findings*:
[Detail findings or record PASS]

---

## 4. Statistical Rigor Audit

* [ ] **Multiple Testing Penalty**: Were prior trials, searches, and parameter sweeps tracked and penalized?
* [ ] **Sample Size & Degrees of Freedom**: Is sample size adequate to reject the null hypothesis reliably?
* [ ] **Overfitting / Model Complexity**: Is parameter count disproportionate to independent opportunity count?
* [ ] **Outlier Dependency**: Does overall performance collapse if the top 1% of outliers are removed?

*Findings*:
[Detail findings or record PASS]

---

## 5. Microstructure & Execution Realism Audit

* [ ] **Fee Schedule**: Were realistic taker/maker exchange fees deducted?
* [ ] **Spread Cost**: Was half-spread or crossing cost explicitly deducted?
* [ ] **Slippage Model**: Is order size realistic relative to order book depth at entry time?
* [ ] **Latency & Fill Feasibility**: Was execution assumed instantaneous, or was queue/network latency modeled?

*Findings*:
[Detail findings or record PASS]

---

## 6. Reproducibility Verification

* [ ] Git commit matches execution code exactly.
* [ ] Deterministic seed and configuration verified.
* [ ] Raw data inputs verified against checksums.

---

## 7. Findings Register

| ID | Category | Severity | Description | Impact on Conclusion |
|----|----------|----------|-------------|----------------------|
| F-01 | Leakage / Bias / Stats / Exec | CRITICAL / HIGH / MED / LOW / PASS | | |
