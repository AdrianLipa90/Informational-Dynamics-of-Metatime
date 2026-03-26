# Tau Modes

## Metadata
- ID: GLOSS-0005
- Serial number: 5
- Canonical file name: tau_modes.md
- Status: derived
- Glossary registry row: glossary/registry.csv#5

## Short definition
Tau modes are the spectral / transport coordinates that weight both the kernel amplitude and the closure contraction in the orbital engine.

## Symbol
`tau_i`

## Equation
`A_ij=(w_ij*T_ij) exp(i(beta Omega_ij-gamma d_ij)) ; sum_j A_ij tau_j ~ exp(i gamma_i^eff)`

## Function / role
They determine which sector pairs resonate strongly and how the closure equation is weighted.

## Derivation path
- Derivation(s): D-0101-phase-components-from-aij-tau

## Code binding
- Module: systems/CIEL_FOUNDATIONS/constants/tau/code.py
- Function/Class: CANONICAL_ORBITAL_TAU_TRIAD, tau_transport_factor

## Cross references
- constants/tau/derivation.md
- derivations/D-0101-phase-components-from-aij-tau.md
- ../../../systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py
