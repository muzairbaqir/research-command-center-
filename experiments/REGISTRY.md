# EXPERIMENT REGISTRY

| ID | Protocol | Question | Status | Execution | Audit | Decision |
|----|----------|----------|--------|-----------|-------|----------|
| *None* | - | *No experiments initialized yet* | INITIALIZATION | - | - | - |

---

## Valid Experiment States

All experiments in this registry must reflect one of the following lifecycle states:

1. `PLANNED` — Experiment plan drafted in `experiments/EXP-XXX/PLAN.md`.
2. `APPROVED` — Plan reviewed and signed off by ChatGPT against frozen protocol.
3. `RUNNING` — Antigravity is actively executing the experiment code.
4. `EXECUTED` — Execution completed and raw results logged by Antigravity.
5. `UNDER_AUDIT` — Claude is conducting an independent red-team audit.
6. `UNDER_REVIEW` — ChatGPT is reviewing audit findings and execution data.
7. `VALIDATED` — Hypothesis satisfied all criteria, verified with zero critical audit defects.
8. `PLAUSIBLE` — Results promising but require further robustness or out-of-sample testing.
9. `REJECTED` — Hypothesis failed acceptance criteria or exhibited critical methodology flaws.
10. `INSUFFICIENT_EVIDENCE` — Inconclusive results, degraded sample size, or non-convergent runs.
11. `ABANDONED` — Experiment halted prior to completion due to protocol change or technical blocker.

> **Integrity Rule**: No experiment may be removed or erased from this registry. Negative and failed experiments are permanent scientific records.
