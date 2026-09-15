# SPLIT / PURGING / EMBARGO AUDIT

## Trace of Train/Validation/Test Splits
- **Implementation**: Handled in `Phase3WalkForwardEngine.run_walk_forward_validation()`.
- **Chronological Ordering**: `df["year"] < test_yr` for train, `df["year"] == test_yr` for test. Chronological ordering is strictly maintained. No random shuffling is used.
- **Validation Split**: Training set is split 80% Train, 20% Calibration (`df_tr`, `df_cal`).
- **Purging / Embargo**: 
  - `split_idx + 75:` is used to gap Train and Calib.
  - `purge_start_ts = df_cal["open_time"].max() + (75 * 60000)` strictly enforces a 75-minute embargo before the Test window begins.
- **Overlap**: Since the maximum label horizon being predicted is 60 minutes, a 75-minute purge gap is mathematically sufficient to prevent overlapping label windows from leaking from train into calibration or from calibration into test.

## Conclusion
**NOT AN ISSUE / CONFIRMED SAFE**. The system implements an expanding walk-forward validation with strict chronological boundaries and a 75-candle purge gap, which safely exceeds the 60-candle maximum label horizon. The methodology is robust against temporal leakage.
