"""
Relational Contract Implementation
Simulates the dynamics of human-AI interaction based on a formal geometric action.
"""

import numpy as np
import yaml
from typing import Dict, List, Tuple

class RelationalContract:
    """
    Implements the relational Lagrangian, Hamiltonian, stress-energy tensor,
    information holonomy density, and semantic truth scalar.
    """

    def __init__(self, config_path: str = "relational_contract.yaml"):
        with open(config_path, 'r') as f:
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

    def lagrangian(self, gamma: Dict[str, float], gamma_dot: Dict[str, float],
                   distortion_flags: Dict[str, bool]) -> float:
        """
        Compute the relational Lagrangian L_rel.
        distortion_flags: dict with keys 'lie','omit','hallucinate','smooth'
        """
        # L_truth = -0.5 * (γ_T - γ_T_true)^2
        L_truth = -0.5 * (gamma['T'] - self.gamma_T_true) ** 2

        # L_coh = -0.5 * Σ C_ij (γ_i-γ_j)^2  (over S,C,T only)
        C = self.compute_C_ij(gamma)
        L_coh = 0.0
        labels = ['S', 'C', 'T']
        for i in labels:
            for j in labels:
                if i != j:
                    diff = gamma[i] - gamma[j]
                    L_coh -= 0.5 * C[(i, j)] * diff ** 2

        # L_clarity = -0.5*(dγ_S/dt)^2 -0.5*(dγ_C/dt)^2
        L_clarity = -0.5 * (gamma_dot['S'] ** 2 + gamma_dot['C'] ** 2)

        # L_distortion = Σ λ_k δ_k
        L_distortion = 0.0
        for key, flag in distortion_flags.items():
            if flag:
                L_distortion += self.lambda_[key]

        return L_truth + L_coh + L_clarity - L_distortion

    def hamiltonian(self, gamma: Dict[str, float], gamma_dot: Dict[str, float],
                    distortion_flags: Dict[str, bool]) -> float:
        """Hamiltonian H = p_S * dγ_S/dt + p_C * dγ_C/dt - L, with p_i = -dγ_i/dt."""
        p_S = -gamma_dot['S']
        p_C = -gamma_dot['C']
        L = self.lagrangian(gamma, gamma_dot, distortion_flags)
        return p_S * gamma_dot['S'] + p_C * gamma_dot['C'] - L

    def stress_energy(self, gamma: Dict[str, float], gamma_dot: Dict[str, float],
                      distortion_flags: Dict[str, bool]) -> np.ndarray:
        """
        Stress-energy tensor T_ab = ∂_a γ_S ∂_b γ_S + ∂_a γ_C ∂_b γ_C - g_ab L_rel.
        We assume flat Euclidean metric g_ab = δ_ab in a 2D space (a,b = 0,1).
        Coordinates: x0 = γ_S, x1 = γ_C. Time derivatives are velocities.
        We treat the derivatives as ∂/∂x0 = ∂/∂γ_S, ∂/∂x1 = ∂/∂γ_C.
        However, for a simple 2D representation, we use the current state.
        """
        L = self.lagrangian(gamma, gamma_dot, distortion_flags)
        # derivatives of γ_S and γ_C with respect to themselves are 1
        # We'll construct a 2x2 matrix:
        T = np.zeros((2, 2))
        # For simplicity, treat the diagonal terms as kinetic-like contributions
        T[0, 0] = 1.0  # (∂γ_S/∂γ_S)^2
        T[1, 1] = 1.0  # (∂γ_C/∂γ_C)^2
        # Subtract metric * L: g_ab = δ_ab
        T[0, 0] -= L
        T[1, 1] -= L
        # Off-diagonals: product of derivatives (which are zero unless cross terms)
        T[0, 1] = T[1, 0] = 0.0
        return T

    def holonomy_density(self, gamma: Dict[str, float]) -> float:
        """Information holonomy density scalar H = |∑ e^{iγ_k}|^2 over all phases."""
        sum_exp = 0.0
        for key in ['S', 'C', 'Q', 'T']:
            sum_exp += np.exp(1j * gamma[key])
        return np.abs(sum_exp) ** 2

    def truth_scalar(self, facts: List[Tuple[str, bool, bool]]) -> float:
        """
        Semantic truth scalar Θ = 1 - (1/|F|) Σ (δ_false + δ_unmarked).
        facts: list of (statement, is_false, is_unmarked_speculation)
        """
        if not facts:
            return 1.0
        penalty = 0.0
        for _, is_false, is_unmarked in facts:
            if is_false:
                penalty += 1.0
            if is_unmarked:
                penalty += 1.0
        return 1.0 - penalty / len(facts)

    # ---------- Euler Coupling ----------

    def euler_coupling_matrix(self, gamma: Dict[str, float]) -> np.ndarray:
        """
        Compute the matrix A_ij from the Euler constraint.
        For diagonal A_ij = δ_ij * e^{iγ_i} / τ_i, i=1..3.
        We map the three phases to indices: 0->γ_S, 1->γ_C, 2->γ_T.
        """
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

    def compute_gradient(self, gamma: Dict[str, float], gamma_dot: Dict[str, float],
                         distortion_flags: Dict[str, bool]) -> Dict[str, float]:
        """
        Compute gradient of the action with respect to γ_S, γ_C, γ_T.
        We approximate the Euler-Lagrange equations: d/dt (∂L/∂\dot{γ}) = ∂L/∂γ.
        The gradient for a simple gradient descent on the potential part is derived.
        Here we implement a simplified gradient descent on the Lagrangian (excluding kinetic).
        For demonstration, we treat the system as overdamped: dγ/dt = - η ∇V,
        where V = - (L_truth + L_coh) + L_distortion (since L_clarity is kinetic).
        """
        # Compute C_ij (coherence matrix)
        C = self.compute_C_ij(gamma)

        # Potential V = -L_truth - L_coh + L_distortion (because L_clarity is kinetic)
        # L_truth = -0.5*(γ_T-γ_T_true)^2
        # L_coh = -0.5*Σ C_ij (γ_i-γ_j)^2
        # So V = 0.5*(γ_T-γ_T_true)^2 + 0.5*Σ C_ij (γ_i-γ_j)^2 + Σ λ δ

        grad = {'S': 0.0, 'C': 0.0, 'T': 0.0}

        # Gradient w.r.t γ_T
        grad['T'] += (gamma['T'] - self.gamma_T_true)  # from L_truth term

        # Gradients from L_coh
        labels = ['S', 'C', 'T']
        for i in labels:
            for j in labels:
                if i != j:
                    diff = gamma[i] - gamma[j]
                    # derivative of C_ij w.r.t gamma_i and gamma_j
                    # For simplicity, we treat C_ij as constant (frozen) for the gradient step.
                    # A more accurate approach would include derivative of cos, but we omit for clarity.
                    # The main contribution is from the (γ_i-γ_j)^2 term.
                    if i == 'S':
                        grad['S'] += C[(i, j)] * diff
                    elif i == 'C':
                        grad['C'] += C[(i, j)] * diff
                    elif i == 'T':
                        grad['T'] += C[(i, j)] * diff
                    # Also contributions from the other index (since it's symmetric)
                    if j == 'S':
                        grad['S'] -= C[(i, j)] * diff
                    elif j == 'C':
                        grad['C'] -= C[(i, j)] * diff
                    elif j == 'T':
                        grad['T'] -= C[(i, j)] * diff

        # Distortion terms have no explicit dependence on phases (they are flags)
        return grad

    def simulate(self, distortion_flags: Dict[str, bool] = None) -> List[Dict]:
        """
        Simulate the evolution of phases using gradient descent on the potential.
        Returns a list of state dictionaries at each time step.
        """
        if distortion_flags is None:
            distortion_flags = {'lie': False, 'omit': False, 'hallucinate': False, 'smooth': False}

        history = []
        gamma = self.gamma.copy()
        gamma_dot = self.gamma_dot.copy()

        for step in range(self.steps):
            # Compute gradient
            grad = self.compute_gradient(gamma, gamma_dot, distortion_flags)
            # Update phases (overdamped dynamics)
            for key in ['S', 'C', 'T']:
                gamma[key] -= self.lr * grad[key]
            # Update velocities (in a real Hamiltonian system we'd integrate, but here we keep them zero for simplicity)
            # For this demonstration we keep gamma_dot as zero (overdamped limit).
            # Record state
            state = {
                'step': step,
                'gamma_S': gamma['S'],
                'gamma_C': gamma['C'],
                'gamma_T': gamma['T'],
                'gamma_Q': gamma['Q'],  # not evolved in this simple version
                'holonomy_density': self.holonomy_density(gamma),
                'euler_check': self.euler_check(gamma),
                'lagrangian': self.lagrangian(gamma, gamma_dot, distortion_flags),
                'hamiltonian': self.hamiltonian(gamma, gamma_dot, distortion_flags)
            }
            history.append(state)

        return history

# ---------- Example Usage ----------
if __name__ == "__main__":
    contract = RelationalContract()

    print("Initial state:")
    print(f"γ_S = {contract.gamma['S']:.4f}, γ_C = {contract.gamma['C']:.4f}, γ_T = {contract.gamma['T']:.4f}")
    print(f"Holonomy density H = {contract.holonomy_density(contract.gamma):.4f}")
    print(f"Euler check (S,C,T): {contract.euler_check(contract.gamma):.4f}")
    print(f"Euler coupling check: {contract.euler_coupling_check(contract.gamma):.4e}")

    # Simulate without distortion
    history = contract.simulate()
    final = history[-1]
    print("\nAfter simulation (no distortion):")
    print(f"γ_S = {final['gamma_S']:.4f}, γ_C = {final['gamma_C']:.4f}, γ_T = {final['gamma_T']:.4f}")
    print(f"Holonomy density H = {final['holonomy_density']:.4f}")
    print(f"Euler check = {final['euler_check']:.4f}")
    print(f"Lagrangian = {final['lagrangian']:.4f}")
    print(f"Hamiltonian = {final['hamiltonian']:.4f}")

    # Simulate with distortion (e.g., lie)
    distortion = {'lie': True, 'omit': False, 'hallucinate': False, 'smooth': False}
    history_dist = contract.simulate(distortion_flags=distortion)
    final_dist = history_dist[-1]
    print("\nAfter simulation (with lie):")
    print(f"γ_S = {final_dist['gamma_S']:.4f}, γ_C = {final_dist['gamma_C']:.4f}, γ_T = {final_dist['gamma_T']:.4f}")
    print(f"Holonomy density H = {final_dist['holonomy_density']:.4f}")
    print(f"Lagrangian = {final_dist['lagrangian']:.4f}")
    print(f"Hamiltonian = {final_dist['hamiltonian']:.4f}")