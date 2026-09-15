# TIMESTAMP SYNCHRONIZATION AUDIT

## Trace of Timestamp Pipeline
- **Exchange Timestamps**: Binance provides kline close time (`k[6]`) and open time (`k[0]`) in milliseconds since epoch.
- **Local / Event Timestamps**: `entry_time_ms` is generated or assigned to the event.
- **Fetch Logic**: `closed_klines = [k for k in res if k[6] <= t_entry]`

## Potential Synchronization Risks
- **Transformation/Truncation**: None observed. It uses strict `<=` inequality on exact millisecond integers.
- **Boundary Condition (T=1000 vs 999)**: If the event triggers at `1000` ms, but the kline closed at `1000` ms, the kline is included. If it triggers at `999` ms, it is excluded.
- **Future Leakage**: Because it uses strict `k[6] <= t_entry`, a kline that closes *after* `t_entry` is correctly excluded. No future candle is included in the feature set. 
- **Time Definitions**: The only remaining risk is if `t_entry` is derived from an asynchronous websocket stream that is delayed. If the local system creates `t_entry` at `T+5` seconds due to lag, then fetching `k[6] <= t_entry` might include a 1-minute kline that actually closed *after* the raw orderbook event physically happened at the exchange.

## Conclusion
**NOT AN ISSUE / HARMLESS IMPLEMENTATION DETAIL** (with a caveat about live socket latency). The historical feature construction safely excludes future candles based on strict millisecond matching. No synthetic resampling or interpolation creates future timestamps in the feature generation script.
