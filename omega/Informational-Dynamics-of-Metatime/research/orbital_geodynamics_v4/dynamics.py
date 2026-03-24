from __future__ import annotations
import math
from copy import deepcopy
from model import OrbitalSystem
from metrics import holonomy_defect, bloch_vector, A_ij, closure_residuals, closure_details

I0 = 0.00917
TARGET_THETA = {1: math.pi / 6.0, 2: math.pi / 3.0, 4: 2.0 * math.pi / 3.0}
TARGET_AMP = {1: 0.35, 2: 0.65, 4: 1.00}


def tau_gradient(system: OrbitalSystem):
    names = system.names()
    lhs_map = {}
    rhs_map = {}
    for i in names:
        lhs = 0j
        for j in names:
            lhs += A_ij(system, i, j) * system.sectors[j].tau
        lhs_map[i] = lhs
        rhs_map[i] = complex(math.cos(system.sectors[i].phi + system.sectors[i].berry_phase), math.sin(system.sectors[i].phi + system.sectors[i].berry_phase))
    grads = {j: 0.0 for j in names}
    for j in names:
        g = 0.0
        for i in names:
            resid = lhs_map[i] - rhs_map[i]
            g += 2.0 * (resid.conjugate() * A_ij(system, i, j)).real
        grads[j] = g
    return grads


def step(system: OrbitalSystem, dt: float = 0.025, tau_eta: float = 0.01, tau_reg: float = 0.00) -> OrbitalSystem:
    nxt = deepcopy(system)
    closure = abs(holonomy_defect(system)) / max(1, len(system.sectors))
    residuals = closure_residuals(system)
    details = closure_details(system)
    tau_base = {name: s.tau for name, s in system.sectors.items()}
    names = system.names()

    for name in names:
        s = system.sectors[name]
        ns = nxt.sectors[name]

        phase_force = 0.0
        theta_force = 0.0
        amp_force = 0.0
        pair_tension = 0.0

        eff_phi = s.phi + s.berry_phase
        va = bloch_vector(s.theta, eff_phi)

        for other in names:
            if other == name:
                continue
            so = system.sectors[other]
            eff_other = so.phi + so.berry_phase
            vb = bloch_vector(so.theta, eff_other)
            Aab = A_ij(system, name, other)
            amp = abs(Aab)
            phase = math.atan2(Aab.imag, Aab.real) if Aab != 0 else 0.0
            phase_force += amp * math.sin((eff_other - eff_phi) + phase)
            theta_force += amp * (so.theta - s.theta)
            amp_force += amp * (so.amplitude - s.amplitude)
            dot = max(-1.0, min(1.0, va[0]*vb[0] + va[1]*vb[1] + va[2]*vb[2]))
            pair_tension += amp * (1.0 - dot)

        theta_target = TARGET_THETA[s.q_target]
        amp_target = TARGET_AMP[s.q_target]
        closure_local = residuals[name]

        ns.amplitude = min(1.35, max(0.05,
            s.amplitude + dt * (
                0.42 * (amp_target - s.amplitude)
                + 0.07 * amp_force
                - 0.18 * s.defect
                - 0.10 * closure_local
            )
        ))

        ns.theta = min(math.pi - 1e-3, max(1e-3,
            s.theta + dt * (
                0.30 * (theta_target - s.theta)
                + 0.06 * theta_force
                - 0.14 * s.defect
                - 0.05 * closure_local
            )
        ))

        old_phi = s.phi
        ns.phi = s.phi + dt * (
            0.36 * s.rhythm_ratio
            + 0.22 * phase_force
            + I0 * s.preference
            - 0.16 * s.defect
            - 0.12 * closure_local
        )

        dphi = (ns.phi - old_phi + math.pi) % (2.0 * math.pi) - math.pi
        avg_theta = 0.5 * (s.theta + ns.theta)
        ns.berry_phase = s.berry_phase + 0.5 * (1.0 - math.cos(avg_theta)) * dphi

        ns.defect = max(0.0,
            s.defect + dt * (
                -0.42 * s.defect
                + 0.05 * pair_tension
                + 0.08 * closure
                + 0.18 * closure_local
            )
        )

    # adaptive tau relaxation after geometric update
    grads = tau_gradient(system)
    for name in names:
        s = system.sectors[name]
        ns = nxt.sectors[name]
        ns.tau = min(0.8, max(0.12,
            s.tau - tau_eta * grads[name] - tau_reg * dt * (s.tau - tau_base[name])
        ))

    return nxt
