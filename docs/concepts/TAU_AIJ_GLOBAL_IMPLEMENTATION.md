# TAU_AIJ_GLOBAL_IMPLEMENTATION

Status: implemented research note

This note records the first global implementation of the coupling
\(A_{ij}(	au_i,	au_j,\Omega_{ij},d_{ij})\) in the repository orbital engine.

## Main result

Compared to the previous real-mesh EB421 engine, the v3 engine reduces final global coherence defect after 20 steps from **1.248511** to **0.278533** while preserving nonzero chirality.

## Meaning

This supports the thesis that the dynamics stabilizes more naturally when the transport operator is derived from local time modes \(	au_i\) rather than from manually fixed weights alone.

## Remaining issue

The local closure penalty remains high and must still be tuned.
