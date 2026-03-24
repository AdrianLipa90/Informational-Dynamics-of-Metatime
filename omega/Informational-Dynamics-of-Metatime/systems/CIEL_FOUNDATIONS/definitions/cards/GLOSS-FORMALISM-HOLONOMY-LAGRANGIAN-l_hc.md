# L_HC - Holonomy Closure Lagrangian

| field | value |
|---|---|
| stable_id | `GLOSS-FORMALISM-HOLONOMY-LAGRANGIAN` |
| canonical_id | `formalism.holonomy.closure.lagrangian` |
| card_type | `formalism` |
| class | `formalism` |
| subclass | `lagrangian` |
| status | `research_note` |
| certainty_scope | `active_repo_formalism` |
| units | `lagrangian density` |
| value | `` |

## Description
Current minimal non-arbitrary Lagrangian used to derive B1 and B2 branches from state, connection, curvature, and closure classes.

## Formal definition
```text
(D_mu psi)^dagger D^mu psi - lambda(psi^dagger psi-1) - (1/4g^2)F^2 - mu sum_a(oint A - chi)^2
```

## Tags
`type:formalism`, `domain:foundations`, `domain:metatime`, `status:research_note`, `role:closure`, `role:holonomy`, `role:transport`, `layer:foundations`, `bind:derived`, `math:lagrangian`, `sector:neutrino`

## Relational couplings
| relation | targets |
|---|---|
| `couples_to` | `A_mu` |
| `couples_to` | `F_munu` |
| `couples_to` | `CP^n` |
| `couples_to` | `ClosureClass` |

## Cross references
- `GLOSS-FIELD-PHASE-CONNECTION`
- `GLOSS-FIELD-CURVATURE`
- `GLOSS-CONSTRAINT-CLOSURE-CLASS`
- `GLOSS-EFFECT-B1-SPINOR-GAP`
- `GLOSS-EFFECT-B2-BARGMANN-PHASE`

## Source-of-truth anchors
- `docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md`

## Notes
Research note formalism; next step is promotion into frozen derivation text and code solver.
