# Holonomy Defect

## Metadata
- ID: GLOSS-0009
- Serial number: 9
- Canonical file name: holonomy_defect.md
- Status: defined
- Glossary registry row: glossary/registry.csv#9

## Short definition
The holonomy defect is the global complex mismatch left after summing the weighted effective phases of all sectors and the zeta pole.

## Symbol
`Delta_H`

## Equation
`Delta_H=sum_i a_i exp(i gamma_i^eff)+a_zeta exp(i gamma_zeta^eff)`

## Function / role
Its norm defines the repo-level coherence observable `R_H=|Delta_H|^2`.

## Derivation path
- Derivation(s): D-0101-phase-components-from-aij-tau

## Code binding
- Module: systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py
- Function/Class: holonomy_defect, global_coherence

## Cross references
- derivations/D-0101-phase-components-from-aij-tau.md
- reports/phase_components/summary.md
