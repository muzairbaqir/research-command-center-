# AUDIT CHECKLIST: REPRODUCIBILITY & TRACEABILITY

Auditor: Claude (Red Team)

## Mandatory Verification Items

1. **Code & Commit Traceability**:
   * Verify git commit hash in execution repository matches exact state run.
   * Check for uncommitted working tree modifications.
2. **Environment & Dependency Pinning**:
   * Verify locked dependencies (requirements.txt / poetry.lock / pipfile.lock).
   * Verify Python runtime and CUDA/driver specs documented.
3. **Deterministic Seeds**:
   * Verify explicit pseudo-random seeds set for all stochastic processes.
4. **Data Input Immutability**:
   * Verify dataset version hash / checksum matches registered catalog.
