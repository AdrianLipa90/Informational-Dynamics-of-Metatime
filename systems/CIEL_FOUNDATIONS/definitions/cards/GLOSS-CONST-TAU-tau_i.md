# tau_i - Spectral Time Coordinates

| field | value |
|---|---|
| stable_id | `GLOSS-CONST-TAU` |
| canonical_id | `constant.tau_i` |
| card_type | `constant` |
| class | `constant` |
| subclass | `` |
| status | `working_definition` |
| certainty_scope | `runtime-backed_working_definition` |
| units | `dimensionless` |
| value | `orbital triad + historical neutrino-seed branch` |

## Description
Transport / spectral coordinates that weight the orbital transport kernel and its closure contraction.

## Formal definition
```text
orbital branch: tau = (0.263, 0.353, 0.489)
A_ij = (w_ij T_ij) exp(i(beta Omega_ij - gamma d_ij))
sum_j A_ij tau_j + A_iζ tau_ζ ≈ exp(i gamma_i^eff)
```

## Tags
`type:constant`, `domain:foundations`, `domain:metatime`, `domain:omega`, `status:working_definition`, `role:spectrum`, `role:transport`, `layer:foundations`, `bind:runtime`, `math:spectrum`, `math:transport`, `sector:neutrino`

## Relational couplings
| relation | targets |
|---|---|
| `couples_to` | `A_ij` |
| `projects_to` | `TransportSpectrum` |
| `stabilizes` | `closure` |

## Cross references
- `systems/CIEL_FOUNDATIONS/constants/tau/`
- `systems/CIEL_FOUNDATIONS/derivations/D-0101-phase-components-from-aij-tau.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-OPERATOR-TRANSPORT-AIJ-a_ij.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-STATE-EFFECTIVE-PHASE-gamma_eff_i.md`

## Source-of-truth anchors
- `systems/CIEL_FOUNDATIONS/constants/registry.yaml`
- `systems/CIEL_FOUNDATIONS/constants/tau/README.md`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py`

## Notes
The repo still contains at least two tau branches. The current runtime uses the orbital / relational triad. The neutrino seed branch should be preserved as provenance, not silently merged.
