# PHASE_COMPONENTS_DERIVATION_AND_OBSERVATION_CHECK

Status: canonical working note
Date: 2026-03-24

## Purpose
Promote the phase decomposition implemented in the orbital runtime into a canonical concept note and point to the measured report.

## Canonical decomposition
- local effective phase: `gamma_i^eff = phi_i + gamma_B,i`
- pair Berry phase: `Omega_ij = 1/2 (1-cos(theta_bar_ij)) Delta phi_ij`
- transport kernel: `A_ij = (w_ij T_ij) exp(i(beta Omega_ij - gamma d_ij))`
- closure contraction: `sum_j A_ij tau_j + A_iζ tau_ζ ≈ exp(i gamma_i^eff)`
- global defect: `Delta_H = sum_i a_i exp(i gamma_i^eff) + a_ζ exp(i gamma_ζ^eff)`
- coherence scalar: `R_H = |Delta_H|^2`

## Current measured report
See:
- `reports/phase_components/summary.md`
- `reports/phase_components/summary.json`
- `manifests/orbital/phase_components.json`

## Observation check
The current orbital run lands below the truthful means of the General and QA proxy phase benchmarks, while remaining far below the hallucinated regime. This should be interpreted as directional consistency, not as a direct observational measurement of the runtime phases.

## Cross references
- `systems/CIEL_FOUNDATIONS/derivations/D-0101-phase-components-from-aij-tau.md`
- `docs/concepts/TAU_AIJ_GLOBAL_IMPLEMENTATION.md`
- `docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md`
- `research/holonomic_observed_end_to_end/results/summary.json`
- `research/holonomy_closure_b1_b2/results.json`
