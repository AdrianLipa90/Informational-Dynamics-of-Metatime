# Winding - Winding

| field | value |
|---|---|
| stable_id | `GLOSS-TOPOLOGY-WINDING-BASE` |
| canonical_id | `topology.winding.base` |
| card_type | `topology` |
| class | `topology` |
| subclass | `winding` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
integer topological class of phase return

## Formal definition
```text
nu = (1/(2*pi)) * integral dphi
```

## Tags
`type:topology`, `domain:omega`, `status:canonical_record`, `role:integer`, `layer:runtime`, `bind:registry`, `domain:foundations`, `math:topology`, `role:identity`, `role:topology`

## Relational couplings
| relation | targets |
|---|---|
| `constrains` | `identity` |
| `measures` | `loop_class` |

## Cross references
- `identity`
- `closure`
- `trajectory`
- `constrains`
- `measures`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.fields.soul_invariant
object: SoulInvariant
mode: deferred
```

## Notes
counts loop turns and defines identity class
