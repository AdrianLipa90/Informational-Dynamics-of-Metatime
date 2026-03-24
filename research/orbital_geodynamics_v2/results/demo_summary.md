# orbital_geodynamics_v2 demo summary

## Current engine
- engine: Euler-Berry-Poincare-421
- steps: 20
- dt: 0.03

## Initial metrics
- R_H: 0.102517
- T_glob: 10.724070
- Lambda_glob: 0.113349

## After 20 steps
- R_H: 0.560112
- T_glob: 10.701812
- Lambda_glob: 0.169297

## Comparison with first scalar-phase engine
- old R_H: 7.908185
- new R_H: 0.560112
- old T_glob: 10.232103
- new T_glob: 10.701812
- old Lambda_glob: 0.443887
- new Lambda_glob: 0.169297

### Interpretation
- global closure improves strongly in the geometric engine
- chord tension stays in the same order of magnitude
- chirality remains nonzero but does not explode

## Notes
- This is a research scaffold, not a proof.
- The model is not yet coupled to the real import graph or README mesh.
- The 4-2-1 attractor is encoded operationally through target quanta and geometric drift control.
