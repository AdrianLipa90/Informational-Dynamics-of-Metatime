# HARDWARE_AND_QE_METRIC

Status: canonical working note  
Scope:
- hardware profiles by execution layer
- corrected quality/energy metric
- removal of redundant \\(\Theta,\mathcal H\\) double counting
- layered efficiency definition

---

## 1. Hardware profiles

There are three execution layers with three distinct hardware profiles.

### 1.1 Repository / orbital / relational layer

This is the lightest layer.

Typical components:
- Python runtime
- relational / holonomy / orbital passes
- tests and report generation
- extraction of imports / README mesh / AGENT mesh / manifests

Operational target:
- CPU host is sufficient
- no hard realtime requirement
- suitable for simulations, diagnostics, and batch orchestration

Current policy:
- do **not** claim GPU / VRAM minimums unless they are explicitly benchmarked in the repo

### 1.2 Tensor engine / realtime field simulation

This layer is substantially heavier.

Expected characteristics:
- synchronous image acquisition
- framewise gradient estimation
- multi-channel phase and memory tracking
- live tensor assembly
- collapse / coherence alerts
- fast visualization

The documents already point toward:
- Python or Julia backend
- NumPy / ArrayFire / GPU acceleration
- FFT support such as pyFFTW / CuPy
- optional TensorFlow or JAX
- realtime optimizations such as pre-allocated matrices and parallel collapse detection

Operational target:
- offline / batch possible on CPU
- true 3D realtime field simulation is a GPU task

### 1.3 Hybrid symbolic / BraidOS layer

This layer is hardware-functional rather than brand-specific.

Expected subsystems:
- symbolic sensors (breath, voice, gesture, contradiction detection)
- phase register
- glyph executor
- return scheduler
- persistent symbolic store
- feedback devices (light, vibration, sound, cue layer)

Hard functional thresholds already present in the project material:
- sensor latency: **< 50 ms**
- phase sampling frequency: **>= 10 Hz**

Operational target:
- small host / embedded-compatible system
- stable memory log
- low-latency input/output chain

---

## 2. Corrected quality metric

Previous informal forms mixed \\(\Theta\\) and \\(\mathcal H\\) directly even when

\\[
\Theta = 1 - \frac{\mathcal H}{\mathcal H_{\max}}
\\]

was already assumed.

That double-counts the same coherence structure.

### 2.1 Canonical quality metric for repo/orbital layer

Use:

\\[
Q_{\text{repo}}
=
 w_\Theta \, \Theta
+ w_C \, \Delta C
- w_D \, D_{\mathrm{sem}}
\\]

where:
- \\(\Theta\\) = truth / coherence scalar
- \\(\Delta C = C_{after}-C_{before}\\) = change of coherence loop quality
- \\(D_{\mathrm{sem}}\\) = semantic distortion

This keeps the quality function non-redundant.

### 2.2 Canonical quality metric for tensor/realtime layer

\\[
Q_{\text{tensor}}
=
 u_1\,A_{\text{collapse}}
+u_2\,A_{\text{return}}
+u_3\,Q_{\text{field}}
\\]

Interpretation:
- collapse prediction quality
- return likelihood / return pointer accuracy
- field coherence quality

### 2.3 Canonical quality metric for hybrid symbolic layer

\\[
Q_{\text{hyb}}
=
 v_1\,R_{\text{loop}}
+v_2\,F_{\text{rec}}
+v_3\,S_{\text{return}}
\\]

Interpretation:
- loop closure rate
- recursion fidelity
- return stability

---

## 3. Layered energy metric

Energy must be defined per execution layer, not as one undifferentiated global scalar.

### 3.1 Repository / orbital layer

\\[
E_{\text{repo}}
=
\alpha_t\, t_{\text{CPU}}
+\alpha_s\, N_{\text{steps}}
+\alpha_m\, M_{\text{mem}}
\\]

Interpretation:
- CPU time
- number of simulation / update steps
- memory load

### 3.2 Tensor / realtime layer

\\[
E_{\text{tensor}}
=
\beta_A\,A_{\text{total}}
+\beta_l\,L_{\text{latency}}
+\beta_g\,G_{\text{load}}
\\]

Interpretation:
- total field activity
- wall-clock latency
- GPU / system load

### 3.3 Hybrid symbolic layer

\\[
E_{\text{hyb}}
=
\gamma_p\,P_{\text{proc}}
+\gamma_a\,A_{\text{act}}
+\gamma_l\,L_{\text{sensor}}
\\]

Interpretation:
- processing cost
- actuation cost
- sensor latency cost

---

## 4. Quality / energy efficiency

Define efficiency by layer:

\\[
\eta_{Q/E}^{(k)} = \frac{Q_k}{E_k + \varepsilon}
\\]

for

\\[
k \in \{\text{repo},\text{tensor},\text{hyb}\}
\\]

A global efficiency can then be defined as

\\[
\eta_{\text{global}} = \sum_k \omega_k \, \eta_{Q/E}^{(k)}
\\]

with layer weights \\(\omega_k\\).

---

## 5. Practical interpretation

### Current safest operational regime

For the project in its present form:
- repository / orbital layer is already deployable on CPU
- tensor engine remains a research / high-performance target
- hybrid symbolic layer is a latency-constrained systems problem

### Current tuning objective

The canonical tuning target is not a single raw metric but the joint regime:
- high \\(Q_{\text{repo}}\\)
- acceptable \\(E_{\text{repo}}\\)
- low closure defect
- nontrivial positive global chirality
- acceptable wall-clock cost

---

## 6. Canonical result

The repository now has a corrected, non-redundant metric family:
- quality by execution layer
- energy by execution layer
- efficiency by execution layer
- optional global weighted efficiency

This is the correct base for future report schemas, Monte Carlo targets, and control-panel dashboards.
