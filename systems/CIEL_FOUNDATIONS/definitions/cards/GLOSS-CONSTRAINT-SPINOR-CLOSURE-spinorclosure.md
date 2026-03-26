# SpinorClosure - SpinorClosure

| field | value |
|---|---|
| stable_id | `GLOSS-CONSTRAINT-SPINOR-CLOSURE` |
| canonical_id | `constraint.spinor.closure` |
| card_type | `constraint` |
| class | `constraint` |
| subclass | `spinor` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
admissible closure class with 2pi -> -1, 4pi -> +1 behavior

## Formal definition
```text
integral dphi = pi(2n+1)
```

## Tags
`type:constraint`, `domain:omega`, `status:canonical_record`, `role:admissible`, `layer:runtime`, `bind:registry`, `domain:foundations`, `math:topology`, `role:spin`, `role:closure`

## Relational couplings
| relation | targets |
|---|---|
| `constrains` | `winding,identity` |
| `stabilizes` | `fermionic_loop` |

## Cross references
- `phase`
- `identity`
- `closure`
- `constrains`
- `stabilizes`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.constraints.euler_constraint
field: spinor
mode: deferred
```

## Notes
permits half-quantized return classes
