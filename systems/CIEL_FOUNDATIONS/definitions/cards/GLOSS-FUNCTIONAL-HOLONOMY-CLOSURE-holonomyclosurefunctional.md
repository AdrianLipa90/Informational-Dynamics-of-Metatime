# HolonomyClosureFunctional - HolonomyClosureFunctional

| field | value |
|---|---|
| stable_id | `GLOSS-FUNCTIONAL-HOLONOMY-CLOSURE` |
| canonical_id | `functional.holonomy.closure` |
| card_type | `coupling` |
| class | `functional` |
| subclass | `closure_holonomy` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
penalizes mismatch between loop holonomy and admissible closure class

## Formal definition
```text
C_H[A] = sum_a (oint_gamma_a A - chi_a)^2
```

## Tags
`type:coupling`, `domain:omega`, `status:canonical_record`, `role:penalizes`, `layer:ontology`, `bind:registry`, `domain:foundations`

## Relational couplings
| relation | targets |
|---|---|
| `constrains` | `connection,loop` |
| `stabilizes` | `identity,closure` |
| `couples_to` | `WhiteThreads,EulerConstraint` |

## Cross references
- `connection`
- `closure`
- `identity`
- `constrains`
- `stabilizes`
- `couples_to`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Notes
drives connection toward admissible bosonic or spinor loop class
