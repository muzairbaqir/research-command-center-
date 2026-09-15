# ENTRY INTELLIGENCE RESEARCH PROTOCOL

Protocol ID:
EI-PROTOCOL-v0.1

Status:
DRAFT

---

## 1. Research Question

[TBD - To be defined by ChatGPT Architect prior to protocol freeze]

---

## 2. Hypothesis

[TBD - Clear, falsifiable hypothesis establishing the theoretical and empirical premise]

---

## 3. Opportunity Definition

[TBD - Precise criteria defining what constitutes an entry candidate, event trigger, or signal opportunity]

---

## 4. Feature Definitions

[TBD - All features must be explicitly declared before execution. Ad-hoc or dynamic feature additions are prohibited.]

Every feature must define:

* **Feature Name**: Identifier conforming to naming conventions.
* **Mathematical Definition**: Exact algorithmic / mathematical formula.
* **Input Data**: Primary data streams and fields required (e.g., L2 book, trades).
* **Timestamp**: Point-in-time timestamping rules.
* **Lookback Window**: Historical calculation horizon $[t - \Delta t, t]$.
* **Information Availability Time**: Timestamp $t_{avail}$ when the data point is fully received and processed.
* **Allowed Information**: Exhaustive list of signals and states accessible without looking ahead.

---

## 5. Label Definition

[TBD - Quantitative definition of outcome labels, e.g., forward return, excursion, fill state]

Must explicitly specify:
* Prediction horizon / event boundary
* Calculation timestamp alignment ($t_{eval} > t_{entry}$)
* Handling of unclosed positions or edge-of-sample data points

---

## 6. Leakage Rules

The following are strictly prohibited:

* Future price information
* Future order-book information
* Future labels
* Future-derived features (e.g., full-sample centering, z-scoring across future intervals)
* Post-event information
* Information unavailable at prediction time ($t_{info} > t_{decision}$)

---

## 7. Dataset Rules

Must explicitly document and verify:

* **Source**: Raw data exchange, vendor, or internal feed.
* **Period**: Inclusive start and end timestamps (UTC).
* **Timezone**: Explicitly UTC across all pipelines.
* **Duplicates**: De-duplication rules and conflict resolution policies.
* **Missing Data**: Handling of missing ticks, drops, or heartbeat timeouts.
* **Gaps**: Identification and treatment of exchange maintenance and downtime gaps.
* **Sampling**: Sampling cadence (event-based, tick, volume, or fixed time).
* **Filtering**: Outlier detection, spread anomaly filters, and volume thresholds.
* **Exclusions**: Documented exclusions with scientific justification (no post-hoc exclusions).

---

## 8. Validation Methodology

* **Temporal validation is the mandatory default** (walk-forward, expanding window, or rolling out-of-sample testing).
* **Random train/test splitting is strictly prohibited** unless explicitly justified, mathematically proven to have zero autocorrelation/leakage, and approved via formal protocol amendment.
* Purging and embargoing must be applied around event-driven or overlapping label horizons.

---

## 9. Cost Model

All candidate evaluations must incorporate realistic transaction and friction costs:

* **Fees**: Explicit maker/taker tier fee schedules.
* **Spread**: Half-spread or dynamic crossing costs observed at $t_{entry}$.
* **Slippage**: Order size vs. available depth impact models.
* **Latency**: Decision-to-exchange wire delay + matching engine queue time.
* **Execution Assumptions**: Passive queue position vs. aggressive taker fills.

---

## 10. Metrics

### Statistical Metrics
* [TBD - e.g., Information Coefficient (IC), Rank IC, Precision, ROC-AUC, Log-Loss, Brier Score]

### Trading Metrics
* [TBD - e.g., Expected Value per trade (EV), Sharpe Ratio, Sortino Ratio, Max Drawdown, Calmar Ratio, Profit Factor after costs]

---

## 11. Statistical Controls

Every experiment must consider and report:

* **Multiple Testing**: Corrections for family-wise error rate or False Discovery Rate (FDR / White's Reality Check / Deflated Sharpe).
* **Sample Size**: Minimum required opportunity count for statistical significance.
* **Confidence Intervals**: Bootstrapped or robust analytical confidence intervals for all primary metrics.
* **Bootstrap Analysis**: Stationary bootstrap or block bootstrap across market regimes.
* **Regime Sensitivity**: Sub-period performance breakdown across volatility, trend, and volume regimes.
* **Data Snooping**: Tracking total researcher trials and model permutations.

---

## 12. Acceptance Criteria

[TBD - Quantitative thresholds that must be met simultaneously for hypothesis validation, e.g., EV > $X$ bps after costs with $p < 0.01$ and zero critical audit findings]

---

## 13. Protocol Change Policy

* Any change to methodology, feature definitions, dataset filtering, cost models, or acceptance criteria requires a new protocol version or a formally approved protocol amendment in `protocols/CHANGE_REQUESTS/`.
* **Silent changes are prohibited.** Running an experiment with unapproved modifications renders the results automatically **REJECTED**.
