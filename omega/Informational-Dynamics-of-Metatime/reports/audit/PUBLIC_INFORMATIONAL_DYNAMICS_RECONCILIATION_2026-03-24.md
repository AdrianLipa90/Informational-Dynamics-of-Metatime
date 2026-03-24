# Public Informational-Dynamics-of-Metatime Reconciliation — 2026-03-24

## Goal
Bring the local canonical repo into high-fidelity alignment with the public `AdrianLipa90/Informational-Dynamics-of-Metatime` repository **only for value-bearing missing artifacts**, without duplicating already unpacked runtime payloads.

## Added / restored
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/configs/heuristics_self.json`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/configs/heuristics_user.json`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/configs/rules_immutable.json`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/configs/relational_contract.yaml`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/configs/relational_contract.py`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/LICENSE`
- mirrored `relational_contract.yaml` and `relational_contract.py` into `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/configs/`
- config registry and README for the restored public config layer

## Intentionally not promoted
- `CIEL_OMEGA_COMPLETE_SYSTEM_WITH_README.tar.gz`
  - reason: already represented by unpacked canonical runtime tree; importing the tarball would duplicate packaging but add no new runtime, documentation, or derivational value.
- `Logo1.png`
  - reason: branding artifact only; not required for runtime, derivation, registry, or reproducibility.

## Structural result
The local repo now preserves both:
1. the unpacked canonical runtime tree under `systems/CIEL_OMEGA_COMPLETE_SYSTEM/`, and
2. the top-level public config/license packaging semantics that were missing from canonical position.

## Validation expectation
- `relational_contract.py` resolves its YAML relative to its own file path by default, avoiding import-time breakage from working-directory changes.
