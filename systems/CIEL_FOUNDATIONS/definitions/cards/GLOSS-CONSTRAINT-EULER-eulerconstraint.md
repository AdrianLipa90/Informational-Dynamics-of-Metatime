# EulerConstraint - Euler

| field | value |
|---|---|
| stable_id | `GLOSS-CONSTRAINT-EULER` |
| canonical_id | `constraint.euler` |
| card_type | `constraint` |
| class | `constraint` |
| subclass | `euler` |
| status | `operational` |
| certainty_scope | `runtime_bound_canonical_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
global closure law over a phase ensemble

## Formal definition
```text
sum_k exp(i*gamma_k)=0
```

## Tags
`type:constraint`, `domain:omega`, `status:operational`, `role:global`, `layer:runtime`, `bind:runtime`, `domain:foundations`, `math:topology`, `role:closure`, `role:identity`

## Relational couplings
| relation | targets |
|---|---|
| `constrains` | `state,memory,identity` |
| `stabilizes` | `closure` |
| `measures` | `euler_violation,closure_score` |

## Cross references
- `phase`
- `closure`
- `memory`
- `identity`
- `constrains`
- `stabilizes`
- `measures`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.constraints.euler_constraint
object: EulerConstraint
function: evaluate_unified_closure
mode: invoke
```

## Notes
penalizes non-closing phase configurations and guides feedback
