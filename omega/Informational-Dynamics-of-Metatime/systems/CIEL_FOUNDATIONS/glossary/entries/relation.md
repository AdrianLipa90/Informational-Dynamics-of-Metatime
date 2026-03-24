# Relation

## Metadata
- ID: GLOSS-0003
- Serial number: 3
- Canonical file name: relation.md
- Status: defined
- Glossary registry row: glossary/registry.csv#3

## Short definition
Relation is the amplitude-phase coupling operator between two states.

## Symbol
R_ij

## Equation
R_ij = w_ij exp(i phi_ij)

## Function / role
Turns chaos and potential into a co-describable joint state through phase-coherent coupling.

## Derivation path
- Axiom(s): AX-0003-relation
- Definition(s): primitive ontology
- Derivation(s): D-0001-primitive-ontology

## Code binding
- Module: src/ciel_foundations/primitives/relation.py
- Function/Class: compute_relation
- Tests: tests/symbolic/test_relation.py

## Cross references
- axioms/AX-0003-relation.md
- derivations/D-0001-primitive-ontology.md
- interfaces/state_interface.yaml

## Notes
This object will later link directly to holonomy and coupling structures.
