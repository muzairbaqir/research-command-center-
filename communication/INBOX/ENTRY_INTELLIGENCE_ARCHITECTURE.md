# ENTRY INTELLIGENCE ARCHITECTURE

## Overview
Entry Intelligence is a scalping prediction and execution engine currently on Phase 5. It is designed to identify high-probability micro-moves (120m horizon) that exceed transaction friction, utilizing an Adaptive Volatility Barrier to secure positive net expectancy.

## Entry Point
`phase5_2_engine_replay.py` and `experiments/phase5_cost_aware_engine.py` appear as the primary orchestrators for running the historical validation and diagnostic tests for Phase 5.

## Input Data
1-minute klines (OHLCV) combined with high-frequency L2 order book data (`entry_obi`, `l2_age_ms`). `generate_entry_features.py` fetches the last 250 klines bounded exactly by the `t_entry` millisecond timestamp.

## Data Flow
Raw Klines (Binance API/Parquet) -> Indicator Calculation (EMA, ATR, BOS, FVG) -> Signal Generation -> Replay Evaluation -> Cost-Aware Diagnostic Reporting.

## Feature Pipeline
`generate_entry_features.py` drives feature generation. It explicitly calculates:
- EMAs (9, 20, 200) and Price Distance to EMA200
- Break of Structure (BOS) and Fair Value Gaps (FVG)
- Choppiness Index and Volume Ratios
- Recent Returns (5m, 15m) and ATR-14

## Label Pipeline
Labels represent forward returns. In `phase5_cost_aware_engine.py`, forward returns are generated using Pandas `.shift(-60)` (and generalized to `-h`). An Adaptive Volatility Barrier (CFG-06, 1.5x volatility) is utilized to filter/target.

## Model Pipeline
The core logic relies on deterministic algorithmic scalpers (`youtube_master_scalper.py`, `smart_pro_scalper.py`) combined with pre-trained evaluation layers (implied by `pro_trader_learned_weights.json`).

## Prediction Pipeline
Event-driven predictions are produced when indicators align (e.g., FIB_GOLDEN_ZONE combined with OBI and EMA alignment).

## Entry Decision Pipeline
Decision logic uses multiple layers: 
- Hard signal alignment
- Volatility filtering ($> 2.0\times C_1$)
- Slippage/l2 freshness gates

## Backtest Integration
Replay engines (`phase3_walk_forward`, `phase5_cost_aware_engine`) simulate historical execution. The simulation subtracts a fixed $0.061\%$ ($C_1$) friction from gross returns. Take Profit and Stop Loss levels are dynamically trailed.

## Evaluation
Out-of-sample walk-forward validation produces Net P&L, Profit Factor, Edge-to-Cost Ratio, and Daily Sharpe.

## Configuration
Currently parameterized inline or via JSON (e.g., `trades_meta` config inside `generate_entry_features.py`).

## Dependencies
- `src.engine.youtube_master_scalper`
- `src.validation.phase3_walk_forward`
- `pandas`, `numpy`, `scipy`, `sklearn`

## Critical Files
- `experiments/phase5_cost_aware_engine.py`
- `scratch/generate_entry_features.py`
- `src/engine/youtube_master_scalper.py`
- `phase5_2_engine_replay.py`

## Unknowns
- How the adaptive volatility barrier is actively enforced in real-time execution (is it predicted volatility or backward-looking ATR?).
- Exact implementation of `Phase3WalkForwardEngine`.

## Risks
- Timestamp millisecond alignment discrepancies during live streaming vs historical 1m candle fetching.
- Pandas `.shift(-h)` overlapping issues if trades are clustered.
- $0.061\%$ fixed execution cost assumption failing during extreme volatility.
