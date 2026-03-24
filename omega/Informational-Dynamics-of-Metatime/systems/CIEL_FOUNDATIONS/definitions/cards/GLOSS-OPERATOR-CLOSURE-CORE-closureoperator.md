# ClosureOperator - ClosureOperator

| field | value |
|---|---|
| stable_id | `GLOSS-OPERATOR-CLOSURE-CORE` |
| canonical_id | `operator.closure.core` |
| card_type | `operator` |
| class | `operator` |
| subclass | `closure` |
| status | `operational` |
| certainty_scope | `runtime_bound_canonical_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
transforms open trajectories into admissible loop classes

## Formal definition
```text
min Delta_closure subject to topology
```

## Tags
`type:operator`, `domain:omega`, `status:operational`, `role:transforms`, `layer:runtime`, `bind:runtime`, `math:topology`

## Relational couplings
| relation | targets |
|---|---|
| `closes` | `loop,trajectory` |
| `stabilizes` | `identity` |
| `couples_to` | `EulerConstraint` |

## Cross references
- `trajectory`
- `identity`
- `memory`
- `closes`
- `stabilizes`
- `couples_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.constraints.euler_constraint
function: apply_active_euler_feedback
mode: invoke
```

## Notes
drives phase toward admissible holonomy class
