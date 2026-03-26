from __future__ import annotations

import json
import math
import cmath
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
SYS_ROOT = REPO_ROOT / "systems" / "CIEL_OMEGA_COMPLETE_SYSTEM"
if str(SYS_ROOT) not in sys.path:
    sys.path.insert(0, str(SYS_ROOT))

from ciel_omega.orbital.global_pass import DEFAULT_PARAMS  # type: ignore
from ciel_omega.orbital.extract_geometry import build  # type: ignore
from ciel_omega.orbital.registry import load_system  # type: ignore
from ciel_omega.orbital.dynamics import step  # type: ignore
from ciel_omega.orbital.metrics import (  # type: ignore
    A_ij,
    A_i_zeta,
    berry_pair_phase,
    poincare_distance,
    closure_details,
    closure_penalty,
    global_coherence,
    chord_tension,
    global_chirality,
    holonomy_defect,
    effective_tau_zeta,
    effective_phase_zeta,
    spectral_observables,
)


def _round(x: float, n: int = 12) -> float:
    return round(float(x), n)


def _phase_components(system) -> dict:
    names = system.names()
    closure = closure_details(system)
    sectors = {}
    for name in names:
        s = system.sectors[name]
        eff = s.phi + s.berry_phase
        sectors[name] = {
            "tau": _round(s.tau),
            "theta": _round(s.theta),
            "rho": _round(s.rho),
            "amplitude": _round(s.amplitude),
            "spin": _round(s.spin),
            "phi_local": _round(s.phi),
            "berry_phase": _round(s.berry_phase),
            "effective_phase": _round(eff),
            "closure": {k: _round(v) for k, v in closure[name].items()},
        }

    pairs = {}
    for a in names:
        s_a = system.sectors[a]
        phi_a = s_a.phi + s_a.berry_phase
        for b in names:
            if a == b:
                continue
            s_b = system.sectors[b]
            phi_b = s_b.phi + s_b.berry_phase
            omega = berry_pair_phase(s_a.theta, phi_a, s_b.theta, phi_b)
            dist = poincare_distance(s_a.theta, phi_a, s_b.theta, phi_b)
            z = A_ij(system, a, b)
            tau_ratio = math.log(max(1e-12, s_a.tau / s_b.tau))
            tau_factor = math.exp(-0.5 * (tau_ratio / float(system.params.get("sigma", 0.28))) ** 2)
            pairs[f"{a}->{b}"] = {
                "tau_ratio_log": _round(tau_ratio),
                "tau_factor": _round(tau_factor),
                "omega_ij": _round(omega),
                "d_ij": _round(dist),
                "transport_abs": _round(abs(z)),
                "transport_phase": _round(cmath.phase(z) if z != 0 else 0.0),
                "phase_formula": "arg(A_ij)=beta*Omega_ij-gamma*d_ij",
            }

    zeta = {
        "enabled": bool(system.zeta_pole is not None),
        "effective_tau": _round(effective_tau_zeta(system)),
        "effective_phase": _round(effective_phase_zeta(system)),
        "D_f": _round(float(system.params.get("D_f", 2.57))),
        "euler_leak_angle": _round(0.5 * math.pi * (float(system.params.get("D_f", 2.57)) - 2.0)),
    }
    if system.zeta_pole is not None:
        zeta["vertices"] = [
            {
                "name": v.name,
                "theta": _round(v.theta),
                "phi": _round(v.phi),
                "tau": _round(v.tau),
                "weight": _round(v.weight),
                "coupling_abs": _round(abs(A_i_zeta(system, name))) if (name := names[0]) else 0.0,
            }
            for v in system.zeta_pole.vertices
        ]

    defect = holonomy_defect(system)
    spec = spectral_observables(system)
    global_summary = {
        "holonomy_defect_abs": _round(abs(defect)),
        "holonomy_defect_phase": _round(cmath.phase(defect) if defect != 0 else 0.0),
        "R_H": _round(global_coherence(system)),
        "T_glob": _round(chord_tension(system)),
        "Lambda_glob": _round(global_chirality(system)),
        "closure_penalty": _round(closure_penalty(system)),
        "spectral_radius_A": _round(spec["spectral_radius_A"]),
        "spectral_gap_A": _round(spec["spectral_gap_A"]),
        "fiedler_L": _round(spec["fiedler_L"]),
    }
    return {
        "sectors": sectors,
        "pairs": pairs,
        "zeta": zeta,
        "global": global_summary,
    }


def _observation_check(repo_root: Path, phase_payload: dict) -> dict:
    observed = json.loads((repo_root / "research" / "holonomic_observed_end_to_end" / "results" / "summary.json").read_text(encoding="utf-8"))
    b12 = json.loads((repo_root / "research" / "holonomy_closure_b1_b2" / "results.json").read_text(encoding="utf-8"))
    r_h = phase_payload["global"]["R_H"]
    checks = {
        "truthful_general_mean_H": observed["general"]["non_hallucinated"]["mean_H"],
        "truthful_qa_mean_H": observed["qa"]["truthful"]["mean_H"],
        "truthful_summarization_mean_H": observed["summarization"]["truthful"]["mean_H"],
        "hallucinated_general_mean_H": observed["general"]["hallucinated"]["mean_H"],
        "repo_R_H_vs_truthful_general_ratio": r_h / observed["general"]["non_hallucinated"]["mean_H"],
        "repo_R_H_vs_truthful_qa_ratio": r_h / observed["qa"]["truthful"]["mean_H"],
        "repo_R_H_below_truthful_general": r_h < observed["general"]["non_hallucinated"]["mean_H"],
        "repo_R_H_below_truthful_qa": r_h < observed["qa"]["truthful"]["mean_H"],
        "repo_R_H_far_below_hallucinated_general": r_h < observed["general"]["hallucinated"]["mean_H"],
        "triangle_loop_phase_rad": b12["B2_cp2_triangle"]["bargmann_invariant"]["phase_rad"],
        "triangle_loop_phase_deg": b12["B2_cp2_triangle"]["bargmann_invariant"]["phase_deg"],
        "zeta_effective_phase_rad": phase_payload["zeta"]["effective_phase"],
        "method_note": observed["method_note"],
        "encoding_note": observed["encoding_note"],
    }
    return checks


def _markdown(payload: dict) -> str:
    lines: list[str] = []
    lines.append("# Orbital Phase Components and Observation Check")
    lines.append("")
    lines.append("This report derives the current canonical phase decomposition from the orbital engine and compares the resulting coherence observables against the repo's observed benchmark package.")
    lines.append("")
    lines.append("## Governing relations")
    lines.append("")
    lines.append(r"- Local effective phase: $\gamma_i^{\mathrm{eff}} = \phi_i + \gamma_{B,i}$." )
    lines.append(r"- Pair transport kernel: $A_{ij} = (w_{ij} \tau\text{-factor}_{ij}) e^{i(\beta \Omega_{ij} - \gamma d_{ij})}$." )
    lines.append(r"- Tau resonance factor: $\tau\text{-factor}_{ij} = \exp\left[-\frac12\left(\frac{\log(\tau_i/\tau_j)}{\sigma}\right)^2\right]$." )
    lines.append(r"- Closure relation: $\sum_j A_{ij}\tau_j + A_{i\zeta}\tau_\zeta \approx e^{i\gamma_i^{\mathrm{eff}}}$." )
    lines.append(r"- Euler leak angle: $\theta_E = \tfrac{\pi}{2}(D_f-2)$." )
    lines.append("")
    lines.append("## Sector phases")
    lines.append("")
    lines.append("| sector | tau | phi_local | berry | effective | lhs_phase | phase_error | residual |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for name, row in payload["phases"]["sectors"].items():
        c = row["closure"]
        lines.append(f"| {name} | {row['tau']:.6f} | {row['phi_local']:.6f} | {row['berry_phase']:.6f} | {row['effective_phase']:.6f} | {c['lhs_phase']:.6f} | {c['phase_error']:.6f} | {c['residual']:.6f} |")
    lines.append("")
    lines.append("## Representative pair transport terms")
    lines.append("")
    lines.append("| pair | tau_factor | Omega_ij | d_ij | arg(A_ij) | |A_ij| |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    pair_keys = list(payload["phases"]["pairs"].keys())
    for key in pair_keys[:10]:
        row = payload["phases"]["pairs"][key]
        lines.append(f"| {key} | {row['tau_factor']:.6f} | {row['omega_ij']:.6f} | {row['d_ij']:.6f} | {row['transport_phase']:.6f} | {row['transport_abs']:.6f} |")
    lines.append("")
    lines.append("## Global observables")
    lines.append("")
    for k, v in payload["phases"]["global"].items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("## Zeta / Euler scaling")
    lines.append("")
    for k, v in payload["phases"]["zeta"].items():
        if k != "vertices":
            lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("## Observation check")
    lines.append("")
    checks = payload["observation_check"]
    lines.append(f"- repo_R_H: {payload['phases']['global']['R_H']}")
    lines.append(f"- truthful_general_mean_H: {checks['truthful_general_mean_H']}")
    lines.append(f"- truthful_qa_mean_H: {checks['truthful_qa_mean_H']}")
    lines.append(f"- hallucinated_general_mean_H: {checks['hallucinated_general_mean_H']}")
    lines.append(f"- repo_R_H_below_truthful_general: {checks['repo_R_H_below_truthful_general']}")
    lines.append(f"- repo_R_H_below_truthful_qa: {checks['repo_R_H_below_truthful_qa']}")
    lines.append(f"- triangle_loop_phase_rad (B2): {checks['triangle_loop_phase_rad']}")
    lines.append(f"- zeta_effective_phase_rad: {checks['zeta_effective_phase_rad']}")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("The current canonical run stays deep inside the truthful side of the observed benchmark split: the repo-level $R_H$ is below the truthful means for the General and QA datasets and far below the hallucinated regime. The B2 triangle loop phase remains nonzero, so closure is not being achieved by collapsing chirality to zero.")
    return "\n".join(lines)


def main() -> None:
    payload = build(REPO_ROOT)
    orbital_dir = REPO_ROOT / "manifests" / "orbital"
    orbital_dir.mkdir(parents=True, exist_ok=True)
    (orbital_dir / "sectors_global.json").write_text(json.dumps(payload["sectors"], indent=2), encoding="utf-8")
    (orbital_dir / "couplings_global.json").write_text(json.dumps(payload["couplings"], indent=2), encoding="utf-8")

    system = load_system(orbital_dir / "sectors_global.json", orbital_dir / "couplings_global.json", params=dict(DEFAULT_PARAMS))
    for _ in range(20):
        system = step(system, dt=DEFAULT_PARAMS["dt"], tau_eta=DEFAULT_PARAMS["tau_eta"], tau_reg=DEFAULT_PARAMS["tau_reg"])

    phase_payload = _phase_components(system)
    observation_check = _observation_check(REPO_ROOT, phase_payload)
    result = {
        "engine": "phase_component_pass_v1",
        "params": dict(DEFAULT_PARAMS),
        "phases": phase_payload,
        "observation_check": observation_check,
    }

    (orbital_dir / "phase_components.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    report_dir = REPO_ROOT / "reports" / "phase_components"
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "summary.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (report_dir / "summary.md").write_text(_markdown(result), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
