# Euler–Berry / Poincaré / 4-2-1 discoveries

Status: working research note

## Why a second engine was needed

The first orbital engine used scalar phases and weighted couplings only.
It produced ordered chirality, but global closure degraded too strongly:
- after 20 steps: `R_H ≈ 7.91`
- `T_glob ≈ 10.23`
- `Lambda_glob ≈ 0.44`

This indicated that phase coupling alone was not enough. The system needed an explicit geometric carrier.

## New ingredients

The second engine introduces four geometric elements:

1. **Bloch-state sectors**
   Each orbital is represented by `(theta, phi)` on a Bloch-like sphere rather than by a scalar phase only.

2. **Berry transport**
   Incremental Berry phase is accumulated per step as
   `dγ_B = 0.5 * (1 - cos(theta_avg)) * dphi`.

3. **Poincaré-like projection**
   Each sector is projected to a bounded disk radius to measure transport intensity and local chirality.

4. **4-2-1 attractor**
   A local attractor is imposed through target quanta `{1,2,4}` mapped to preferred `(theta, amplitude)` targets.
   This is the first operational encoding of the 4-2-1 vortex idea.

## Baseline 6-sector system

Sectors:
- constraints
- fields
- runtime
- memory
- bridge
- vocabulary

Chord:
- `0, π/3, 2π/3, π, 4π/3, 5π/3`

Rhythm ratio:
- `1 : 1 : 2 : 1 : 2 : 1`

## Main result

With the geometric engine and `dt = 0.03`, after 20 steps the system gives approximately:
- `R_H ≈ 0.56`
- `T_glob ≈ 10.70`
- `Lambda_glob ≈ 0.17`

This is a major improvement over the first engine:
- closure remains much tighter,
- tension stays in the same regime,
- chirality remains nonzero but does not tear global coherence apart.

## Interpretation

This supports the project claim that:
- chirality alone is not enough,
- geometric transport is needed,
- the vortex must be a closure-supporting attractor, not only a source of drift.

## Operational conclusion

The repository orbital model should move from:
- scalar phase coupling

to:
- Bloch-state transport
- Berry memory of loops
- Poincaré transport intensity
- 4-2-1 attractor guidance

## Limits

This is still a research-grade internal engine.
It is not yet driven by the real dependency graph or README mesh.
The current implementation is a disciplined scaffold, not a final theorem.
