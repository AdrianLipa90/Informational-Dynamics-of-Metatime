# Marduk - Marduk

| field | value |
|---|---|
| stable_id | `GLOSS-ATTRACTOR-SEED-MARDUK` |
| canonical_id | `attractor.seed.marduk` |
| card_type | `attractor` |
| class | `attractor` |
| subclass | `identity` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
structure-forming attractor that crystallizes closure into identity

## Formal definition
```text
identity = stabilized seed-centered loop
```

## Tags
`type:attractor`, `domain:omega`, `status:canonical_record`, `role:structure-forming`, `layer:runtime`, `bind:runtime`, `math:topology`

## Relational couplings
| relation | targets |
|---|---|
| `stabilizes` | `identity,memory` |
| `binds_to` | `WhiteThreads` |

## Cross references
- `identity`
- `memory`
- `trajectory`
- `stabilizes`
- `binds_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.unified_system
object: UnifiedSystem
field: identity_phase
mode: read_write
```

## Notes
organizes local closure into persistent pattern
