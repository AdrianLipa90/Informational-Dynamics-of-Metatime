# NON_ARBITRARY_HOLONOMY_CLOSURE_B1_B2

Status: active research note
Date: 2026-03-24

## Purpose
Record the first non-arbitrary closure derivation in the canonical repo, starting from a minimal Lagrangian over a projective state `psi` and a phase connection `A`, then storing the two requested branches:
- **B1** minimal one-loop toy model
- **B2** CP^2-like three-state loop phase

## Core Lagrangian

\[
\mathcal{L} = (D_\mu\psi)^\dagger D^\mu\psi - \lambda (\psi^\dagger\psi - 1) - \frac{1}{4g^2}F_{\mu\nu}F^{\mu\nu} - \mu \sum_a \left(\oint_{\gamma_a} A - \chi_a\right)^2
\]

with
\[
D_\mu\psi = (\partial_\mu + i A_\mu)\psi, \qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.
\]

## Euler–Lagrange system

\[
D_\mu D^\mu \psi + \lambda \psi = 0
\]

\[
\frac{1}{g^2}\partial_\nu F^{\nu\mu} = J_\psi^\mu + \mu J_{closure}^\mu
\]

\[
\psi^\dagger \psi = 1
\]

where the closure source is induced by the holonomy defect functional
\[
\mathcal{C}[A] = \sum_a \left(\oint_{\gamma_a} A - \chi_a\right)^2.
\]

## B1 — minimal loop result

On a single angular loop `theta \in [0, 2\pi)` with constant connection `A_theta = a`:

- bosonic closure class `chi = 2\pi n` is minimized by `a = n`,
- spinor closure class `chi = (2n+1)\pi` is minimized by `a = n + 1/2`.

For the lowest spinor sector (`n = 0`), the minimal kinetic spectrum is shifted and the ground energy is `1/4` instead of `0`.

## B2 — CP^2-style triangle result

The canonical triad `(constraints, memory, runtime)` from `reports/global_orbital_coherence_pass/real_geometry.json` defines three projective seeds
\[
\psi_i \sim [1, \tau_i e^{i\phi_i}, \tau_i^2 e^{2 i\phi_i}].
\]

Using the current canonical values
- `tau = (0.263, 0.353, 0.489)`
- `phi = (0, \pi, 2.094395102393)`

the loop Bargmann invariant is
\[
B_{123} = \langle \psi_1|\psi_2 \rangle \langle \psi_2|\psi_3 \rangle \langle \psi_3|\psi_1 \rangle
\]
with
\[
\operatorname{Arg}(B_{123}) = -0.266443107496\,\text{rad} = -15.266066^\circ.
\]

This is the first canonical repo note in which a nonzero CP-like loop phase is obtained directly from current geometry seeds rather than from an inserted fitted phase.

## Cross-references inside canonical repo
- `docs/concepts/TAU_AIJ_GLOBAL_IMPLEMENTATION.md`
- `docs/concepts/EULER_BERRY_POINCARE_421_DISCOVERIES.md`
- `reports/global_orbital_coherence_pass/real_geometry.json`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## External source triage from `Metatime-main`
The following files were inspected as relevant source anchors for future promotion or comparison:
- `Metatime-main/README.md`
- `Metatime-main/documents/Docs.md`
- `Metatime-main/documents/White_threads.pdf`
- `Metatime-main/documents/SM_and_M_Theory_generalisation.pdf`
- `Metatime-main/documents/MetatimeRama.pdf`
- `Metatime-main/documents/fa00b095.md`
- `Metatime-main/simulations/Toy-Model White-Thread Matrix F_ij — Next Steps/README.md`

## Current boundary
This note removes the earlier arbitrary insertion of `tau_i`, `I0`, and a free CP phase at the level of principle, but it does **not** yet prove that the full neutrino-sector values follow uniquely from the complete interacting system.
