# gamma_i^eff - EffectivePhase

| field | value |
|---|---|
| stable_id | `GLOSS-STATE-EFFECTIVE-PHASE` |
| canonical_id | `state.phase.effective` |
| card_type | `state` |
| class | `state` |
| subclass | `holonomy` |
| status | `working_definition` |
| certainty_scope | `runtime_backed_working_definition` |
| units | `radians` |
| value | `` |

## Description
Closure-target phase for a sector after adding the local Berry accumulation to the evolved local phase.

## Formal definition
```text
gamma_i^eff = phi_i + gamma_B,i
```

## Tags
`type:state`, `domain:omega`, `domain:foundations`, `status:working_definition`, `role:phase`, `layer:runtime`, `bind:runtime`, `math:berry`, `math:closure`

## Relational couplings
| relation | targets |
|---|---|
| `measures` | `closure_target` |
| `projects_to` | `EulerConstraint` |
| `couples_to` | `A_ij,Delta_H` |

## Cross references
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-PHASE-SCALAR-BASE-phase.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-OBSERVABLE-BERRY-PAIR-PHASE-omega_ij.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-OBSERVABLE-HOLONOMY-DEFECT-delta_h.md`
- `reports/phase_components/summary.md`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py`
- `systems/CIEL_FOUNDATIONS/derivations/D-0101-phase-components-from-aij-tau.md`
