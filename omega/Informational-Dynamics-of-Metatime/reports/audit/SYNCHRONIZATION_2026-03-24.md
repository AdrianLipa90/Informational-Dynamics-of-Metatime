# Synchronization report — 2026-03-24

## Canonical base
- Base snapshot: `CIEL_REPO_B1_B2_REGISTRY_UPDATE_2026-03-24.zip`

## Selective merges performed
1. Imported human glossary source and bibliography seeds from `CIEL_REPO_WITH_GLOSSARY_2026-03-24.zip`.
2. Imported glossary build tooling and richer ontology vocabulary from `CIEL_REPO_GLOSSARY_CARDS_STATS_2026-03-24.zip`.
3. Added missing `systems/CIEL_FOUNDATIONS/glossary/` and `systems/CIEL_FOUNDATIONS/verification/` layers from `CIEL_FOUNDATIONS_SCAFFOLD_V5.tar.gz`.
4. Mapped HTRI simulation artifacts into canonical `research/orbital_geodynamics_v3..v5/results/`.
5. Preserved `ciel_rh_control_mini_repo` as an external source and distilled its core threshold logic into `ciel_omega/orbital/rh_control.py`.
6. Parked `metatron_kernel.py` as an external intake artifact.
7. Parked `origins_planetary_biology_app` as a clean external intake artifact.

## Runtime assets intentionally not embedded
- `qwen2.5-0.5b-instruct-q2_k.gguf`
- `llama-b8149-bin-linux-avx-x64.tar.gz`

These remain external runtime assets and were not copied into the canonical repository tree.

## Validation
- Rebuilt glossary artifacts after merge.
- `pytest -q systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/test_orbital_rh_control.py` → `2 passed`.

## Counts
- Added paths: 136
- Modified paths: 4

## Notes
- `CIEL_LAST_COPIES_MERGED_with_omega_dna_module.zip` was not re-promoted into canon during this sync.
  It remains a historical branch source rather than the active source of truth.
- Build caches were removed after validation (`__pycache__`, `*.pyc`).
