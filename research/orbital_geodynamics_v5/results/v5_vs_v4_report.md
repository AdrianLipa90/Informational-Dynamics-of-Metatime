# V5 Monte Carlo + Spectral Comparison

## Baseline v4 after 20 steps
- R_H: 0.188223
- T_glob: 2.948105
- Lambda_glob: 0.170605
- closure_penalty: 5.837493

## Best Monte Carlo run
- R_H: 0.174195
- T_glob: 2.517631
- Lambda_glob: 0.165156
- closure_penalty: 5.475675
- spectral_radius_A: 1.716730
- spectral_gap_A: 0.792482
- fiedler_L: 0.170651

## Best parameters
- dt: 0.022510
- tau_eta: 0.008504
- tau_reg: 0.002375
- sigma: 0.209927
- beta: 0.885885
- gamma: 0.338362
- I0: 0.008114
- mesh_boost: 0.990207
- tension_weight: 0.248417
- closure_weight: 0.089455

## Delta vs baseline
- R_H: -0.014028
- T_glob: -0.430474
- Lambda_glob: -0.005449
- closure_penalty: -0.361818

## Top sensitivity by |corr(objective)|
- sigma: 0.637062
- tau_eta: 0.381463
- gamma: -0.212998
- beta: -0.187572
- mesh_boost: 0.173896
- dt: 0.149521
- tau_reg: 0.052372
- I0: 0.051209
- closure_weight: 0.044781
- tension_weight: 0.020384