# E0_spinor - B1 Minimal Spinor Gap

| field | value |
|---|---|
| stable_id | `GLOSS-EFFECT-B1-SPINOR-GAP` |
| canonical_id | `effect.b1.spinor_gap` |
| card_type | `effect` |
| class | `observable` |
| subclass | `toy_gap` |
| status | `measured` |
| certainty_scope | `repo_numeric_result` |
| units | `dimensionless toy energy` |
| value | `1/4` |
| numeric_value | `0.25` |

## Description
Measured toy result from the single-loop branch: spinor closure leaves a nonzero minimal spectral gap after defect minimization.

## Formal definition
```text
For n=0 spinor class, a*=1/2 and ground energy = 1/4
```

## Tags
`type:effect`, `type:observable`, `domain:foundations`, `domain:metatime`, `status:measured`, `role:closure`, `role:spin`, `layer:research`, `bind:derived`, `math:topology`, `sector:neutrino`

## Relational couplings
| relation | targets |
|---|---|
| `depends_on` | `chi_a` |
| `depends_on` | `A_theta` |
| `supports` | `SpinorClosure` |

## Cross references
- `GLOSS-CONSTRAINT-CLOSURE-CLASS`
- `GLOSS-CONSTRAINT-SPINOR-CLOSURE`
- `GLOSS-FORMALISM-HOLONOMY-LAGRANGIAN`

## Source-of-truth anchors
- `research/holonomy_closure_b1_b2/results.json`
- `docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md`

## Notes
Numerically trivial but canonically recorded toy measurement.
