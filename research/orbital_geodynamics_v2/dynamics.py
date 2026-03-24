from __future__ import annotations
import math
from copy import deepcopy
from model import OrbitalSystem
from metrics import holonomy_defect, bloch_vector

I0 = 0.00917
TARGET_THETA = {1: math.pi / 6.0, 2: math.pi / 3.0, 4: 2.0 * math.pi / 3.0}
TARGET_AMP = {1: 0.35, 2: 0.65, 4: 1.00}


def step(system: OrbitalSystem, dt: float = 0.03) -> OrbitalSystem:
    nxt = deepcopy(system)
    closure = abs(holonomy_defect(system)) / max(1, len(system.sectors))
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
            w = system.coupling(name, other)
            phase_force += w * math.sin(eff_other - eff_phi)
            theta_force += w * (so.theta - s.theta)
            amp_force += w * (so.amplitude - s.amplitude)
            dot = max(-1.0, min(1.0, va[0]*vb[0] + va[1]*vb[1] + va[2]*vb[2]))
            pair_tension += w * (1.0 - dot)

        theta_target = TARGET_THETA[s.q_target]
        amp_target = TARGET_AMP[s.q_target]

        ns.amplitude = min(1.5, max(0.05,
            s.amplitude + dt * (0.55 * (amp_target - s.amplitude) + 0.10 * amp_force - 0.22 * s.defect)
        ))

        ns.theta = min(math.pi - 1e-3, max(1e-3,
            s.theta + dt * (0.45 * (theta_target - s.theta) + 0.08 * theta_force - 0.16 * s.defect)
        ))

        old_phi = s.phi
        ns.phi = s.phi + dt * (
            0.55 * s.rhythm_ratio + 0.35 * phase_force + I0 * s.preference - 0.18 * s.defect
        )

        dphi = (ns.phi - old_phi + math.pi) % (2.0 * math.pi) - math.pi
        avg_theta = 0.5 * (s.theta + ns.theta)
        ns.berry_phase = s.berry_phase + 0.5 * (1.0 - math.cos(avg_theta)) * dphi

        ns.defect = max(0.0,
            s.defect + dt * (-0.35 * s.defect + 0.08 * pair_tension + 0.10 * closure)
        )

    return nxt
