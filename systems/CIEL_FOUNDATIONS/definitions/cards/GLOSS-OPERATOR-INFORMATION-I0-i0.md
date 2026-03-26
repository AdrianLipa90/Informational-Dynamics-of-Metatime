# I0 - I0

| field | value |
|---|---|
| stable_id | `GLOSS-OPERATOR-INFORMATION-I0` |
| canonical_id | `operator.information.i0` |
| card_type | `operator` |
| class | `operator` |
| subclass | `information` |
| status | `working_definition` |
| certainty_scope | `canonical_working_definition` |
| units | `dimensionless` |
| value | `ln(2)/(24*pi)` |

## Description
minimal information coupling

## Formal definition
```text
I0 = ln(2)/(24*pi)
```

## Tags
`type:operator`, `domain:omega`, `status:working_definition`, `role:minimal`, `layer:runtime`, `bind:runtime`, `domain:foundations`, `math:topology`, `role:information`, `role:closure`, `role:phase`

## Relational couplings
| relation | targets |
|---|---|
| `stabilizes` | `closure,identity` |
| `biases` | `attractor` |
| `couples_to` | `holonomy,trajectory` |

## Cross references
- `phase`
- `closure`
- `state`
- `memory`
- `stabilizes`
- `biases`
- `couples_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.fields.intention_field
object: IntentionField
field: I0
mode: read
```

## Notes
biases phase evolution toward low-defect closure
