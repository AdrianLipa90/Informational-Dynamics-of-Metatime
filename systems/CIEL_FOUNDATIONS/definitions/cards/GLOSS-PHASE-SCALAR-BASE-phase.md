# Phase - Phase

| field | value |
|---|---|
| stable_id | `GLOSS-PHASE-SCALAR-BASE` |
| canonical_id | `phase.scalar.base` |
| card_type | `state` |
| class | `phase` |
| subclass | `holonomy` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `radians` |
| value | `` |

## Description
Angular state coordinate governing closure and transport. In the current runtime the operational target is the effective phase `gamma_i^eff = phi_i + gamma_B,i`.

## Formal definition
```text
phi ~ arg(psi)
gamma_i^eff = phi_i + gamma_B,i
```

## Tags
`type:state`, `domain:omega`, `status:canonical_record`, `role:angular`, `layer:runtime`, `bind:registry`, `math:spectrum`, `math:topology`, `math:connection`, `role:phase`

## Relational couplings
| relation | targets |
|---|---|
| `measures` | `winding,holonomy` |
| `projects_to` | `Bloch,CP2` |
| `couples_to` | `BerryPairPhase,EffectivePhase` |

## Cross references
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-STATE-EFFECTIVE-PHASE-gamma_eff_i.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-OBSERVABLE-BERRY-PAIR-PHASE-omega_ij.md`
- `systems/CIEL_FOUNDATIONS/derivations/D-0101-phase-components-from-aij-tau.md`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py`

## Runtime binding
```yaml
module: ciel_omega.phase_equation_of_motion
field: phase
mode: deferred
```

## Notes
The repo-level phase architecture now distinguishes bare local phase `phi_i`, local Berry accumulation `gamma_B,i`, pair Berry phase `Omega_ij`, and the closure target `gamma_i^eff`.
