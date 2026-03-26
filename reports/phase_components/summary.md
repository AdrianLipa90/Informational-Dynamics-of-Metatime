# Orbital Phase Components and Observation Check

This report derives the current canonical phase decomposition from the orbital engine and compares the resulting coherence observables against the repo's observed benchmark package.

## Governing relations

- Local effective phase: $\gamma_i^{\mathrm{eff}} = \phi_i + \gamma_{B,i}$.
- Pair transport kernel: $A_{ij} = (w_{ij} \tau\text{-factor}_{ij}) e^{i(\beta \Omega_{ij} - \gamma d_{ij})}$.
- Tau resonance factor: $\tau\text{-factor}_{ij} = \exp\left[-\frac12\left(\frac{\log(\tau_i/\tau_j)}{\sigma}\right)^2\right]$.
- Closure relation: $\sum_j A_{ij}\tau_j + A_{i\zeta}\tau_\zeta \approx e^{i\gamma_i^{\mathrm{eff}}}$.
- Euler leak angle: $\theta_E = \tfrac{\pi}{2}(D_f-2)$.

## Sector phases

| sector | tau | phi_local | berry | effective | lhs_phase | phase_error | residual |
|---|---:|---:|---:|---:|---:|---:|---:|
| constraints | 0.162228 | 0.181536 | 0.014087 | 0.195623 | -0.647260 | -0.842883 | 0.845771 |
| fields | 0.241565 | 0.991083 | -0.006496 | 0.984587 | -0.901358 | -1.885945 | 1.073579 |
| runtime | 0.408080 | 2.106456 | 0.006001 | 2.112456 | -0.366438 | -2.478894 | 1.094811 |
| memory | 0.305484 | 2.921088 | -0.054754 | 2.866334 | -0.758912 | 2.657939 | 1.164285 |
| bridge | 0.193900 | 4.282621 | 0.041902 | 4.324523 | -0.322306 | 1.636357 | 1.097435 |
| vocabulary | 0.182256 | 5.244118 | 0.000885 | 5.245003 | -0.432891 | 0.605291 | 0.749465 |

## Representative pair transport terms

| pair | tau_factor | Omega_ij | d_ij | arg(A_ij) | |A_ij| |
|---|---:|---:|---:|---:|---:|
| constraints->fields | 0.165560 | 0.062118 | 0.508884 | -0.117158 | 0.152644 |
| constraints->runtime | 0.000064 | 0.455283 | 2.241147 | -0.354991 | 0.000057 |
| constraints->memory | 0.010624 | 0.388624 | 1.665706 | -0.219335 | 0.009381 |
| constraints->bridge | 0.697087 | -0.448688 | 2.059268 | -1.094264 | 0.690261 |
| constraints->vocabulary | 0.857492 | -0.094048 | 0.705306 | -0.321965 | 0.652614 |
| fields->constraints | 0.165560 | -0.062118 | 0.508884 | -0.227216 | 0.152644 |
| fields->runtime | 0.044195 | 0.315290 | 1.920832 | -0.370627 | 0.039022 |
| fields->memory | 0.535105 | 0.340535 | 1.626890 | -0.248803 | 0.052987 |
| fields->bridge | 0.578038 | -0.731601 | 2.407419 | -1.462693 | 0.510389 |
| fields->vocabulary | 0.406364 | -0.209620 | 1.174990 | -0.583272 | 0.338969 |

## Global observables

- holonomy_defect_abs: 0.278322633991
- holonomy_defect_phase: 1.199501441949
- R_H: 0.077463488592
- T_glob: 2.583958108544
- Lambda_glob: 0.096815196635
- closure_penalty: 6.188132507053
- spectral_radius_A: 1.57713404743
- spectral_gap_A: 0.746659326181
- fiedler_L: 0.160953468733

## Zeta / Euler scaling

- enabled: True
- effective_tau: 0.3645
- effective_phase: 0.004766952652
- D_f: 2.57
- euler_leak_angle: 0.895353906273

## Observation check

- repo_R_H: 0.077463488592
- truthful_general_mean_H: 0.21873157442875774
- truthful_qa_mean_H: 0.2539757847158979
- hallucinated_general_mean_H: 2.128904990151081
- repo_R_H_below_truthful_general: True
- repo_R_H_below_truthful_qa: True
- triangle_loop_phase_rad (B2): -0.26644310749634853
- zeta_effective_phase_rad: 0.004766952652

## Interpretation

The current canonical run stays deep inside the truthful side of the observed benchmark split: the repo-level $R_H$ is below the truthful means for the General and QA datasets and far below the hallucinated regime. The B2 triangle loop phase remains nonzero, so closure is not being achieved by collapsing chirality to zero.