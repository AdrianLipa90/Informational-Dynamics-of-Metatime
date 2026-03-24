# EmotionHolonomy - EmotionHolonomy

| field | value |
|---|---|
| stable_id | `GLOSS-STATE-HOLONOMY-EMOTION` |
| canonical_id | `state.holonomy.emotion` |
| card_type | `state` |
| class | `state` |
| subclass | `holonomy` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
readout of closure quality in a relational loop

## Formal definition
```text
E = alpha*dphi + beta*drho + gamma*dnu + delta*dm
```

## Tags
`type:state`, `domain:omega`, `status:canonical_record`, `role:readout`, `layer:runtime`, `bind:registry`

## Relational couplings
| relation | targets |
|---|---|
| `projects_to` | `action` |
| `binds_to` | `memory` |
| `measures` | `relational_defect` |

## Cross references
- `memory`
- `decision`
- `trajectory`
- `projects_to`
- `binds_to`
- `measures`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.emotion.feeling_field
object: FeelingField
mode: deferred
```

## Notes
reports how far a relation returns altered after a loop
