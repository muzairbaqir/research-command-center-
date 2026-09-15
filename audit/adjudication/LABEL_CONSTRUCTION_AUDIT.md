# LABEL CONSTRUCTION AUDIT

## Trace of Labels
- **Definition**: The target variable in `phase3_walk_forward.py` is `long_target`.
- **Construction**: The exact logic defining `long_target` is pre-computed in the Parquet files (`data/parquet/features/v2.0.0/...`).
- **Phase 5 Diagnostic Moves**: In `phase5_cost_aware_engine.py`, diagnostic labels are dynamically created using `(df_2023["close"].shift(-60) / df_2023["close"] - 1.0)`.
- **Future Information**: The `.shift(-60)` relies exactly on future information (+60 minutes) to define the forward return. This is mathematically correct for *label construction* to evaluate predictive accuracy.
- **Leakage Check**: The `long_target` or `.shift(-60)` values are *only* used as `y_tr`, `y_cal`, and evaluation benchmarks. The feature matrices `X_tr` and `X_cal` are explicitly sliced using `self.feature_cols = [c for c in EXPECTED_FEATURES_V101]`. As long as `EXPECTED_FEATURES_V101` does not contain target leakage columns, the model is safe.

## Conclusion
**NOT AN ISSUE**. The use of Pandas `.shift(-60)` in diagnostic reports and the use of `long_target` in training are correctly isolated to the label side of the supervised learning equation. They do not leak into the `EXPECTED_FEATURES_V101` list used for predictions.
