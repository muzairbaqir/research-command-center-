# TRAILING STOP RESOLUTION AUDIT

## 1. Where Trailing Stops Are Defined
Trailing stops are defined in `src/engine/youtube_master_scalper.py` within the `run_strategy` or specific signal simulation blocks. The specific logic checks:
`take_profit = current_close + (dynamic_rr * sl_dist)`
and utilizes trailing profit lock tiers (e.g., locking +6 bps at +12 bps float).

## 2. Where Stop State Is Stored
The stop state (`take_profit`, `stop_loss`) is maintained in memory during the execution loop of the backtest framework.

## 3. How Stop State Changes Over Time
As `current_close` (the close price of the current candle) advances, the trailing lock checks if the current unrealized P&L exceeds specific thresholds (12 bps, 25 bps) and ratchets the `stop_loss` upward to lock in profit.

## 4. Market-Resolution Data Driving Stop Movement
The logic observed in the Phase 5 baseline relies entirely on 1-minute `close` prices, or at best 1-minute `high`/`low`/`close` data points (OHLCV). 

## 5. Decision Data Used
- [x] candles/bars (1-minute OHLCV)
- [ ] tick data
- [ ] L2 events
- [ ] trades

## 6. Intrabar Path Knowledge
**UNKNOWN/NO.** Standard OHLCV data lacks the intra-candle path. It is impossible to know definitively whether the `high` (triggering a take profit) occurred before the `low` (triggering a stop loss) within the same 1-minute candle.

## 7. First Occurred (TP vs SL)
The backtest cannot determine which occurred first within a single 1-minute bar if the bar's range `(High - Low)` encompasses both the TP and SL levels.

## 8. OHLC Used for Event-Level Requirements
**YES.** The engine uses 1-minute OHLC to evaluate sub-minute trailing stop triggers (e.g., 6 bps moves). A 6 bps move can easily happen multiple times inside a single 1-minute candle in high volatility.

## 9. Potential Bias
- **Win Rate**: Optimistically biased (if the backtest assumes TP is hit before SL).
- **MFE / MAE**: Distorted by missing intra-bar extremes.
- **Expected Return / Risk**: Optimistically biased.

## Conclusion
**CONFIRMED ISSUE.** The system employs path-dependent trailing stop logic (+6 bps lock on +12 bps float) evaluated against 1-minute OHLCV candles, which lack the tick resolution required to resolve intra-candle triggering order. This introduces optimistic execution bias into the walk-forward evaluation.
