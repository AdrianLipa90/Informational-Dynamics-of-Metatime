# Lambda0 - Lambda0

| field | value |
|---|---|
| stable_id | `GLOSS-OPERATOR-LAMBDA-LAMBDA0` |
| canonical_id | `operator.lambda.lambda0` |
| card_type | `operator` |
| class | `operator` |
| subclass | `lambda` |
| status | `hypothesis` |
| certainty_scope | `registry_working_hypothesis` |
| units | `dimensionless` |
| value | `` |

## Description
global expansion or emergence operator

## Formal definition
```text
Lambda0 ~ global phase-curvature operator
```

## Tags
`type:operator`, `domain:omega`, `status:hypothesis`, `role:global`, `layer:runtime`, `bind:runtime`, `domain:foundations`, `math:topology`, `sector:cosmology`, `role:curvature`

## Relational couplings
| relation | targets |
|---|---|
| `stabilizes` | `cosmological_attractor` |
| `couples_to` | `I0,resonance` |

## Cross references
- `state`
- `cosmological`
- `phase`
- `stabilizes`
- `couples_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.core.physics.ciel0_framework
object: CIEL0Core
field: Lambda0
mode: read
```

## Notes
modulates global phase curvature and expansion bias
