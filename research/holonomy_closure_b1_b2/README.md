# Holonomy Closure B1/B2

This research sector stores the non-arbitrary closure derivations requested on 2026-03-24.

## Scope
- **B1**: minimal one-loop U(1) toy model with bosonic and spinor closure classes.
- **B2**: CP^2-inspired three-state triangle built from canonical repo geometry seeds.

## Inputs
- `reports/global_orbital_coherence_pass/real_geometry.json`
- `docs/concepts/TAU_AIJ_GLOBAL_IMPLEMENTATION.md`
- `docs/concepts/EULER_BERRY_POINCARE_421_DISCOVERIES.md`

## Main outputs
- `results.json`
- `solve_b1_b2.py`

## B1 summary
For constant connection `A_theta = a` on a unit loop:
- bosonic closure (`chi = 0`) gives `a* = 0`, zero ground energy,
- spinor closure (`chi = pi`) gives `a* = 1/2`, minimal ground energy `1/4`.

This is the first minimal record in the repo where nonzero spectral structure appears from closure class alone.

## B2 summary
Using canonical sector seeds `(constraints, memory, runtime)` with taus `(0.263, 0.353, 0.489)` and phases from `real_geometry.json`, the normalized CP^2-style projective states produce a nonzero Bargmann loop phase:
- `Arg(B_123) = -0.266443107496 rad`
- `Arg(B_123) = -15.266066 deg`

This is recorded as a CP-like loop observable generated from canonical repo geometry rather than from an externally inserted phase parameter.
