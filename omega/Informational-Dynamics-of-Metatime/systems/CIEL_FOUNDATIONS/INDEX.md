# CIEL Foundations Index

This index is the canonical navigation layer for the foundations subtree.
It answers four questions for every object:

1. where it is defined,
2. where it is derived,
3. where it is implemented,
4. where it is tested or falsified.

## Canonical navigation

### Ontology and axioms
- `axioms/registry.yaml` — frozen axiom inventory.
- `axioms/AX-0100-canonical-relational-phase-postulates.md` — bilingual bridge from repo canon into foundations.
- `postulates/POSTULATES_CANON_PL_EN.md` — local postulate anchor.

### Definitions and glossary
- `definitions/registry.yaml` — canonical card registry.
- `definitions/cards/` — one stable object per card.
- `definitions/operators/` — operator-level summaries and implementation anchors.
- `definitions/spaces/` — state-space and geometry summaries.
- `definitions/constants/` — constant-level canonical summaries.
- `glossary/registry.yaml` — compact searchable glossary table.

### Derivations and code bindings
- `derivations/code_map.yaml` — formal object to code/test/artifact map.
- `derivations/D-0101-phase-components-from-aij-tau.md` — current promoted numeric derivation.
- `verification/diff_registry.yaml` — reconciliation log between canon, raw inputs, and promoted artifacts.

### Constants, sectors, and export surface
- `constants/registry.yaml` — canonical constant inventory.
- `sectors/SECTOR_INDEX.md` — sector inheritance map.
- `interfaces/` — import/export contracts.
- `whitepapers/` — publication-grade explanatory layer.

### Tests, falsification, provenance
- `tests/` — numeric, regression, symbolic, and falsification-facing tests.
- `falsification/matrix.yaml` — explicit failure targets.
- `provenance/lineage.yaml` — lineage and artifact ancestry.
- `artifacts/registry.yaml` — generated artifact registry.

## Review discipline
A formal object should not be considered stabilized unless it can be traced across:

`axiom/postulate -> definition -> derivation -> code -> test -> artifact/report`

## Current priority gaps closed in this pass
- populated `definitions/operators/`, `definitions/spaces/`, and `definitions/constants/`
- expanded `derivations/code_map.yaml`
- filled `verification/diff_registry.yaml`
- added sector-level organization and LaTeX section anchors
