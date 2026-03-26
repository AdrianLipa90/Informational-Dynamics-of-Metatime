# Omega_ij - BerryPairPhase

| field | value |
|---|---|
| stable_id | `GLOSS-OBSERVABLE-BERRY-PAIR-PHASE` |
| canonical_id | `observable.berry_pair_phase.omega_ij` |
| card_type | `observable` |
| class | `observable` |
| subclass | `loop_phase` |
| status | `working_definition` |
| certainty_scope | `runtime_backed_working_definition` |
| units | `radians` |
| value | `` |

## Description
Pairwise Berry phase used inside the argument of the transport kernel.

## Formal definition
```text
Omega_ij = 1/2 (1-cos(theta_bar_ij)) Delta phi_ij
```

## Tags
`type:observable`, `domain:omega`, `domain:foundations`, `status:working_definition`, `role:geometry`, `layer:runtime`, `bind:runtime`, `math:connection`, `math:berry`

## Relational couplings
| relation | targets |
|---|---|
| `projects_to` | `A_ij` |
| `measures` | `pair_geometry` |
| `couples_to` | `Phase` |

## Cross references
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-OPERATOR-TRANSPORT-AIJ-a_ij.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-PHASE-SCALAR-BASE-phase.md`
- `systems/CIEL_FOUNDATIONS/derivations/D-0101-phase-components-from-aij-tau.md`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py`
- `reports/phase_components/summary.md`

## Runtime binding
```yaml
module: ciel_omega.orbital.metrics
object: berry_pair_phase
mode: invoke
```
