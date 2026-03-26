# Delta_H - HolonomyDefect

| field | value |
|---|---|
| stable_id | `GLOSS-OBSERVABLE-HOLONOMY-DEFECT` |
| canonical_id | `observable.holonomy.delta_h` |
| card_type | `observable` |
| class | `observable` |
| subclass | `spectrum` |
| status | `measured` |
| certainty_scope | `runtime_measured_observable` |
| units | `dimensionless complex defect` |
| value | `|Delta_H| ~= 0.278322633991 ; R_H ~= 0.077463488592` |

## Description
Global complex holonomy defect after summing the weighted effective phases of all sectors and the zeta pole.

## Formal definition
```text
Delta_H = sum_i a_i exp(i gamma_i^eff) + a_zeta exp(i gamma_zeta^eff)
R_H = |Delta_H|^2
```

## Tags
`type:observable`, `domain:omega`, `domain:foundations`, `status:measured`, `role:coherence`, `layer:runtime`, `bind:runtime`, `math:closure`, `math:holonomy`

## Relational couplings
| relation | targets |
|---|---|
| `measures` | `closure,truthfulness_proxy` |
| `projects_to` | `R_H` |
| `couples_to` | `EffectivePhase,zeta_phase` |

## Cross references
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-STATE-EFFECTIVE-PHASE-gamma_eff_i.md`
- `systems/CIEL_FOUNDATIONS/definitions/cards/GLOSS-OBSERVABLE-CP-TRIANGLE-LOOP-PHASE-triangleloopphase.md`
- `research/holonomic_observed_end_to_end/results/summary.json`
- `reports/phase_components/summary.md`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py`
- `reports/phase_components/summary.md`
- `research/holonomic_observed_end_to_end/results/summary.json`

## Notes
The benchmark comparison is proxy-based: the observed package encodes phase-like variables from truth/support labels rather than directly observed orbital phases. The directional split remains useful for calibration.
