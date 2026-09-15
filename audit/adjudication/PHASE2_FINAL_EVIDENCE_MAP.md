# PHASE 2 FINAL EVIDENCE MAP

### 1. Trailing Stop Path Dependence
**CLAIM**: The execution model evaluates intra-candle trailing stops optimistically due to lack of tick resolution.
↓
**SOURCE FILE**: `src/engine/youtube_master_scalper.py`
↓
**FUNCTION / CLASS**: Signal trailing blocks (`take_profit = ...`)
↓
**LINE RANGE**: ~L381 - L476
↓
**OBSERVED BEHAVIOR**: Takes profit logic is computed against 1-minute `close` or `high` boundaries. If both TP and SL are hit in the same 1-minute `High-Low` range, the code executes sequentially (TP checks often precede SL checks).
↓
**METHODOLOGICAL CONSEQUENCE**: Generates artificial wins. If Open=100, High=110(TP), Low=90(SL). Path O->H->L results in a win. Path O->L->H results in a loss. Standard OHLC data cannot resolve this, creating optimistic execution bias.
↓
**SEVERITY**: CRITICAL

### 2. Multiple Testing Degradation
**CLAIM**: Reusing the 2021-2024 test sets across Phase 1 through Phase 5 degrades statistical confidence.
↓
**SOURCE FILE**: `src/validation/phase3_walk_forward.py`
↓
**FUNCTION / CLASS**: `run_walk_forward_validation`
↓
**LINE RANGE**: L30 - L90
↓
**OBSERVED BEHAVIOR**: The expanding walk-forward uses the exact same `[2022, 2023, 2024]` test folds. Re-running the baseline across 5 project phases implicitly optimizes for this exact test set.
↓
**METHODOLOGICAL CONSEQUENCE**: Reduces the true out-of-sample validity of the Phase 5 baseline Sharpe ratio.
↓
**SEVERITY**: MEDIUM

### 3. Volatility Barrier Divergence
**CLAIM**: The Volatility filter is diagnostic and not actively enforced in the backtest.
↓
**SOURCE FILE**: `experiments/phase5_cost_aware_engine.py`
↓
**FUNCTION / CLASS**: `run_phase5a_diagnostics`
↓
**LINE RANGE**: L120
↓
**OBSERVED BEHAVIOR**: `filter_mask = vol_2023 > threshold_move` is applied to already-computed `df_2023` outputs, rather than inside `PortfolioEngine` entry logic.
↓
**METHODOLOGICAL CONSEQUENCE**: Live production logic expecting to avoid low-volatility regimes will diverge from the backtested baseline, which included those trades. This is a LIVE/PRODUCTION DIVERGENCE, not a research leakage issue.
↓
**SEVERITY**: MEDIUM

### 4. Static C1 Hurdle
**CLAIM**: The $0.061\%$ execution cost is a static assumption.
↓
**SOURCE FILE**: `src/validation/phase3_walk_forward.py`
↓
**FUNCTION / CLASS**: `PortfolioEngine`
↓
**LINE RANGE**: L86
↓
**OBSERVED BEHAVIOR**: `cost_friction=0.00061`
↓
**METHODOLOGICAL CONSEQUENCE**: It is a VALID PRE-SPECIFIED ASSUMPTION. It does not cause data snooping or leakage. However, it may be an *unrealistic* assumption during high volatility, causing the expected edge to be overstated.
↓
**SEVERITY**: LOW
