# Glossary build tools

This module builds the canonical glossary cards, machine-readable registry, semantic SQLite mirror, and statistics from the current repository source-of-truth files.

## Entry point
- `build_semantic_glossary.py`

## Inputs
- `systems/CIEL_FOUNDATIONS/axioms/registry.yaml`
- `systems/CIEL_FOUNDATIONS/constants/registry.yaml`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`
- `docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md`
- `research/holonomy_closure_b1_b2/results.json`
- `reports/global_orbital_coherence_pass/real_geometry.json`

## Outputs
- `systems/CIEL_FOUNDATIONS/definitions/cards/`
- `systems/CIEL_FOUNDATIONS/definitions/registry.yaml`
- `systems/CIEL_FOUNDATIONS/definitions/tables/`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary/generated/`
- `reports/glossary/`

## Rule
Generated artifacts are **derived**, not source of truth.
YAML, Markdown, code, and JSON source inputs remain authoritative.
