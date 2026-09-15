# Research Command Center

The **Research Command Center** is the centralized control plane and research governance layer for the **Entry Intelligence** multi-agent quantitative research project.

It provides a single source of truth for the scientific pipeline:

$$\text{Hypothesis} \longrightarrow \text{Protocol} \longrightarrow \text{Experiment} \longrightarrow \text{Execution} \longrightarrow \text{Evidence} \longrightarrow \text{Audit} \longrightarrow \text{Decision} \longrightarrow \text{Next Experiment}$$

---

> ## CORE PRINCIPLE
> 
> ### **NO RESULT IS VALID BECAUSE AN AI SAYS IT IS VALID.**
> 
> A computational result becomes empirical evidence **only** after passing through four mandatory gates:
> 1. **Frozen Protocol**: Pre-specified hypothesis, features, labels, and acceptance criteria.
> 2. **Reproducible Execution**: Deterministic code, locked dependencies, and immutable data hashes.
> 3. **Independent Red-Team Audit**: Adversarial verification for leakage, bias, and execution realism.
> 4. **Decision Gate**: Formal adjudication against pre-committed success criteria.

---

## Why the Command Center Exists

In AI-assisted quantitative research, language models exhibit strong tendencies toward confirmation bias, researcher degrees of freedom, silent methodology drifting, and data leakage. Without rigorous governance:
* Agents tweak features post-hoc to salvage failing hypotheses.
* Unpenalized multiple testing inflates apparent performance.
* Look-ahead leakage creeps into scalers, features, and target boundaries.
* Negative experiments are quietly abandoned without records.

The Command Center eliminates researcher degrees of freedom by separating the **governance layer** from the **computational execution layer** and segregating agent responsibilities.

---

## Strict Separation of Repositories

| Repository | Responsibility | Contents |
|---|---|---|
| **Research Command Center** *(This Repo)* | Research Governance & Control Plane | Protocols, experiment registry, agent roles, handoffs, audit checklists, decisions, project state, change requests. |
| **Entry Intelligence Execution Repo** *(External)* | Computational Execution & Pipelines | Source code, models, feature engineering pipelines, dataset generation, backtest runners, raw data, model weights, execution logs. |

> **CRITICAL RULE**: The Command Center references the external execution repository via version tags and git commit hashes. It never duplicates, moves, or overwrites execution codebase assets.

---

## Three-Agent Architecture

To prevent self-validation and confirmation bias, responsibilities are segregated across three specialized agents:

```
                  ┌─────────────────────────────────┐
                  │            CHATGPT              │
                  │   Research Architect / Decision │
                  └───────┬─────────────────▲───────┘
   1. Protocols & Plans   │                 │ 4. Adjudication & Decision
                          ▼                 │
                  ┌─────────────────┐       │
                  │   ANTIGRAVITY   │       │
                  │ Executor/Builder│       │
                  └───────┬─────────┘       │
      2. Execution Record │                 │ 3. Independent Audit
      & Empirical Data    ▼                 │
                  ┌─────────────────────────┴───────┐
                  │             CLAUDE              │
                  │  Red-Team Validator / Critic    │
                  └─────────────────────────────────┘
```

### 1. [ChatGPT](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/agents/CHATGPT_ROLE.md)
* **Role**: Research Architect / Strategist / Decision Layer
* **Responsibilities**: Formulates research questions, hypotheses, experimental architectures, protocols, acceptance criteria, and final experiment adjudications.
* **Prohibitions**: Cannot fabricate results, claim unexecuted experiments succeeded, or alter protocols post-hoc.

### 2. [Antigravity IDE](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/agents/ANTIGRAVITY_ROLE.md)
* **Role**: Research Engineer / Builder / Executor
* **Responsibilities**: Implements code in the execution repo, builds clean datasets, computes features/labels, runs backtests, and produces raw execution reports with cryptographic commit hashes.
* **Prohibitions**: Cannot alter methodology silently, remove inconvenient samples, cherry-pick results, or certify its own work.

### 3. [Claude](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/agents/CLAUDE_ROLE.md)
* **Role**: Independent Research Validator / Red-Team Critic
* **Responsibilities**: Driven by the question *"What could make this conclusion wrong?"*, independently audits code, data pipelines, timestamps, leakage, statistical power, and microstructural assumptions.
* **Prohibitions**: Cannot edit execution code or protocols, and does not render the final decision.

---

## Research State Machine

No experiment may transition from execution directly to validation. Every finding must clear red-team audit:

```text
IDEA
 ↓
PLANNED
 ↓
APPROVED
 ↓
EXECUTED
 ↓
UNDER AUDIT
 ↓
UNDER REVIEW
 ↓
 ┌──────────────┬───────────────┬───────────────┐
 ▼              ▼               ▼               ▼
VALIDATED    PLAUSIBLE       REJECTED      INSUFFICIENT
```

### Decision Gates

Every completed experiment terminates in exactly one classification:
* **`VALIDATED`**: Pre-specified acceptance criteria fully met; zero `CRITICAL` or `HIGH` red-team audit findings; 100% reproducible.
* **`PLAUSIBLE`**: Promising empirical results exceeding baseline, but with noted medium-severity caveats or regime dependencies requiring further testing.
* **`REJECTED`**: Failed acceptance criteria, falsified hypothesis, or critical methodological/leakage flaws. (Rejections are recorded permanently as successful scientific eliminations).
* **`INSUFFICIENT_EVIDENCE`**: Degraded sample size, pipeline errors, or statistical power too low to support a conclusion.

---

## Research Integrity Rules

1. **No Cherry-Picking**: Every experiment launched must be entered in [experiments/REGISTRY.md](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/experiments/REGISTRY.md). Negative results are first-class assets.
2. **No Hidden Exclusions**: Every data filter, outlier exclusion, or dropped symbol must be explicitly justified ex-ante.
3. **No Future Information**: All features and data points must strictly respect information availability horizons ($t_{avail} \le t_{decision}$).
4. **No Result-Driven Methodology**: The research protocol cannot be tweaked because an initial run produced an unfavorable metric.
5. **No Multiple-Testing Blindness**: All parameter iterations, feature explorations, and backtest variations must be logged and penalized using multiple-testing adjustments.
6. **No Silent Changes**: Any alteration to feature math, data windows, cost models, or acceptance criteria requires a versioned [Change Request](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/protocols/CHANGE_REQUESTS/CHANGE_REQUEST_TEMPLATE.md).
7. **No Self-Validation**: The agent implementing the experiment (Antigravity) cannot validate or adjudicate its own output.

---

## Communication & Handoff System

All inter-agent handoffs are logged in structured Markdown documents inside [`communication/HANDOFFS/`](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/communication/HANDOFFS/) using [`HANDOFF_TEMPLATE.md`](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/communication/HANDOFFS/HANDOFF_TEMPLATE.md).

* Conversational memory is ephemeral; the filesystem is the project's permanent auditable memory.
* Every handoff links explicitly to an Experiment ID (`EXP-XXX`) and Protocol Version (`EI-PROTOCOL-vX.X`).

---

## Directory Structure

```text
research-command-center/
│
├── README.md                           # Master governance documentation
├── PROJECT_STATE.md                    # Central real-time project state
├── RESEARCH_CHARTER.md                 # Research philosophy & principles
├── RESEARCH_PROTOCOL.md                # Active research protocol framework
│
├── agents/                             # Agent role charters and boundaries
│   ├── CHATGPT_ROLE.md                 # Architect / Strategist / Adjudicator
│   ├── ANTIGRAVITY_ROLE.md             # Builder / Executor / Reproducibility
│   └── CLAUDE_ROLE.md                  # Independent Red-Team Validator
│
├── communication/                      # Formal inter-agent communications
│   ├── INBOX/                          # Incoming tasks awaiting processing
│   ├── OUTBOX/                         # Outgoing dispatched handoffs
│   ├── HANDOFFS/                       # Structured handoff artifacts
│   │   └── HANDOFF_TEMPLATE.md         # Template for all handoffs
│   └── ARCHIVE/                        # Completed communication records
│
├── protocols/                          # Protocol management & versioning
│   ├── CURRENT_PROTOCOL.md             # Active frozen protocol pointer
│   ├── VERSION_HISTORY.md              # Historical protocol changelog
│   └── CHANGE_REQUESTS/                # Formal protocol amendment requests
│       └── CHANGE_REQUEST_TEMPLATE.md  # Template for methodology changes
│
├── experiments/                        # Experiment catalog & templates
│   ├── REGISTRY.md                     # Permanent master experiment ledger
│   └── TEMPLATE/                       # Standardized experiment pack
│       ├── PLAN.md                     # Pre-execution experiment specification
│       ├── EXECUTION.md                # Verifiable execution chronology & metadata
│       ├── RESULTS.md                  # Raw empirical measurements (no opinions)
│       ├── CLAUDE_AUDIT.md             # Independent red-team critique
│       └── DECISION.md                 # Final adjudication & classification
│
├── decisions/                          # Formal decision records
│   ├── VALIDATED/                      # Experiments meeting all criteria
│   ├── PLAUSIBLE/                      # Promising experiments requiring more data
│   ├── REJECTED/                       # Disproven hypotheses or flawed runs
│   └── INSUFFICIENT/                   # Inconclusive or degraded runs
│
├── audit/                              # Red-team verification checklists
│   ├── leakage/                        # Look-ahead & temporal integrity
│   ├── bias/                           # Selection, survivorship & clustering
│   ├── statistics/                     # Sample size, FDR & multiple testing
│   ├── execution/                      # Fees, slippage, latency & spread
│   └── reproducibility/                # Commits, environments & seeds
│
├── logs/                               # Operational logs
│   ├── execution/                      # Antigravity run traces
│   ├── audits/                         # Claude red-team reports
│   └── decisions/                      # Final adjudication notices
│
└── config/                             # Command Center configuration
    └── project.yaml                    # System configuration & pointers
```

---

## Protocol Versioning & Change Policy

Any modification to research methodology must adhere to the following workflow:

1. **Change Request Initiated**: Documented using [`CHANGE_REQUEST_TEMPLATE.md`](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/protocols/CHANGE_REQUESTS/CHANGE_REQUEST_TEMPLATE.md).
2. **Red-Team Bias Review**: Claude reviews the proposed change for data snooping or bias risks.
3. **Architect Approval**: ChatGPT formally approves or rejects the change.
4. **Version Increment**: The protocol is versioned in [`protocols/VERSION_HISTORY.md`](file:///Users/uzair/.gemini/antigravity-ide/scratch/research-command-center/protocols/VERSION_HISTORY.md) and frozen.