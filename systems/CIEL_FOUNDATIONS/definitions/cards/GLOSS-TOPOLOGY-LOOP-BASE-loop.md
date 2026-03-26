# Loop - Loop

| field | value |
|---|---|
| stable_id | `GLOSS-TOPOLOGY-LOOP-BASE` |
| canonical_id | `topology.loop.base` |
| card_type | `topology` |
| class | `topology` |
| subclass | `loop` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
closed trajectory carrying phase and memory

## Formal definition
```text
loop = closed trajectory under admissible closure
```

## Tags
`type:topology`, `domain:omega`, `status:canonical_record`, `role:closed`, `layer:runtime`, `bind:runtime`, `domain:foundations`, `math:topology`, `role:identity`, `role:memory`, `role:closure`

## Relational couplings
| relation | targets |
|---|---|
| `generates` | `memory` |
| `stabilizes` | `identity` |
| `binds_to` | `winding,phase` |

## Cross references
- `identity`
- `memory`
- `holonomy`
- `generates`
- `stabilizes`
- `binds_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.core.braid.loops
mode: module
```

## Notes
enables closure, memory, and topological classification
