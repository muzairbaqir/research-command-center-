# AUDIT CHECKLIST: EXECUTION REALISM & FRICTION

Auditor: Claude (Red Team)

## Mandatory Verification Items

1. **Transaction Fees**:
   * Verify exchange fee schedule applied matches historical tier (maker/taker).
2. **Spread Crossing**:
   * Verify bid-ask spread crossing cost was applied for aggressive orders.
3. **Slippage & Market Impact**:
   * Confirm slippage model accounts for trade size vs. top-of-book depth.
4. **Latency Modeling**:
   * Confirm realistic latency delay between signal generation and order fill at matching engine.
5. **Fill Feasibility**:
   * For passive limit orders, verify queue priority was modeled and trade volume at level was sufficient.
