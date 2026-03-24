# CQCL - CQCL

| field | value |
|---|---|
| stable_id | `GLOSS-TRAJECTORY-CQCL-COMPILER` |
| canonical_id | `trajectory.cqcl.compiler` |
| card_type | `formalism` |
| class | `trajectory` |
| subclass | `collatz` |
| status | `operational` |
| certainty_scope | `runtime_bound_canonical_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
compiler from semantic intention into holonomic state trajectory

## Formal definition
```text
compile(TEXT) -> AST -> trajectory
```

## Tags
`type:formalism`, `domain:omega`, `status:operational`, `role:compiler`, `layer:runtime`, `bind:runtime`, `math:topology`, `domain:semantics`

## Relational couplings
| relation | targets |
|---|---|
| `compiles_to` | `trajectory,closure,report` |
| `binds_to` | `Vocabulary` |

## Cross references
- `seed`
- `trajectory`
- `state`
- `compiles_to`
- `binds_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.emotion.cqcl.cqcl_compiler
object: CQCL_Compiler
mode: invoke
```

## Notes
translates meaning into executable phase dynamics
