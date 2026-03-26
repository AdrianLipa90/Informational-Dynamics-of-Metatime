# B1/B2 REGISTRY UPDATE — 2026-03-24

## Scope
This report records the canonical repository update that stores the new non-arbitrary closure derivation and both requested branches:
- B1 minimal loop toy model
- B2 CP^2-style triangle loop phase

## Files added
- `docs/concepts/NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2.md`
- `research/holonomy_closure_b1_b2/README.md`
- `research/holonomy_closure_b1_b2/solve_b1_b2.py`
- `research/holonomy_closure_b1_b2/results.json`
- `reports/theory/B1_B2_REGISTRY_UPDATE_2026-03-24.md`
- `reports/theory/METATIME_MAIN_SOURCE_TRIAGE_2026-03-24.md`

## Files updated
- `docs/concepts/README.md`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`
- `manifests/linkage_map.json`

## Main recorded numerical result
For the canonical triad `(constraints, memory, runtime)` the CP-like loop observable from the Bargmann invariant is:
- `Arg(B_123) = -0.266443107496 rad`
- `Arg(B_123) = -15.266066 deg`

## Registry effect
The repo now stores the derivation in three places:
1. **concept note** — semantic and mathematical record
2. **runtime vocabulary** — canonical symbol/operator registration
3. **research package** — executable B1/B2 computation and results log

## Boundary
`import_dependency_graph.*` was not regenerated in this update because the new package is documentation/research-only and does not change canonical runtime imports. This is an explicit known manifest gap, not a hidden inconsistency.
