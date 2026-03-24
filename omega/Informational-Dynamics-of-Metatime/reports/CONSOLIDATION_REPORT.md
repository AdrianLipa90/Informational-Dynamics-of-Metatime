# Consolidation report

## Scope
This bundle consolidates all uploaded archives, extracted project trees, PDFs, and generated research packages into one auditable folder.

## Canonical selection
**Chosen runtime source of truth for executable code:** `systems/CIEL_OMEGA_COMPLETE_SYSTEM`

### Why this tree was chosen
- It is the broadest integrated runtime among the uploaded archives.
- It contains `bridge/`, `constraints/`, `memory/`, `vocabulary/`, `runtime/`, `cognition/`, `fields/`, and demos in one place.
- In this environment, `pytest -q` completed successfully.
- Key demos executed successfully.

### Reference trees retained
- `systems/CIEL_OMEGA_MEMORY_REFERENCE_v3.1.7`
- `systems/CIEL_OMEGA_VOCABULARY_REFERENCE`
- `systems/CIEL_FOUNDATIONS`

These were kept as lineage/reference material, not as the primary executable tree.

## What was unpacked and sorted
- All incoming `.tar.gz` and `.zip` archives were copied to `incoming_archives/`.
- All PDF documents were collected into `docs/pdfs/`.
- The runtime, foundations scaffold, memory lineage, vocabulary lineage, synthetic holonomic package, observed-data holonomic package, and observed datasets were placed into dedicated top-level folders.
- `__pycache__`, `.pytest_cache`, and `.pyc` files were removed from the consolidated tree.

## Code linkage findings
The uploaded codebases are linkable at the symbol and subsystem level.

### Confirmed bindings
- `operator.information.i0` -> `ciel_omega.fields.intention_field`
- `constraint.euler` -> `ciel_omega.constraints.euler_constraint`
- `channel.holonomy.white_threads` -> `ciel_omega.bridge.memory_core_phase_bridge`

This means the runtime already contains explicit symbolic hooks for the Information Operator, Euler closure machinery, and white-thread amplitude handling.

## Tests and execution
### Runtime tests
- `pytest -q` result: **58 passed**, **46 warnings**
- The warnings are dominated by tests returning values instead of asserting, plus one timestep warning.

### Runtime demos executed successfully
- `demo_unified_euler.py`
- `demo_vocabulary_resolve.py`
- `demo_ciel_omega_complete.py`

Logs are stored in `logs/`.

### Compile checks
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM`: `python -m compileall -q ciel_omega` -> no logged errors
- `systems/CIEL_FOUNDATIONS`: `python -m compileall -q .` -> no logged errors

## Research package results
### Synthetic holonomic package
Path: `research/holonomic_relations_research_grade`

Key result snapshot:
- low-distortion mean final `H`: 8.8408
- high-distortion mean final `H`: 8.8396
- note from package: synthetic validation only

Interpretation:
- the package runs and generates artifacts,
- but in its current parametrization the final `H` separation between low/high distortion is weak,
- so this package should be treated as executable scaffolding, not strong discriminative evidence.

### Observed-data end-to-end package
Path: `research/holonomic_observed_end_to_end`

Observed benchmark summary:
- General: non-hallucinated mean `H` = 0.2187, hallucinated mean `H` = 2.1289
- QA: truthful mean `H` = 0.2540, hallucinated mean `H` = 2.2189
- Summarization: truthful mean `H` = 0.0077, hallucinated mean `H` = 2.7827

Interpretation:
- under the proxy phase encoding used in that package, hallucinated cases show substantially larger `H` than truthful/non-hallucinated cases,
- this is directionally consistent with the intended observable behavior,
- but it remains a proxy-observable pipeline rather than direct phase measurement.

## File-comparison summary
See `manifests/comparison_summary.json`.

High-level outcome:
- `CIEL_OMEGA_COMPLETE_SYSTEM_WITH_README` dominates the other runtime tarballs in breadth and integration.
- The memory sector from `v3.1.7` is already contained in the canonical runtime for all overlapping source files checked.
- The standalone vocabulary package is mostly contained in the canonical runtime; the main difference observed was a cleaner orchestrator import structure in the canonical runtime.

## Limits of this consolidation
- I did not semantically validate every one of the 244 Python files line by line.
- The PDFs were archived and grouped, but not rewritten into the runtime.
- The observed-data and synthetic holonomic packages remain separate research packages; they were not fused into the runtime codebase.
- No claim is made here that the physics-level interpretations are empirically verified.

## Recommended next step
If the goal is a single operational repo, the next highest-value move is:
1. promote `systems/CIEL_FOUNDATIONS` to the formal source-of-truth layer,
2. keep `systems/CIEL_OMEGA_COMPLETE_SYSTEM` as runtime/inference layer,
3. move the holonomic packages behind a shared `research/` interface with one launcher script.
