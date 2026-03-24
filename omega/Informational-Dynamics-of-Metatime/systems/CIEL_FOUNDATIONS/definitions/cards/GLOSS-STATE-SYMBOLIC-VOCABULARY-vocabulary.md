# Vocabulary - Vocabulary

| field | value |
|---|---|
| stable_id | `GLOSS-STATE-SYMBOLIC-VOCABULARY` |
| canonical_id | `state.symbolic.vocabulary` |
| card_type | `formalism` |
| class | `state` |
| subclass | `memory_trace` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
ontological transition table between symbol, formalism, and runtime

## Formal definition
```text
V(symbol)=binding
```

## Tags
`type:formalism`, `domain:omega`, `status:canonical_record`, `role:ontological`, `layer:runtime`, `bind:registry`

## Relational couplings
| relation | targets |
|---|---|
| `binds_to` | `CQCL,runtime,memory` |
| `stabilizes` | `meaning` |

## Cross references
- `CQCL`
- `resolver`
- `state`
- `binds_to`
- `stabilizes`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.vocabulary
field: canonical_vocabulary
mode: deferred
```

## Notes
stabilizes meaning across compilation and execution
