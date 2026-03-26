# WhiteThreads - WhiteThreads

| field | value |
|---|---|
| stable_id | `GLOSS-CHANNEL-HOLONOMY-WHITE-THREADS` |
| canonical_id | `channel.holonomy.white_threads` |
| card_type | `coupling` |
| class | `channel` |
| subclass | `holonomy` |
| status | `operational` |
| certainty_scope | `runtime_bound_canonical_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
nonlocal holonomy transport between states

## Formal definition
```text
W_ij = <psi_j|U_gamma|psi_i>
```

## Tags
`type:coupling`, `domain:omega`, `status:operational`, `role:nonlocal`, `layer:runtime`, `bind:registry`, `domain:foundations`, `domain:metatime`, `math:topology`, `math:connection`, `role:holonomy`, `role:coupling`

## Relational couplings
| relation | targets |
|---|---|
| `transports` | `phase,memory` |
| `binds_to` | `attractor,memory` |
| `leaks_to` | `observable` |

## Cross references
- `state`
- `memory`
- `closure`
- `transports`
- `binds_to`
- `leaks_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.bridge.memory_core_phase_bridge
object: MemoryCorePhaseBridge
function: compute_white_thread_amplitude
mode: deferred
```

## Notes
transports relative phase and closure memory between nodes
