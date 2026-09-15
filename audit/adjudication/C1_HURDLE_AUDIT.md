# C1 HURDLE AUDIT

## Trace of C1
- **Definition**: $C_1$ represents a base cost friction, defined as `0.061%` (6.1 basis points) per trade.
- **Calculation**: Used statically as `cost_friction=0.00061` inside `PortfolioEngine` instantiation in `phase3_walk_forward.py`.
- **Application**: Applied *after* gross returns are generated in the simulation to calculate net returns. Also used as a threshold to filter out trades (`net_return > 0` requires gross return > 6.1 bps).
- **Selection Bias**: It is a fixed hurdle. It does not dynamically adjust to observed test results.

## Classification
**A. Valid Methodological Constraint**. Binance UM Futures taker fees are 0.04% to 0.05% depending on VIP tier. A 0.061% total friction assumption per round trip (maker/taker blend + spread slippage) is a standard, albeit slightly optimistic, baseline hurdle. It is not an overfit parameter; it is a rigid execution assumption.

## Conclusion
**NOT AN ISSUE.** The C1 hurdle is a valid static baseline for execution costs. (Note: Whether $0.061\%$ is *realistic* for market orders in high volatility is an execution model risk, but it is not a *methodological data-snooping risk*).
