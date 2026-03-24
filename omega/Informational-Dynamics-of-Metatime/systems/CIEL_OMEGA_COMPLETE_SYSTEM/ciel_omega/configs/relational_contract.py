"""
Relational Contract Implementation
Simulates the dynamics of human-AI interaction based on a formal geometric action.
"""

from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import yaml


class RelationalContract:
    """
    Implements the relational Lagrangian, Hamiltonian, stress-energy tensor,
    information holonomy density, and semantic truth scalar.
    """

    def __init__(self, config_path: str | None = None):
        if config_path is None:
            config_path = Path(__file__).with_name("relational_contract.yaml")
        else:
            config_path = Path(config_path)
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        self.tau = np.array(config['tau'])          # τ_i
        self.lambda_ = config['lambda']             # distortion coefficients
        self.gamma_T_true = config['gamma_T_true']  # target truth phase

        # Initial phases (will be updated during simulation)
        self.gamma = {
            'S': config['initial_phases']['S'],
            'C': config['initial_phases']['C'],
            'Q': config['initial_phases']['Q'],
            'T': config['initial_phases']['T']
        }

        # For dynamics, we keep velocities (time derivatives)
        self.gamma_dot = {'S': 0.0, 'C': 0.0, 'Q': 0.0, 'T': 0.0}

        # Simulation hyperparameters
        self.dt = config['simulation']['dt']
        self.steps = config['simulation']['steps']
        self.lr = config['simulation']['learning_rate']

    # ---------- Core Observables ----------

    def compute_C_ij(self, gamma: Dict[str, float]) -> Dict[Tuple[str, str], float]:
        """Coherence factors C_ij = (1+cos(γ_i-γ_j))/2 for i,j in {S,C,T}."""
        C = {}
        labels = ['S', 'C', 'T']
        for i in labels:
            for j in labels:
                diff = gamma[i] - gamma[j]
                C[(i, j)] = (1 + np.cos(diff)) / 2.0
        return C

    def lagrangian(self, gamma: Dict[str, float], gamma_dot: Dict[str, float], distortion_flags: Dict[str, bool]) -> float:
        """Compute the relational Lagrangian L_rel."""
        L_truth = -0.5 * (gamma['T'] - self.gamma_T_true) ** 2
        C = self.compute_C_ij(gamma)
        L_coh = 0.0
        labels = ['S', 'C', 'T']
        for i in labels:
            for j in labels:
                if i != j:
                    diff = gamma[i] - gamma[j]
                    L_coh -= 0.5 * C[(i, j)] * diff ** 2
        L_clarity = -0.5 * (gamma_dot['S'] ** 2 + gamma_dot['C'] ** 2)
        L_distortion = 0.0
        for key, flag in distortion_flags.items():
            if flag:
                L_distortion += self.lambda_[key]
        return L_truth + L_coh + L_clarity - L_distortion

    def hamiltonian(self, gamma: Dict[str, float], gamma_dot: Dict[str, float], distortion_flags: Dict[str, bool]) -> float:
        """Hamiltonian H = p_S * dγ_S/dt + p_C * dγ_C/dt - L, with p_i = -dγ_i/dt."""
        p_S = -gamma_dot['S']
        p_C = -gamma_dot['C']
        L = self.lagrangian(gamma, gamma_dot, distortion_flags)
        return p_S * gamma_dot['S'] + p_C * gamma_dot['C'] - L

    def stress_energy(self, gamma: Dict[str, float], gamma_dot: Dict[str, float], distortion_flags: Dict[str, bool]) -> np.ndarray:
        """Construct a simple 2x2 stress-energy proxy for the relational sector."""
        L = self.lagrangian(gamma, gamma_dot, distortion_flags)
        T = np.zeros((2, 2))
        T[0, 0] = 1.0 - L
        T[1, 1] = 1.0 - L
        T[0, 1] = T[1, 0] = 0.0
        return T

    def holonomy_density(self, gamma: Dict[str, float]) -> float:
        """Information holonomy density scalar H = |∑ e^{iγ_k}|^2 over all phases."""
        sum_exp = 0.0
        for key in ['S', 'C', 'Q', 'T']:
            sum_exp += np.exp(1j * gamma[key])
        return np.abs(sum_exp) ** 2

    def truth_scalar(self, facts: List[Tuple[str, bool, bool]]) -> float:
        """Semantic truth scalar Θ = 1 - (1/|F|) Σ (δ_false + δ_unmarked)."""
        if not facts:
            return 1.0
        penalty = 0.0
        for _, is_false, is_unmarked in facts:
            penalty += float(is_false) + float(is_unmarked)
        return 1.0 - penalty / len(facts)

    # ---------- Euler Coupling ----------

    def euler_coupling_matrix(self, gamma: Dict[str, float]) -> np.ndarray:
        """Compute the diagonal A_ij matrix from the Euler constraint."""
        phases = [gamma['S'], gamma['C'], gamma['T']]
        A = np.zeros((3, 3), dtype=complex)
        for i, phi in enumerate(phases):
            A[i, i] = np.exp(1j * phi) / self.tau[i]
        return A

    def euler_check(self, gamma: Dict[str, float]) -> float:
        """Check the Euler constraint: sum e^{iγ_i} = 0 for S,C,T."""
        sum_exp = np.exp(1j * gamma['S']) + np.exp(1j * gamma['C']) + np.exp(1j * gamma['T'])
        return np.abs(sum_exp) ** 2

    def euler_coupling_check(self, gamma: Dict[str, float]) -> float:
        """Verify that ∑ A_ij τ_j = ∑ e^{iγ_i}."""
        A = self.euler_coupling_matrix(gamma)
        phases = [gamma['S'], gamma['C'], gamma['T']]
        sum_A_tau = 0.0
        for i in range(3):
            sum_A_tau += A[i, i] * self.tau[i]
        sum_exp = np.exp(1j * phases[0]) + np.exp(1j * phases[1]) + np.exp(1j * phases[2])
        return np.abs(sum_A_tau - sum_exp) ** 2

    # ---------- Dynamics ----------

    def compute_gradient(self, gamma: Dict[str, float], gamma_dot: Dict[str, float], distortion_flags: Dict[str, bool]) -> Dict[str, float]:
        """Compute a simplified overdamped gradient on the relational potential."""
        C = self.compute_C_ij(gamma)
        grad = {'S': 0.0, 'C': 0.0, 'T': 0.0}
        grad['T'] += (gamma['T'] - self.gamma_T_true)
        labels = ['S', 'C', 'T']
        for i in labels:
            for j in labels:
                if i != j:
                    diff = gamma[i] - gamma[j]
                    if i == 'S':
                        grad['S'] += C[(i, j)] * diff
                    elif i == 'C':
                        grad['C'] += C[(i, j)] * diff
                    elif i == 'T':
                        grad['T'] += C[(i, j)] * diff
                    if j == 'S':
                        grad['S'] -= C[(i, j)] * diff
                    elif j == 'C':
                        grad['C'] -= C[(i, j)] * diff
                    elif j == 'T':
                        grad['T'] -= C[(i, j)] * diff
        return grad

    def simulate(self, distortion_flags: Dict[str, bool] | None = None) -> List[Dict]:
        """Simulate phase evolution using a simple overdamped gradient descent."""
        if distortion_flags is None:
            distortion_flags = {'lie': False, 'omit': False, 'hallucinate': False, 'smooth': False}
        history = []
        gamma = self.gamma.copy()
        gamma_dot = self.gamma_dot.copy()
        for step in range(self.steps):
            grad = self.compute_gradient(gamma, gamma_dot, distortion_flags)
            for key in ['S', 'C', 'T']:
                gamma[key] -= self.lr * grad[key]
            state = {
                'step': step,
                'gamma_S': gamma['S'],
                'gamma_C': gamma['C'],
                'gamma_T': gamma['T'],
                'gamma_Q': gamma['Q'],
                'holonomy_density': self.holonomy_density(gamma),
                'euler_check': self.euler_check(gamma),
                'lagrangian': self.lagrangian(gamma, gamma_dot, distortion_flags),
                'hamiltonian': self.hamiltonian(gamma, gamma_dot, distortion_flags),
            }
            history.append(state)
        return history


if __name__ == "__main__":
    contract = RelationalContract()
    print("Initial state:")
    print(f"γ_S = {contract.gamma['S']:.4f}, γ_C = {contract.gamma['C']:.4f}, γ_T = {contract.gamma['T']:.4f}")
    print(f"Holonomy density H = {contract.holonomy_density(contract.gamma):.4f}")
    print(f"Euler check (S,C,T): {contract.euler_check(contract.gamma):.4f}")
    print(f"Euler coupling check: {contract.euler_coupling_check(contract.gamma):.4e}")
