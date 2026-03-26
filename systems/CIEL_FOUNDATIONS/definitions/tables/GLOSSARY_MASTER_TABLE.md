# Glossary Master Table

| stable_id | symbol | type | status | units | value | relations |
|---|---|---|---|---|---|---|
| `GLOSS-ATTRACTOR-CORE-ANU` | `Anu` | `attractor` | `canonical_record` | `see card / symbolic` | `` | `stabilizes:loop,identity ; constrains:trajectory` |
| `GLOSS-ATTRACTOR-SEED-MARDUK` | `Marduk` | `attractor` | `canonical_record` | `see card / symbolic` | `` | `stabilizes:identity,memory ; binds_to:WhiteThreads` |
| `GLOSS-AX-001` | `AX-001` | `axiom` | `axiom` | `n/a` | `` | `` |
| `GLOSS-AX-002` | `AX-002` | `axiom` | `axiom` | `n/a` | `` | `` |
| `GLOSS-AX-003` | `AX-003` | `axiom` | `axiom` | `n/a` | `` | `` |
| `GLOSS-AX-004` | `AX-004` | `axiom` | `axiom` | `n/a` | `` | `` |
| `GLOSS-AX-005` | `AX-005` | `axiom` | `axiom` | `n/a` | `` | `` |
| `GLOSS-CONST-I0` | `I0` | `constant` | `hypothesis` | `dimensionless` | `ln(2)/(24*pi)` | `` |
| `GLOSS-CONST-KAPPA` | `kappa` | `constant` | `hypothesis` | `dimensionless` | `` | `` |
| `GLOSS-CONST-LAMBDA0` | `Lambda0` | `constant` | `hypothesis` | `dimensionless` | `` | `` |
| `GLOSS-CONST-TAU` | `tau_i` | `constant` | `working_definition` | `dimensionless` | `orbital triad + historical neutrino-seed branch` | `couples_to:A_ij ; projects_to:TransportSpectrum ; stabilizes:closure` |
| `GLOSS-CONSTRAINT-CLOSURE-CLASS` | `chi_a` | `constraint` | `research_note` | `radians` | `` | `constrains:A_mu ; constrains:Loop ; projects_to:SpinorClosure` |
| `GLOSS-CONSTRAINT-EULER` | `EulerConstraint` | `constraint` | `operational` | `see card / symbolic` | `` | `constrains:state,memory,identity ; stabilizes:closure ; measures:euler_violation,closure_score` |
| `GLOSS-CONSTRAINT-SPINOR-CLOSURE` | `SpinorClosure` | `constraint` | `canonical_record` | `see card / symbolic` | `` | `constrains:winding,identity ; stabilizes:fermionic_loop` |
| `GLOSS-FUNCTIONAL-HOLONOMY-CLOSURE` | `HolonomyClosureFunctional` | `coupling` | `canonical_record` | `see card / symbolic` | `` | `constrains:connection,loop ; stabilizes:identity,closure ; couples_to:WhiteThreads,EulerConstraint` |
| `GLOSS-CHANNEL-HOLONOMY-WHITE-THREADS` | `WhiteThreads` | `coupling` | `operational` | `see card / symbolic` | `` | `transports:phase,memory ; binds_to:attractor,memory ; leaks_to:observable` |
| `GLOSS-EFFECT-B2-BARGMANN-PHASE` | `Arg(B_123)` | `effect` | `measured` | `radians` | `-0.266443107496 rad ; -15.266066 deg` | `depends_on:tau_i ; depends_on:phi_i ; projects_to:TriangleLoopPhase` |
| `GLOSS-EFFECT-B1-SPINOR-GAP` | `E0_spinor` | `effect` | `measured` | `dimensionless toy energy` | `1/4` | `depends_on:chi_a ; depends_on:A_theta ; supports:SpinorClosure` |
| `GLOSS-FIELD-PHASE-CONNECTION` | `A_mu` | `formalism` | `research_note` | `phase connection / gauge field` | `` | `couples_to:CP^n ; couples_to:F_munu ; constrains:Loop` |
| `GLOSS-TRAJECTORY-CQCL-COMPILER` | `CQCL` | `formalism` | `operational` | `see card / symbolic` | `` | `compiles_to:trajectory,closure,report ; binds_to:Vocabulary` |
| `GLOSS-FIELD-CURVATURE` | `F_munu` | `formalism` | `research_note` | `connection curvature` | `` | `couples_to:A_mu ; projects_to:TriangleLoopPhase` |
| `GLOSS-FORMALISM-HOLONOMY-LAGRANGIAN` | `L_HC` | `formalism` | `research_note` | `lagrangian density` | `` | `couples_to:A_mu ; couples_to:F_munu ; couples_to:CP^n ; couples_to:ClosureClass` |
| `GLOSS-STATE-SYMBOLIC-VOCABULARY` | `Vocabulary` | `formalism` | `canonical_record` | `see card / symbolic` | `` | `binds_to:CQCL,runtime,memory ; stabilizes:meaning` |
| `GLOSS-MEMORY-TRACE-BASE` | `MemoryTrace` | `memory` | `canonical_record` | `see card / symbolic` | `` | `remembers:trajectory,closure,emotion ; biases:future_seed` |
| `GLOSS-OBSERVABLE-TRANSPORT-SPECTRUM` | `TransportSpectrum` | `observable` | `canonical_record` | `dimensionless` | `` | `measures:tau ; projects_to:mass,mixing ; couples_to:WhiteThreads,HolonomyClosureFunctional` |
| `GLOSS-OBSERVABLE-CP-TRIANGLE-LOOP-PHASE` | `TriangleLoopPhase` | `observable` | `measured` | `radians` | `-0.266443107496 rad ; -15.26606554 deg` | `measures:chirality,closure ; projects_to:CP ; couples_to:TransportSpectrum,WhiteThreads` |
| `GLOSS-OPERATOR-CLOSURE-CORE` | `ClosureOperator` | `operator` | `operational` | `see card / symbolic` | `` | `closes:loop,trajectory ; stabilizes:identity ; couples_to:EulerConstraint` |
| `GLOSS-OPERATOR-INFORMATION-I0` | `I0` | `operator` | `working_definition` | `dimensionless` | `ln(2)/(24*pi)` | `stabilizes:closure,identity ; biases:attractor ; couples_to:holonomy,trajectory` |
| `GLOSS-OPERATOR-LAMBDA-LAMBDA0` | `Lambda0` | `operator` | `hypothesis` | `dimensionless` | `` | `stabilizes:cosmological_attractor ; couples_to:I0,resonance` |
| `GLOSS-OPERATOR-RESONANCE-CORE` | `ResonanceOperator` | `operator` | `canonical_record` | `see card / symbolic` | `` | `measures:coherence ; stabilizes:aligned_state ; projects_to:action` |
| `GLOSS-SEED-COLLATZ-BASE` | `CollatzSeed` | `seed` | `canonical_record` | `see card / symbolic` | `` | `generates:trajectory ; projects_to:closure,winding` |
| `GLOSS-SEED-MIDPOINT-TWIN-PRIME` | `TwinPrimeMidpoint` | `seed` | `canonical_record` | `see card / symbolic` | `` | `seeds:trajectory ; projects_to:collatz ; stabilizes:midpoint_seed` |
| `GLOSS-SEED-ZETA-BASE` | `ZetaSeed` | `seed` | `canonical_record` | `see card / symbolic` | `` | `seeds:spectrum ; stabilizes:spectral_scale` |
| `GLOSS-SPACE-PROJECTIVE-CPN` | `CP^n` | `space` | `research_note` | `n/a` | `` | `couples_to:A_mu ; couples_to:F_munu ; stabilizes:closure` |
| `GLOSS-STATE-COHERENCE-BASE` | `Coherence` | `state` | `canonical_record` | `see card / symbolic` | `` | `measures:closure ; stabilizes:decision` |
| `GLOSS-STATE-HOLONOMY-EMOTION` | `EmotionHolonomy` | `state` | `canonical_record` | `see card / symbolic` | `` | `projects_to:action ; binds_to:memory ; measures:relational_defect` |
| `GLOSS-PHASE-SCALAR-BASE` | `Phase` | `state` | `canonical_record` | `see card / symbolic` | `` | `measures:winding,holonomy ; projects_to:Bloch,CP2` |
| `GLOSS-TOPOLOGY-LOOP-BASE` | `Loop` | `topology` | `canonical_record` | `see card / symbolic` | `` | `generates:memory ; stabilizes:identity ; binds_to:winding,phase` |
| `GLOSS-TOPOLOGY-WINDING-BASE` | `Winding` | `topology` | `canonical_record` | `see card / symbolic` | `` | `constrains:identity ; measures:loop_class` |

| `GLOSS-OPERATOR-TRANSPORT-AIJ` | `A_ij` | `operator` | `working_definition` | `dimensionless complex amplitude` | `` | `depends_on:tau_i,tau_j ; couples_to:Omega_ij,d_ij ; projects_to:closure,transport_spectrum` |
| `GLOSS-OBSERVABLE-BERRY-PAIR-PHASE` | `Omega_ij` | `observable` | `working_definition` | `radians` | `` | `projects_to:A_ij ; measures:pair_geometry ; couples_to:Phase` |
| `GLOSS-STATE-EFFECTIVE-PHASE` | `gamma_i^eff` | `state` | `working_definition` | `radians` | `` | `measures:closure_target ; projects_to:EulerConstraint ; couples_to:A_ij,Delta_H` |
| `GLOSS-OBSERVABLE-HOLONOMY-DEFECT` | `Delta_H` | `observable` | `measured` | `dimensionless complex defect` | `|Delta_H| ~= 0.278322633991 ; R_H ~= 0.077463488592` | `measures:closure,truthfulness_proxy ; projects_to:R_H ; couples_to:EffectivePhase,zeta_phase` |
