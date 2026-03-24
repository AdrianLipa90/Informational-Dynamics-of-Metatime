# ZETA_POLE_TETRAHEDRAL_PATCH

This patch introduces `zeta_pole` as a composite tetrahedral Bloch-frame into the global orbital engine.

Core changes:
- `ZetaVertex` and `ZetaPole` added to the orbital model.
- `use_zeta_pole` flag added to the global pass parameters.
- `closure_penalty` extended with an additional `A_{i\zeta}	au_\zeta` term.
- tetrahedral rigidity penalty added:
  `zeta_tetra_defect`.
- global reports now expose:
  - `zeta_enabled`
  - `zeta_tetra_defect`
  - `zeta_effective_tau`
  - `zeta_effective_phase`
  - `zeta_coupling_norm`

The pole is treated as a composite sector, not as a single scalar node.
