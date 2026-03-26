# TriangleLoopPhase - TriangleLoopPhase

| field | value |
|---|---|
| stable_id | `GLOSS-OBSERVABLE-CP-TRIANGLE-LOOP-PHASE` |
| canonical_id | `observable.cp.triangle_loop_phase` |
| card_type | `observable` |
| class | `observable` |
| subclass | `loop_phase` |
| status | `measured` |
| certainty_scope | `repo_measured_observable` |
| units | `radians` |
| value | `-0.266443107496 rad ; -15.26606554 deg` |

## Description
Gauge-invariant three-state loop phase used as the canonical CP-like observable.

## Formal definition
```text
Phi_123 = Arg(<psi1|psi2><psi2|psi3><psi3|psi1>)
```

## Tags
`type:observable`, `domain:omega`, `status:measured`, `role:gauge-invariant`, `layer:ontology`, `bind:registry`, `domain:foundations`, `domain:metatime`, `math:spectrum`, `math:connection`, `role:cp`, `sector:neutrino`

## Relational couplings
| relation | targets |
|---|---|
| `measures` | `chirality,closure` |
| `projects_to` | `CP` |
| `couples_to` | `TransportSpectrum,WhiteThreads` |

## Cross references
- `docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md`
- `research/holonomy_closure_b1_b2/results.json`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-OBSERVABLE-HOLONOMY-DEFECT-delta_h.md`

## Source-of-truth anchors
- `docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md`
- `research/holonomy_closure_b1_b2/results.json`

## Notes
This value is obtained from the canonical triad `(constraints, memory, runtime)` using repo-derived `tau` and `phi` seeds rather than an externally inserted fit.
