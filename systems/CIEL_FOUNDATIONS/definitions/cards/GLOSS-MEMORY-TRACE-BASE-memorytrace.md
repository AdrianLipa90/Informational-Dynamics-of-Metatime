# MemoryTrace - MemoryTrace

| field | value |
|---|---|
| stable_id | `GLOSS-MEMORY-TRACE-BASE` |
| canonical_id | `memory.trace.base` |
| card_type | `memory` |
| class | `memory` |
| subclass | `memory_trace` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
persistent residual left by completed or incomplete loops

## Formal definition
```text
M = residual(loop_history)
```

## Tags
`type:memory`, `domain:omega`, `status:canonical_record`, `role:persistent`, `layer:runtime`, `bind:registry`, `math:topology`, `sector:memory`, `role:memory`

## Relational couplings
| relation | targets |
|---|---|
| `remembers` | `trajectory,closure,emotion` |
| `biases` | `future_seed` |

## Cross references
- `state`
- `decision`
- `identity`
- `remembers`
- `biases`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.core.braid.memory
object: MemoryScars
mode: deferred
```

## Notes
retains closure history and biases future trajectories
