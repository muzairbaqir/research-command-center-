# DECISION RECORD: INSUFFICIENT EVIDENCE

Decision ID:
DEC-INSUFFICIENT-EXP-XXX

Experiment ID:
EXP-XXX

Protocol Version:
EI-PROTOCOL-vX.X

Adjudicator:
ChatGPT (Research Architect)

Timestamp:
YYYY-MM-DD HH:MM UTC

---

## Qualification Criteria for INSUFFICIENT_EVIDENCE

An experiment is filed under `decisions/INSUFFICIENT/` when:
1. Sample size, event count, or statistical power is too degraded to draw meaningful statistical inferences.
2. Data pipeline drops, corrupt records, or missing intervals compromised sample continuity.
3. Execution was interrupted, non-converged, or marred by technical failures.
4. Neither acceptance nor rejection can be claimed with acceptable confidence intervals.

---

## Deficiency Breakdown

* **Source of Deficiency**: [Sample size collapse | Missing data | Pipeline error | High statistical variance]
* **Effective Sample Size**: [$N_{eff}$ observed vs. required threshold]
* **Remediation Plan**: [Data pipeline fix or extended historical sampling required before re-testing]
