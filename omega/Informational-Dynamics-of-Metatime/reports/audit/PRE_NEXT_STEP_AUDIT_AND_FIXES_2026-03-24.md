# Pre-next-step audit and fixes — 2026-03-24

## Validation
- `python -m compileall -q ciel_omega` — passed.
- `pytest -q` — ..........................................................               [100%]
58 passed in 3.12s.
- Package-mode smoke (`from ciel_omega.unified_system import UnifiedSystem`) — passed with `closure_score = 0.910618923880` and `memory_cycle_index = 1`.
- Package-internal `WPM/wave_archive.h5` recreation after path fix: **False**.
- Direct script-style import of `unified_system.py` from inside the package directory is not a supported execution mode because the module uses relative imports; package-root import works correctly.

## Canonical integrity
- Manifest synchronized: **True**.
- Whole-system payload: `307` files, fingerprint `874926cee90af09544e09bca4a05432189bccb2e8f3161049b67fc09cbc76cee`.
- Code+docs payload: `304` files, fingerprint `9e9ed93e7d701afe0cee0d632799a51abe720fefe4a9e2e5a040d2b3fcc3c91c`.
- `ciel_omega/` subtree: `298` files, fingerprint `98061d0ecd22860fc2ab31fd4c01ffa26141d88256a56cfc90346e3f2291fe0a`.

## Data layer findings
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db` — size `12288`, sha256 `a34926b730016cc6b0b897680421127d51d65b3021a6dba079f0d368b37c2700`.
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/CIEL_MEMORY_SYSTEM/TSM/ledger/memory_ledger.db` — size `12288`, sha256 `1131d054a13e88f00911c71c1e48f33727ca3f0f7d93f6516cb9ea11e97bdfb9`.
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/CIEL_MEMORY_SYSTEM/WPM/wave_snapshots/wave_archive.h5` — size `1832`, sha256 `7859c8aaf311c22e68f5c754b1a0bf31f26c1fcba902da4710d48f46446e8ea8`.
- Top-level runtime data layer and package-embedded ledger mirror still coexist. The two `memory_ledger.db` files are not identical.
- The accidental package-internal WPM archive generated during earlier smoke validation was removed, and the default path logic was fixed so new writes target the system-root data layer.

## Crossrefs / Bloch map / registries / derivations
- Matched artifacts by name pattern: `27` files.
- Present canonical examples include:
  - `NONLOCAL_REPO_HYPERSPACE/maps/semantic_bloch_localization.yaml`
  - `NONLOCAL_REPO_HYPERSPACE/registry.yaml`
  - `systems/CIEL_FOUNDATIONS/Simulations/registry.yaml`
  - `systems/CIEL_FOUNDATIONS/artifacts/registry.yaml`
  - `systems/CIEL_FOUNDATIONS/assumptions/registry.yaml`
  - `systems/CIEL_FOUNDATIONS/axioms/registry.yaml`
  - `systems/CIEL_FOUNDATIONS/benchmarks/registry.yaml`
  - `systems/CIEL_FOUNDATIONS/constants/I0/derivation.md`
  - `systems/CIEL_FOUNDATIONS/constants/Lambda0/derivation.md`
  - `systems/CIEL_FOUNDATIONS/constants/kappa/derivation.md`
  - `systems/CIEL_FOUNDATIONS/constants/registry.yaml`
  - `systems/CIEL_FOUNDATIONS/constants/tau/derivation.md`
- **No active runtime Python module was found that writes Bloch/crossref artifacts automatically.** Current Bloch/crossref state appears to be registry/document driven, not runtime-generated.

## Fixes applied
- resolved SyntaxWarning by converting compute_gradient docstring to raw string in TODO/loose_from_old/relational_contract.py.
- anchored monolith memory default paths to the system root in memory/monolith/orchestrator.py.
- anchored monolith CLI data/config paths to the system root in memory/monolith/cli.py.
- anchored legacy unified_memory defaults and backup/export paths to the system root in memory/monolith/unified_memory.py.
- removed package-internal WPM wave_archive.h5 generated during prior smoke run.
- re-synchronized CANONICAL_BUILD_MANIFEST.md after code/path fixes.

## Residue before cleanup
- `__pycache__` dirs: `44`
- `.pyc` files: `279`
- `.pytest_cache` dirs: `1`
- These are validation byproducts and will be removed before snapshotting.

## Conclusion
- The reconsolidated repo is executable, test-clean, and its canonical manifest is synchronized.
- The main unresolved issue before later architectural work is not build failure but **data-layer duplication** and the lack of a canonical runtime-generated Bloch crossref artifact.
