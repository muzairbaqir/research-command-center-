# RESEARCH PIPELINE

DATA
 `v2.0.0 Parquet Klines` & Live API Fetches
 ↓
PROCESSING
 `generate_entry_features.py`: Filters API responses to `k[6] <= t_entry`
 ↓
FEATURES
 `youtube_master_scalper.py`: Computes EMA(9,20,200), FVG, BOS, Choppiness, Vol Ratios, ATR-14
 ↓
LABELS
 `phase5_cost_aware_engine.py`: Pandas `.shift(-60)` for forward returns, adjusted by $C_1$ (0.061%) and 1.5x Volatility bounds
 ↓
TRAINING
 Handled historically (weights loaded from `pro_trader_learned_weights.json`)
 ↓
MODEL
 `YouTubeMasterScalper` combined with `pro_trader_evaluator`
 ↓
PREDICTION
 `FIB_GOLDEN_ZONE_LONG`, `INDICATOR_CROSSOVER`, etc.
 ↓
ENTRY INTELLIGENCE
 Volatility-aware filtering ($> 2.0\times C_1$)
 ↓
EXECUTION / BACKTEST
 `Phase3WalkForwardEngine` / `phase5_cost_aware_engine.py`: Walk-forward validation over 2021-2024
 ↓
METRICS
 Gross Move, Net Return, Edge-to-Cost Ratio, Profit Factor, Daily Sharpe, PBO, Deflated Sharpe Ratio
