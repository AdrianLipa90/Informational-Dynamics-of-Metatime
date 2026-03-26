# A_ij - TransportKernelAij

| field | value |
|---|---|
| stable_id | `GLOSS-OPERATOR-TRANSPORT-AIJ` |
| canonical_id | `operator.transport.a_ij` |
| card_type | `operator` |
| class | `operator` |
| subclass | `transport` |
| status | `working_definition` |
| certainty_scope | `runtime_backed_working_definition` |
| units | `dimensionless complex amplitude` |
| value | `` |

## Description
Complex transport operator between sectors. It carries tau-resonant amplitude and geometric phase.

## Formal definition
```text
A_ij = (w_ij T_ij) exp(i(beta Omega_ij - gamma d_ij))
T_ij = exp[-1/2 (log(tau_i/tau_j)/sigma)^2]
```

## Tags
`type:operator`, `domain:omega`, `domain:foundations`, `status:working_definition`, `role:transport`, `layer:runtime`, `bind:runtime`, `math:connection`, `math:spectrum`, `math:geometry`

## Relational couplings
| relation | targets |
|---|---|
| `depends_on` | `tau_i,tau_j` |
| `couples_to` | `Omega_ij,d_ij` |
| `projects_to` | `closure,TransportSpectrum` |

## Cross references
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-CONST-TAU-tau_i.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-OBSERVABLE-BERRY-PAIR-PHASE-omega_ij.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-STATE-EFFECTIVE-PHASE-gamma_eff_i.md`
- `systems/CIEL_FOUNDATIONS/derivations/D-0101-phase-components-from-aij-tau.md`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py`
- `reports/phase_components/summary.md`

## Runtime binding
```yaml
module: ciel_omega.orbital.metrics
object: A_ij
mode: invoke
```

## Notes
In the current canonical engine `A_ij` is the place where the tau branch is operationally promoted into transport.
