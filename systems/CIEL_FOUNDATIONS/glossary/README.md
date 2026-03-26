# Glossary

This directory is the canonical definition layer for named objects in the project.

It has two synchronized components:

1. `registry.csv` / `registry.yaml`
   - compact tabular register for fast scanning
   - one row per defined element

2. `entries/`
   - one detailed file per element
   - includes definition, symbol, equation, function, derivation path, and cross-references

## Required fields

Every glossary element should define:
- serial number
- file name / canonical ID
- display name
- symbol
- equation
- function / role
- derivation source
- status
- cross references

## Rule

Nothing should appear as a stable project object unless it has either:
- a glossary registry row
- or a glossary entry file
and ideally both.


## Canonical postulate linkage
- `../../../POSTULATES_CANON_PL_EN.md` - repo-level bilingual postulate canon
- `../axioms/AX-0100-canonical-relational-phase-postulates.md` - local foundations bridge
- `entries/canonical_postulates_relational_phase_formalism.md` - glossary entry for the canonical postulate set
