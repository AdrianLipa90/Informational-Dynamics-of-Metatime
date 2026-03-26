# Coherence - Coherence

| field | value |
|---|---|
| stable_id | `GLOSS-STATE-COHERENCE-BASE` |
| canonical_id | `state.coherence.base` |
| card_type | `state` |
| class | `state` |
| subclass | `coherence` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
degree of alignment or low-defect closure

## Formal definition
```text
C ~ 1 - normalized_closure_defect
```

## Tags
`type:state`, `domain:omega`, `status:canonical_record`, `role:degree`, `layer:runtime`, `bind:registry`, `math:topology`, `role:coherence`

## Relational couplings
| relation | targets |
|---|---|
| `measures` | `closure` |
| `stabilizes` | `decision` |

## Cross references
- `decision`
- `report`
- `memory`
- `measures`
- `stabilizes`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.constraints.euler_constraint
function: closure_score
mode: deferred
```

## Notes
rises when phase ensemble approaches admissible closure
