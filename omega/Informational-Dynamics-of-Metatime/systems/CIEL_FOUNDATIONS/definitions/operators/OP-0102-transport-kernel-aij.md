# OP-0102 — Transport Kernel A_ij

## Role
Derived bridge operator connecting sector couplings, Berry geometry, and distance penalties.

## Formal anchor
- `../derivations/D-0101-phase-components-from-aij-tau.md`

## Current form
`A_ij = (w_ij T_ij) exp(i(beta Omega_ij - gamma d_ij))`

## Implementation anchor
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py`

## Tests
- `systems/CIEL_FOUNDATIONS/tests/numeric/test_tau_phase_components.py`

## Status
`derived_bridge`
