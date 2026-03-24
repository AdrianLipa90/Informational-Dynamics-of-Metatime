from __future__ import annotations
import cmath
import math
from typing import Dict
from model import OrbitalSystem


def bloch_vector(theta: float, phi: float):
    return (
        math.sin(theta) * math.cos(phi),
        math.sin(theta) * math.sin(phi),
        math.cos(theta),
    )


def poincare_radius(theta: float) -> float:
    return math.tanh(math.tan(theta / 2.0))


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
            total += system.coupling(a, b) * (1.0 - dot)
    return total


def local_vorticity(system: OrbitalSystem) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for a in system.names():
        sa = system.sectors[a]
        ra = poincare_radius(sa.theta)
        eff_a = sa.phi + sa.berry_phase
        vort = 0.0
        for b in system.names():
            if a == b:
                continue
            sb = system.sectors[b]
            rb = poincare_radius(sb.theta)
            eff_b = sb.phi + sb.berry_phase
            vort += system.coupling(a, b) * ra * rb * math.sin(eff_b - eff_a)
        out[a] = vort
    return out


def global_chirality(system: OrbitalSystem) -> float:
    vort = local_vorticity(system)
    total = 0.0
    for name, sector in system.sectors.items():
        A_k = sector.coherence_weight * sector.amplitude
        total += A_k * vort[name]
    return total


def effective_mass(system: OrbitalSystem, tension_weight: float = 0.25) -> Dict[str, float]:
    names = system.names()
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
            local_tension += system.coupling(a, b) * (1.0 - dot)
        masses[a] = sa.info_mass * (1.0 + tension_weight * local_tension) / sa.rhythm_ratio
    return masses
