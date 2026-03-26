# P0 Canonical Integrity Audit — 2026-03-24

## Scope
- Whole repo: `repo/`
- Canonical runtime under audit: `systems/CIEL_OMEGA_COMPLETE_SYSTEM`

## Verified execution state
- `pytest -q`: **58 passed**
- `compileall`: **passed**
- unified smoke run: **passed**
- observed smoke `closure_score`: **0.9106189238797913**

## Main findings

### 1. The canonical runtime is executable
The runtime still compiles, tests pass, and `UnifiedSystem.create(...).run_text_cycle(...)` works in the current environment.

### 2. Volatile residue was present and was cleaned
During this audit, validation recreated cache artifacts inside the repo.

**Dirty state observed after compile/test checks**
- repo `__pycache__` dirs: **44**
- repo `.pyc` files: **279**
- repo `.pytest_cache` dirs: **1**
- runtime file count in dirty state: **590**

**Clean state after volatile cleanup**
- repo `__pycache__` dirs: **0**
- repo `.pyc` files: **0**
- repo `.pytest_cache` dirs: **0**
- runtime clean file count: **307**
- runtime clean dir count: **58**
- runtime clean fingerprint: `a22695ee353f12ddc49d2c63a44f2159a31b36d9cd02b7a3eb8d0dc8b7fb151e`

### 3. The canonical build manifest is inconsistent with the actual runtime tree
`systems/CIEL_OMEGA_COMPLETE_SYSTEM/CANONICAL_BUILD_MANIFEST.md` declares:

- file count: **539**
- fingerprint: `736a1576d7186517826581d9c7e4c88846bb397d835e763f21b3a69e5ad012f1`

Actual clean runtime on disk:

- file count: **307**
- fingerprint: `a22695ee353f12ddc49d2c63a44f2159a31b36d9cd02b7a3eb8d0dc8b7fb151e`

This is a real mismatch.

### 4. The old “244 Python files” statement still aligns if TODO material is excluded
When excluding paths containing `TODO/` from the runtime tree:

- files: **281**
- Python files: **244**
- fingerprint: `bf208bf700b3662f8c370a008912e89b089e42852da7f4ad93ba2c9bf1fc74c7`

This means the old py-file count is still explainable, but the manifest file count/fingerprint are not.

### 5. Nonvolatile memory artifacts still need policy
Three committed ledger DBs are present, and two copies live inside/around the canonical runtime:

- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db`
- `systems/RECOVERED_ARCHIVAL_SYSTEMS/.../memory_ledger.db`

Important asymmetry:
- top-level `CIEL_MEMORY_SYSTEM/` contains `WPM/wave_snapshots/wave_archive.h5`
- nested `ciel_omega/CIEL_MEMORY_SYSTEM/` does **not**

So the duplicated memory trees are not identical.

## Audit conclusion
P0 confirms three things simultaneously:

1. The runtime is **alive and executable**.
2. The canonical tree is **not fully hygienic by default** after validation unless cleanup is enforced.
3. The declared canonical manifest is **not synchronized** with the clean runtime currently on disk.

## Required next actions before P1
1. Regenerate or rewrite `CANONICAL_BUILD_MANIFEST.md`.
2. Formalize policy for:
   - committed DB ledgers,
   - duplicated `CIEL_MEMORY_SYSTEM` trees,
   - `TODO/` material inside runtime.
3. Keep validation outputs outside the canonical tree or auto-clean them after checks.

## Artifacts written by this audit
- `reports/audit/P0_CANONICAL_INTEGRITY_AUDIT_2026-03-24.md`
- `reports/audit/p0_canonical_integrity_summary.json`
- `reports/audit/p0_db_artifacts.tsv`
- `reports/audit/p0_extless_files.tsv`
