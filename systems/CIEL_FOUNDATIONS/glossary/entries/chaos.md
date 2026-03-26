# Chaos

## Metadata
- ID: GLOSS-0001
- Serial number: 1
- Canonical file name: chaos.md
- Status: defined
- Glossary registry row: glossary/registry.csv#1

## Short definition
Chaos is the local measure of instability, branching, or admissible multiplicity of continuation from a state.

## Symbol
C

## Equation
C(x)=log(1+N_adm(x))

## Function / role
Provides the destabilizing / branching component of the primitive ontology.

## Derivation path
- Axiom(s): AX-0001-chaos
- Definition(s): primitive ontology
- Derivation(s): D-0001-primitive-ontology

## Code binding
- Module: src/ciel_foundations/primitives/chaos.py
- Function/Class: compute_chaos
- Tests: tests/symbolic/test_chaos.py

## Cross references
- axioms/AX-0001-chaos.md
- derivations/D-0001-primitive-ontology.md
- interfaces/state_interface.yaml

## Notes
Current equation is a minimal start and may be refined during raw re-derivation.
