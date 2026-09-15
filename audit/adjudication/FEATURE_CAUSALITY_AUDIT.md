# FEATURE CAUSALITY AUDIT

## Trace of Critical Features
All features examined in `scratch/generate_entry_features.py`:
- **EMAs (9, 20, 200)**: Calculated using `closes` up to `t_entry`. Safe.
- **FVG / BOS**: Computed over `highs`, `lows`, `closes` up to `t_entry`. Safe.
- **Volatility (ATR-14)**: Mean of past 14 high-low ranges. Safe.
- **Returns (5m, 15m)**: Computed using `closes[-1]` vs `closes[-6]` and `closes[-16]`. Safe.
- **Causality Rule**: `feature_timestamp <= decision_timestamp` is maintained strictly because the source array (`closed_klines`) rigorously truncates any kline where `close_time > t_entry`.

## Other Checks
- **Rolling Windows**: Look backward only.
- **Interpolation/Fills**: None used in the real-time feature generator.
- **Normalization**: No dataset-wide scaling (like `StandardScaler.fit_transform()` over the whole dataset) is present in the real-time script.

## Conclusion
**NOT AN ISSUE**. The real-time feature generation script `generate_entry_features.py` strictly adheres to temporal causality. There is no backward filling or future information leakage in the explicit feature calculations.
