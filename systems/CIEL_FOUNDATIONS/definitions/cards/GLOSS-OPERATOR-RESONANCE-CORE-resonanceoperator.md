# ResonanceOperator - ResonanceOperator

| field | value |
|---|---|
| stable_id | `GLOSS-OPERATOR-RESONANCE-CORE` |
| canonical_id | `operator.resonance.core` |
| card_type | `operator` |
| class | `operator` |
| subclass | `resonance` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
measures or enforces state-intention coherence

## Formal definition
```text
R(S,I)=|<S|I>|^2
```

## Tags
`type:operator`, `domain:omega`, `status:canonical_record`, `role:measures`, `layer:runtime`, `bind:runtime`

## Relational couplings
| relation | targets |
|---|---|
| `measures` | `coherence` |
| `stabilizes` | `aligned_state` |
| `projects_to` | `action` |

## Cross references
- `coherence`
- `decision`
- `state`
- `measures`
- `stabilizes`
- `projects_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.resonance.resonance_operator
object: ResonanceOperator
mode: invoke
```

## Notes
amplifies coherent channels, suppresses mismatch
