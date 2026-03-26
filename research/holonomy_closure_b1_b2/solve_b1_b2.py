#!/usr/bin/env python3
from __future__ import annotations
import json, math, cmath
from pathlib import Path


def normalize(v):
    n = math.sqrt(sum(abs(z)**2 for z in v))
    return [z / n for z in v]


def inner(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def compute_b1():
    return {
        "loop_coordinate": "theta in [0, 2pi)",
        "connection_ansatz": "A_theta = a (constant)",
        "closure_classes": {
            "bosonic_n0": {"chi": 0.0, "a_star": 0.0, "ground_energy": 0.0},
            "spinor_n0": {"chi": math.pi, "a_star": 0.5, "ground_energy": 0.25},
            "bosonic_n1": {"chi": 2 * math.pi, "a_star": 1.0, "ground_energy": 0.0},
        },
        "toy_conclusion": "spinor closure induces a nonzero minimal spectral gap even when the closure defect is minimized",
    }


def compute_b2(repo_root: Path):
    data = json.loads((repo_root / "reports/global_orbital_coherence_pass/real_geometry.json").read_text())
    sectors = data["sectors"]["sectors"]
    triad = ["constraints", "memory", "runtime"]
    vectors = {}
    for name in triad:
        tau = sectors[name]["tau"]
        phi = sectors[name]["phi"]
        vectors[name] = normalize([1 + 0j, tau * cmath.exp(1j * phi), tau * tau * cmath.exp(2j * phi)])

    pairs = {}
    for i, a in enumerate(triad):
        for b in triad[i + 1 :]:
            z = inner(vectors[a], vectors[b])
            pairs[f"{a}|{b}"] = {
                "overlap_abs": abs(z),
                "overlap_arg_rad": cmath.phase(z),
                "fubini_study_distance_rad": math.acos(min(1.0, max(-1.0, abs(z)))),
            }
    B = inner(vectors["constraints"], vectors["memory"]) * inner(vectors["memory"], vectors["runtime"]) * inner(vectors["runtime"], vectors["constraints"])
    return {
        "triad": triad,
        "source_geometry_file": "reports/global_orbital_coherence_pass/real_geometry.json",
        "states": {
            name: {
                "tau": sectors[name]["tau"],
                "phi": sectors[name]["phi"],
                "projective_seed": "[1, tau*exp(i phi), tau^2*exp(2 i phi)]",
            }
            for name in triad
        },
        "pair_metrics": pairs,
        "bargmann_invariant": {
            "real": B.real,
            "imag": B.imag,
            "abs": abs(B),
            "phase_rad": cmath.phase(B),
            "phase_deg": cmath.phase(B) * 180 / math.pi,
        },
        "cp_like_loop_phase_statement": "nonzero Bargmann phase from the canonical repo triad shows a closure-sensitive CP-like loop observable without inserting an external fitted phase",
    }


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    results = {
        "B1_minimal_loop": compute_b1(),
        "B2_cp2_triangle": compute_b2(repo_root),
    }
    out = repo_root / "research/holonomy_closure_b1_b2/results.json"
    out.write_text(json.dumps(results, indent=2))
    print(out)


if __name__ == "__main__":
    main()
