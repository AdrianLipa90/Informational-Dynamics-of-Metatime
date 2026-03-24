from __future__ import annotations
import cmath
import math
from typing import Dict, Tuple
from model import OrbitalSystem


def bloch_vector(theta: float, phi: float):
    return (
        math.sin(theta) * math.cos(phi),
        math.sin(theta) * math.sin(phi),
        math.cos(theta),
    )


def poincare_radius(theta: float) -> float:
    return math.tanh(math.tan(theta / 2.0))


def poincare_distance(theta_a: float, phi_a: float, theta_b: float, phi_b: float) -> float:
    ra = min(0.999999, abs(poincare_radius(theta_a)))
    rb = min(0.999999, abs(poincare_radius(theta_b)))
    dphi = phi_b - phi_a
    num = ra**2 + rb**2 - 2.0 * ra * rb * math.cos(dphi)
    den = max(1e-12, (1.0 - ra**2) * (1.0 - rb**2))
    arg = 1.0 + 2.0 * num / den
    arg = max(1.0, arg)
    return math.acosh(arg)


def berry_pair_phase(theta_a: float, phi_a: float, theta_b: float, phi_b: float) -> float:
    # small-step pair proxy, antisymmetric by construction
    dphi = (phi_b - phi_a + math.pi) % (2 * math.pi) - math.pi
    avg_theta = 0.5 * (theta_a + theta_b)
    return 0.5 * (1.0 - math.cos(avg_theta)) * dphi


def A_ij(system: OrbitalSystem, a: str, b: str, sigma: float = 0.28, beta: float = 0.9, gamma: float = 0.25) -> complex:
    sa = system.sectors[a]
    sb = system.sectors[b]
    if a == b:
        return 0.0 + 0.0j
    base = system.coupling(a, b)
    if base <= 0.0:
        return 0.0 + 0.0j
    tau_factor = math.exp(-0.5 * (math.log(max(1e-9, sa.tau / sb.tau)) / sigma) ** 2)
    phi_a = sa.phi + sa.berry_phase
    phi_b = sb.phi + sb.berry_phase
    d_ij = poincare_distance(sa.theta, phi_a, sb.theta, phi_b)
    omega_ij = berry_pair_phase(sa.theta, phi_a, sb.theta, phi_b)
    phase = beta * omega_ij - gamma * d_ij
    return (base * tau_factor) * cmath.exp(1j * phase)


def A_matrix(system: OrbitalSystem) -> Dict[str, Dict[str, Tuple[float, float]]]:
    out: Dict[str, Dict[str, Tuple[float, float]]] = {}
    for a in system.names():
        out[a] = {}
        for b in system.names():
            z = A_ij(system, a, b)
            out[a][b] = (abs(z), cmath.phase(z) if z != 0 else 0.0)
    return out


def closure_residuals(system: OrbitalSystem) -> Dict[str, float]:
    out = {}
    for a in system.names():
        sa = system.sectors[a]
        lhs = 0j
        for b in system.names():
            lhs += A_ij(system, a, b) * system.sectors[b].tau
        rhs = cmath.exp(1j * (sa.phi + sa.berry_phase))
        out[a] = abs(lhs - rhs)
    return out


def closure_penalty(system: OrbitalSystem) -> float:
    res = closure_residuals(system)
    return sum(v * v for v in res.values())


def holonomy_defect(system: OrbitalSystem) -> complex:
    z = 0j
    for sector in system.sectors.values():
        eff_phi = sector.phi + sector.berry_phase
        A_k = sector.coherence_weight * sector.amplitude
        z += A_k * cmath.exp(1j * eff_phi)
    return z


def global_coherence(system: OrbitalSystem) -> float:
    delta = holonomy_defect(system)
    return abs(delta) ** 2


def chord_tension(system: OrbitalSystem) -> float:
    names = system.names()
    total = 0.0
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            sa = system.sectors[a]
            sb = system.sectors[b]
            va = bloch_vector(sa.theta, sa.phi + sa.berry_phase)
            vb = bloch_vector(sb.theta, sb.phi + sb.berry_phase)
            dot = max(-1.0, min(1.0, va[0]*vb[0] + va[1]*vb[1] + va[2]*vb[2]))
            total += abs(A_ij(system, a, b)) * (1.0 - dot)
    return total


def local_vorticity(system: OrbitalSystem) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for a in system.names():
        sa = system.sectors[a]
        eff_a = sa.phi + sa.berry_phase
        ra = poincare_radius(sa.theta)
        vort = 0.0
        for b in system.names():
            if a == b:
                continue
            sb = system.sectors[b]
            eff_b = sb.phi + sb.berry_phase
            rb = poincare_radius(sb.theta)
            Aab = A_ij(system, a, b)
            vort += abs(Aab) * ra * rb * math.sin((eff_b - eff_a) + cmath.phase(Aab))
        out[a] = vort
    return out


def global_chirality(system: OrbitalSystem) -> float:
    vort = local_vorticity(system)
    total = 0.0
    for name, sector in system.sectors.items():
        A_k = sector.coherence_weight * sector.amplitude
        total += A_k * vort[name]
    return total


def effective_mass(system: OrbitalSystem, tension_weight: float = 0.25, closure_weight: float = 0.10) -> Dict[str, float]:
    names = system.names()
    residuals = closure_residuals(system)
    masses: Dict[str, float] = {}
    for a in names:
        sa = system.sectors[a]
        local_tension = 0.0
        for b in names:
            if a == b:
                continue
            sb = system.sectors[b]
            va = bloch_vector(sa.theta, sa.phi + sa.berry_phase)
            vb = bloch_vector(sb.theta, sb.phi + sb.berry_phase)
            dot = max(-1.0, min(1.0, va[0]*vb[0] + va[1]*vb[1] + va[2]*vb[2]))
            local_tension += abs(A_ij(system, a, b)) * (1.0 - dot)
        masses[a] = sa.info_mass * (1.0 + tension_weight * local_tension + closure_weight * residuals[a]) / sa.rhythm_ratio
    return masses
