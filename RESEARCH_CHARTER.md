# RESEARCH CHARTER

## Mission

Develop and rigorously evaluate Entry Intelligence research without allowing confirmation bias, leakage, overfitting, or uncontrolled experimentation.

---

## Principles

1. **Reproducibility**: Every finding, dataset, and evaluation metric must be deterministically reproducible from version-controlled artifacts and raw logs.
2. **Temporal Correctness**: Strict enforcement of time arrows. No feature, calculation, normalization, or label may reference information that was not available at prediction time.
3. **Independent Validation**: Execution and validation must remain strictly segregated across independent agents.
4. **Protocol Freezing**: Experiments must be executed against frozen, explicitly versioned protocols. No post-hoc adjustments.
5. **Explicit Assumptions**: All latency, fee, slip, market microstructure, and model constraints must be codified explicitly.
6. **Version Control**: Every protocol change, experiment configuration, and code commit must be tracked in version control.
7. **Evidence-Based Decisions**: Hypotheses succeed or fail solely on objective, pre-specified quantitative criteria.
8. **No Silent Methodology Changes**: Any adjustment to data filtering, model parameters, or validation windows requires a formal protocol amendment.
9. **No Cherry-Picking**: Negative and neutral findings are first-class research assets and must be cataloged in the experiment registry.
10. **No Result-Driven Protocol Modification**: Protocols cannot be altered to salvage a failing experiment or flatter an underperforming hypothesis.

---

## Agent Independence

To prevent self-validation, researcher degrees of freedom, and confirmation bias, agent responsibilities are strictly segregated:

* **Antigravity** produces evidence (implements, executes, logs, and extracts data).
* **Claude** challenges evidence (red-teams, audits leakage/bias/statistics, and probes edge cases).
* **ChatGPT** adjudicates evidence (designs protocols, synthesizes findings, and makes final decision calls).

> **Core Rule**: No agent can unilaterally validate its own work. Antigravity cannot certify its execution as valid, Claude cannot redesign the protocol it audits, and ChatGPT cannot invent execution outputs.
