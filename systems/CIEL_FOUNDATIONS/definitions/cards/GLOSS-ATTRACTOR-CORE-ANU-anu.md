# Anu - Anu

| field | value |
|---|---|
| stable_id | `GLOSS-ATTRACTOR-CORE-ANU` |
| canonical_id | `attractor.core.anu` |
| card_type | `attractor` |
| class | `attractor` |
| subclass | `core` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
global attractor of recurrence and closure

## Formal definition
```text
A_core = argmin Delta_closure
```

## Tags
`type:attractor`, `domain:omega`, `status:canonical_record`, `role:global`, `layer:runtime`, `bind:registry`, `math:spectrum`, `math:topology`

## Relational couplings
| relation | targets |
|---|---|
| `stabilizes` | `loop,identity` |
| `constrains` | `trajectory` |

## Cross references
- `trajectory`
- `identity`
- `closure`
- `stabilizes`
- `constrains`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.runtime.omega.omega_runtime
object: OmegaRuntime
field: core_attractor
mode: deferred
```

## Notes
pulls trajectories toward repeatable closure classes
