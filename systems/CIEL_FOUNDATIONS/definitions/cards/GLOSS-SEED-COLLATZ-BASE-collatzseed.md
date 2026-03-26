# CollatzSeed - CollatzSeed

| field | value |
|---|---|
| stable_id | `GLOSS-SEED-COLLATZ-BASE` |
| canonical_id | `seed.collatz.base` |
| card_type | `seed` |
| class | `seed` |
| subclass | `collatz` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
discrete trajectory seed for recursive phase evolution

## Formal definition
```text
T(n)=n/2 if even else 3n+1
```

## Tags
`type:seed`, `domain:omega`, `status:canonical_record`, `role:discrete`, `layer:runtime`, `bind:runtime`, `domain:metatime`

## Relational couplings
| relation | targets |
|---|---|
| `generates` | `trajectory` |
| `projects_to` | `closure,winding` |

## Cross references
- `trajectory`
- `winding_class`
- `generates`
- `projects_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.emotion.cqcl.emotional_collatz
object: EmotionalCollatzEngine
function: emotional_collatz_transform
mode: invoke
```

## Notes
generates recursive orbit classes under discrete dynamics
