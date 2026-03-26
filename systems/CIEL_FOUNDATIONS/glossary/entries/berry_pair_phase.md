# Berry Pair Phase

## Metadata
- ID: GLOSS-0007
- Serial number: 7
- Canonical file name: berry_pair_phase.md
- Status: defined
- Glossary registry row: glossary/registry.csv#7

## Short definition
The Berry pair phase Omega_ij is the pairwise geometric contribution inserted into the phase of A_ij.

## Symbol
`Omega_ij`

## Equation
`Omega_ij = 1/2 (1-cos(theta_bar_ij)) Delta phi_ij`

## Function / role
It encodes projective transport on the Bloch sphere and competes with the hyperbolic distance term.

## Derivation path
- Derivation(s): D-0101-phase-components-from-aij-tau

## Code binding
- Module: systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py
- Function/Class: berry_pair_phase

## Cross references
- derivations/D-0101-phase-components-from-aij-tau.md
- reports/phase_components/summary.md
