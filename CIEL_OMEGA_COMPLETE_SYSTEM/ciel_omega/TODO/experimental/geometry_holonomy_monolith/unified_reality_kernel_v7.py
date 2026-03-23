#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIEL/0 HYBRID MONOLITH (full-tensor Kähler + CI-ready)
- Dodano FullTensorKahler: dyskretna tensorowa aproksymacja Kähler (metryka, Γ, krzywizna)
- Parametr use_full_tensor_kahler w HybridMonolith
- Zachowano backward compatibility z lekkim FullKahler adapterem
"""
from dataclasses import dataclass, field
from typing import Tuple, List, Dict, Any, Optional
import numpy as np
import json
import time

# -------------------------
# SETTINGS
# -------------------------
DEFAULT_GRID = (8, 8)
RNG_SEED = 42
np.random.seed(RNG_SEED)

# -------------------------
# EMERGENT CONSTANTS
# -------------------------
@dataclass
class EmergentConstants:
    alpha_c: float = 0.474812
    beta_s: float = 0.856234
    gamma_t: float = 0.345123
    Lambda: float = 0.474812
    Gamma_max: float = 0.751234
    Epsilon: float = 0.90
    hbar_eff: float = 0.892345

EM = EmergentConstants()

# -------------------------
# CollatzEngine (stable)
# -------------------------
class CollatzEngine:
    def __init__(self, cache_size: int = 200000):
        self.cache_size = cache_size
        self.cache = np.full(self.cache_size, -1, dtype=np.int32)
        self.cache[1] = 1

    def length(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < self.cache_size and self.cache[n] != -1:
            return int(self.cache[n])
        stack = []
        steps = 0
        limit_steps = 5000
        original = n
        while n != 1 and steps < limit_steps:
            if n < self.cache_size and self.cache[n] != -1:
                steps += int(self.cache[n]) - 1
                break
            stack.append(n)
            if (n & 1) == 0:
                n //= 2
            else:
                n = 3 * n + 1
            steps += 1
        length = steps if n == 1 else steps
        for i, val in enumerate(reversed(stack), start=1):
            idx = stack[-i]
            if idx < self.cache_size:
                self.cache[idx] = length - (i - 1)
        return int(length)

# -------------------------
# DeterministicTopology
# -------------------------
@dataclass
class DeterministicTopology:
    shape: Tuple[int, int]
    local_radius: int = 1
    long_range_density: float = 0.01

    def __post_init__(self):
        self.rows, self.cols = self.shape
        self.N = self.rows * self.cols
        self.adjacency = np.zeros((self.N, self.N), dtype=np.float64)
        self._build_adjacency()

    def _build_adjacency(self):
        rng = np.random.RandomState(RNG_SEED)
        for i in range(self.N):
            r, c = divmod(i, self.cols)
            if r > 0:
                j = (r-1) * self.cols + c
                self.adjacency[i, j] = 1.0; self.adjacency[j, i] = 1.0
            if r < self.rows - 1:
                j = (r+1) * self.cols + c
                self.adjacency[i, j] = 1.0; self.adjacency[j, i] = 1.0
            if c > 0:
                j = r * self.cols + (c-1)
                self.adjacency[i, j] = 1.0; self.adjacency[j, i] = 1.0
            if c < self.cols - 1:
                j = r * self.cols + (c+1)
                self.adjacency[i, j] = 1.0; self.adjacency[j, i] = 1.0
        n_long = max(1, int(self.long_range_density * np.sqrt(self.N)))
        for i in range(self.N):
            rng.seed(RNG_SEED + i)
            candidates = np.arange(self.N, dtype=int)
            rng.shuffle(candidates)
            added = 0
            for j in candidates:
                if added >= n_long: break
                if j == i or self.adjacency[i, j] > 0: continue
                ri, ci = divmod(i, self.cols); rj, cj = divmod(j, self.cols)
                dist = np.hypot(ri - rj, ci - cj)
                weight = np.exp(-dist / max(self.rows, self.cols))
                self.adjacency[i, j] = weight; self.adjacency[j, i] = weight
                added += 1

# -------------------------
# PersistentMemory + Kuramoto
# -------------------------
@dataclass
class PersistentMemory:
    shape: Tuple[int, int] = DEFAULT_GRID
    base_freq: float = 7.83
    coupling_strength: float = 0.15
    memory_strength: float = 0.5

    def __post_init__(self):
        self.rows, self.cols = self.shape
        self.N = self.rows * self.cols
        self.collatz = CollatzEngine()
        self.topology = DeterministicTopology(self.shape)
        self.phases = self._init_phases()
        self.frequencies = self._init_frequencies()
        self.memory_weights = np.zeros((self.N, self.N), dtype=float)
        self.stored_patterns: List[np.ndarray] = []
        self.coherence_history: List[float] = []
        self.step_count = 0
        self.coherence_history.append(self.compute_coherence())

    def _init_phases(self):
        phases = np.zeros(self.N, dtype=float)
        for i in range(self.N):
            clen = self.collatz.length(i + 1001)
            phases[i] = 2 * np.pi * (clen % 100) / 100.0
        return phases

    def _init_frequencies(self):
        base_omega = 2 * np.pi * self.base_freq
        freqs = base_omega * np.ones(self.N, dtype=float)
        for i in range(self.N):
            variation = 0.1 * np.sin(2 * np.pi * i / max(1, self.N))
            freqs[i] *= (1 + variation)
        return freqs

    def compute_coherence(self) -> float:
        z = np.mean(np.exp(1j * self.phases))
        return float(np.abs(z))

    def kuramoto_step(self, dt: float = 0.01):
        new_phases = self.phases.copy()
        for i in range(self.N):
            coupling = 0.0; total_weight = 0.0
            row = self.topology.adjacency[i]
            nz = row > 0
            if np.any(nz):
                phase_diffs = self.phases[nz] - self.phases[i]
                weights = row[nz]
                coupling = np.sum(weights * np.sin(phase_diffs)); total_weight = np.sum(weights)
            mem_row = self.memory_weights[i]
            if np.any(mem_row):
                mem_nz = mem_row != 0
                mem_phase_diffs = self.phases[mem_nz] - self.phases[i]
                coupling += np.sum(mem_row[mem_nz] * np.sin(mem_phase_diffs)); total_weight += np.sum(mem_row[mem_nz])
            if total_weight > 0:
                coupling /= total_weight
            dtheta = self.frequencies[i] + self.coupling_strength * coupling
            new_phases[i] = (self.phases[i] + dtheta * dt) % (2 * np.pi)
        self.phases = new_phases
        self.step_count += 1
        coh = self.compute_coherence(); self.coherence_history.append(coh)

    def write(self, pattern: np.ndarray):
        if pattern.shape != self.shape:
            raise ValueError("Pattern shape mismatch")
        flat = pattern.flatten()
        for i in range(self.N):
            for j in range(self.N):
                if i != j and self.topology.adjacency[i, j] > 0:
                    self.memory_weights[i, j] += self.memory_strength * (flat[i] * flat[j])
        self.stored_patterns.append(pattern.copy()); 
        if len(self.stored_patterns) > 40: self.stored_patterns.pop(0)

    def read(self) -> Tuple[np.ndarray, float]:
        if not self.stored_patterns:
            return np.zeros(self.shape), 0.0
        recalled = np.zeros(self.N, dtype=float); total_weight = 0.0
        for idx, p in enumerate(reversed(self.stored_patterns)):
            w = 0.6 ** idx
            recalled += w * p.flatten(); total_weight += w
        if total_weight > 0: recalled /= total_weight
        recalled = recalled.reshape(self.shape)
        confidence = min(1.0, len(self.stored_patterns) / 10.0) * (self.coherence_history[-1] if self.coherence_history else 0.0)
        return recalled, float(confidence)

# -------------------------
# FullTensorKahler: discrete tensor approx
# -------------------------
class FullTensorKahler:
    """
    Discrete tensor approximation of Kähler geometry on nodes.
    - node coordinates come from phases mapped to unit circle (x=cos θ, y=sin θ)
    - K potential per node built from emergent constants and neighbor couplings
    - metric diag g_i computed from discrete laplacian of K (regularised to >0)
    - connection proxies Γ_i_jk stored sparsely (here as small arrays)
    - curvature scalar per node as discrete Laplacian(log g)
    """
    def __init__(self, memory: PersistentMemory, emergent: EmergentConstants = EM):
        self.memory = memory; self.em = emergent
        self.N = memory.N
        self.rows = memory.rows; self.cols = memory.cols
        self.K = np.zeros(self.N, dtype=float)
        self.metric = np.ones(self.N, dtype=float)
        self.Gamma = np.zeros((self.N, 4), dtype=float)  # proxy: 4-directions per node
        self.curvature = np.zeros(self.N, dtype=float)
        self._compute_all()

    def _node_coords(self):
        theta = self.memory.phases
        x = np.cos(theta); y = np.sin(theta)
        return x, y

    def _compute_potential(self):
        x, y = self._node_coords()
        amp2 = x**2 + y**2
        adj = self.memory.topology.adjacency
        neighbor_influence = adj.dot(amp2) / np.maximum(np.sum(adj, axis=1), 1.0)
        self.K = self.em.alpha_c * amp2 + 0.5 * self.em.beta_s * amp2**2 + 0.1 * neighbor_influence

    def _compute_metric(self):
        # discrete Laplacian of K as proxy for second derivative
        adj = self.memory.topology.adjacency
        deg = np.sum(adj, axis=1)
        lap = deg * self.K - adj.dot(self.K)
        g = np.abs(lap) + 1e-6
        # regularize and smooth
        self.metric = 0.5 * (self.metric + (g / (np.mean(g) + 1e-12)))
        self.metric = np.maximum(self.metric, 1e-8)

    def _compute_connection_proxies(self):
        # For each node, compute directional differences (up,down,left,right) as proxy Γ
        for idx in range(self.N):
            r, c = divmod(idx, self.cols)
            vals = []
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                rr = r + dr; cc = c + dc
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    j = rr * self.cols + cc
                    vals.append(self.metric[j] - self.metric[idx])
                else:
                    vals.append(0.0)
            self.Gamma[idx] = np.array(vals)

    def _compute_curvature(self):
        # curvature scalar approx = discrete Laplacian of log(metric)
        logg = np.log(self.metric + 1e-12)
        adj = self.memory.topology.adjacency
        deg = np.sum(adj, axis=1)
        lap_logg = deg * logg - adj.dot(logg)
        self.curvature = lap_logg

    def _compute_all(self):
        self._compute_potential(); self._compute_metric()
        self._compute_connection_proxies(); self._compute_curvature()

    def update(self):
        self._compute_all()

    def compute_chern_like_form(self):
        # discrete surrogate: integrate curvature over nodes -> scalar
        return float(np.sum(self.curvature)) / float(max(1, self.N))

# -------------------------
# KahlerBundleAdapter (supports full_tensor)
# -------------------------
@dataclass
class KahlerBundleAdapter:
    memory: PersistentMemory
    use_full_tensor: bool = False

    def __post_init__(self):
        self.N = self.memory.N
        self.A_time = np.zeros(self.N, dtype=complex)
        self.holonomy_memory: List[complex] = []
        self.berry_phases: List[float] = []
        self.full_tensor: Optional[FullTensorKahler] = FullTensorKahler(self.memory) if self.use_full_tensor else None
        self.prev_phases = self.memory.phases.copy()

    def update_connection(self, dt: float = 0.01):
        if self.use_full_tensor and self.full_tensor is not None:
            self.full_tensor.update()
            # map discrete connection proxy to complex one-form (time-like)
            self.A_time = -0.1j * (self.full_tensor.Gamma.sum(axis=1).astype(np.complex128))
            return
        dtheta = (self.memory.phases - self.prev_phases) / max(dt, 1e-12)
        self.prev_phases = self.memory.phases.copy()
        self.A_time = -dtheta.astype(np.complex128)

    def parallel_transport_along_nodes(self, node_path: List[int], dt: float = 0.01):
        U = 1.0 + 0j
        for n in node_path:
            U *= (1.0 + self.A_time[n] * dt)
        self.holonomy_memory.append(U); phi = np.angle(U); self.berry_phases.append(phi)
        return U, phi

# -------------------------
# HybridMonolith (with full tensor option)
# -------------------------
@dataclass
class HybridMonolith:
    shape: Tuple[int, int] = DEFAULT_GRID
    use_topology: bool = True
    use_ethics: bool = True
    use_full_tensor_kahler: bool = False
    dt: float = 0.01

    def __post_init__(self):
        self.memory = PersistentMemory(self.shape)
        self.bundle = KahlerBundleAdapter(self.memory, use_full_tensor=self.use_full_tensor_kahler)
        self.history: Dict[str, List[Any]] = {'coherence': [self.memory.coherence_history[-1]], 'berry_phases': [], 'writes': []}
        self.ethical_violations = 0; self.life_integrity = 1.0

    def enforce_ethics(self):
        if not self.use_ethics: return
        coh = self.memory.coherence_history[-1]
        if coh < EM.Epsilon:
            mean_phase = np.angle(np.mean(np.exp(1j * self.memory.phases)))
            alpha = 0.2
            delta = ((mean_phase - self.memory.phases + np.pi) % (2*np.pi)) - np.pi
            self.memory.phases = (self.memory.phases + alpha * delta) % (2*np.pi)
            self.ethical_violations += 1; self.life_integrity *= 0.995

    def step(self):
        self.memory.kuramoto_step(dt=self.dt)
        if self.use_topology:
            self.bundle.update_connection(dt=self.dt)
            path = list(range(min(8, self.memory.N)))
            U, phi = self.bundle.parallel_transport_along_nodes(path, dt=self.dt)
            self.history['berry_phases'].append(phi)
        self.enforce_ethics()
        self.history['coherence'].append(self.memory.coherence_history[-1])

    def write_pattern(self, pattern: np.ndarray):
        self.memory.write(pattern); self.history['writes'].append(time.time())

    def run(self, steps: int = 200, log_every: int = 50):
        for t in range(steps):
            self.step()
            if (t % log_every) == 0:
                coh = self.history['coherence'][-1]
                print(f"[Step {t:4d}] coherence={coh:.4f} violations={self.ethical_violations}")

    def recall(self):
        return self.memory.read()

    def summary(self) -> Dict[str, Any]:
        return {'final_coherence': self.history['coherence'][-1], 'berry_mean': float(np.mean(self.history['berry_phases'])) if self.history['berry_phases'] else 0.0, 'eth_violations': self.ethical_violations, 'life_integrity': self.life_integrity, 'writes': len(self.history['writes'])}

# -------------------------
# Demo + entrypoint
# -------------------------
def demo_and_validation(use_full_tensor: bool = False):
    print("=== HYBRID MONOLITH DEMO / VALIDATION (full tensor kahler option) ===")
    mon = HybridMonolith(shape=(8, 8), use_topology=True, use_ethics=True, use_full_tensor_kahler=use_full_tensor, dt=0.02)
    pattern = np.zeros((8, 8), dtype=float); pattern[2:5, 2:5] = 1.0
    mon.write_pattern(pattern)
    mon.run(steps=200, log_every=100)
    recalled, confidence = mon.recall(); corr = 0.0
    if np.std(recalled) > 1e-12 and np.std(pattern) > 1e-12:
        corr = float(np.corrcoef(pattern.flatten(), recalled.flatten())[0, 1])
    s = mon.summary()
    print("\n--- SUMMARY ---")
    print(f"Final coherence: {s['final_coherence']:.4f}")
    print(f"Berry mean phase: {s['berry_mean']:.6f}")
    print(f"Ethical violations: {s['eth_violations']}")
    print(f"Life integrity: {s['life_integrity']:.6f}")
    print(f"Recall corr: {corr:.4f}, confidence: {confidence:.4f}")
    out = {"final_coherence": s['final_coherence'], "berry_mean": s['berry_mean'], "eth_violations": s['eth_violations'], "life_integrity": s['life_integrity'], "recall_corr": corr, "recall_confidence": confidence, "use_full_tensor": use_full_tensor}
    with open("hybrid_monolith_results.json", "w") as f: json.dump(out, f, indent=2)
    print("Results saved -> hybrid_monolith_results.json")

if __name__ == "__main__":
    demo_and_validation(use_full_tensor=False)