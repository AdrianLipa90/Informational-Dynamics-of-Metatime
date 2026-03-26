# DEBUG_RUN_REPORT

## Summary
- pytest: 58 passed
- warnings: 0
- global orbital coherence pass: operational

## Fixes applied
1. Replaced pytest test functions that incorrectly returned values with explicit `assert` statements.
2. Preserved script-style `main()` runners by adding `_run_test()` helpers where needed.
3. Updated the large-`dt` grid stability test to capture and validate the expected substepping warning instead of leaking it into pytest output.
4. Relaxed the vocabulary integration assertion for `ethical_ok` to accept both `bool` and `numpy.bool_`.

## Files touched
- `ciel_omega/TODO/vocabulary/test_comprehensive.py`
- `ciel_omega/vocabulary/test_comprehensive.py`
- `ciel_omega/test_alignment_strengthening.py`
- `ciel_omega/test_grid_stability.py`
- `ciel_omega/test_defect_minimization.py`
- `ciel_omega/test_affective_memory.py`
- `ciel_omega/test_affective_memory_consolidation.py`
- `ciel_omega/test_m6_1_acceptance.py`
- `ciel_omega/test_perceptual_memory.py`
- `ciel_omega/test_perceptual_memory_consolidation.py`
- `ciel_omega/test_procedural_memory.py`
- `ciel_omega/test_procedural_memory_consolidation.py`
- `ciel_omega/test_semantic_memory.py`
- `ciel_omega/test_semantic_memory_consolidation.py`
- `ciel_omega/test_working_memory.py`
- `ciel_omega/test_working_memory_consolidation.py`

Archived from source path: `omega/Informational-Dynamics-of-Metatime/reports/debug/DEBUG_RUN_REPORT.md`
