
import json
import math
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "results"
OUT.mkdir(parents=True, exist_ok=True)

T = 2500
N_RUNS = 300
ETA = 0.012
NOISE_SCALE = 0.018
SEED = 42

rng = np.random.default_rng(SEED)


def project(gS, gC, gQ, gT):
    """Operational -> geometric projection."""
    return np.array([gS - gT, gC - gT, gQ - gT], dtype=float)


def wrap_phase(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def holonomy_density(g):
    return float(np.abs(np.sum(np.exp(1j * g))) ** 2)


def coherence_coeffs(g):
    c12 = 0.5 * (1 + math.cos(g[0] - g[1]))
    c13 = 0.5 * (1 + math.cos(g[0] - g[2]))
    c23 = 0.5 * (1 + math.cos(g[1] - g[2]))
    return c12, c13, c23


def potential_grad(g):
    """Gradient of 0.5 * sum C_ij (gi-gj)^2 with frozen coefficients."""
    c12, c13, c23 = coherence_coeffs(g)
    grad = np.zeros(3, dtype=float)
    grad[0] = c12 * (g[0] - g[1]) + c13 * (g[0] - g[2])
    grad[1] = c12 * (g[1] - g[0]) + c23 * (g[1] - g[2])
    grad[2] = c13 * (g[2] - g[0]) + c23 * (g[2] - g[1])
    return grad


def truth_scalar(dist_profile):
    # Distortion scores represent false/unmarked burden in [0,1].
    pi_false = dist_profile["false"]
    pi_unmarked = dist_profile["unmarked"]
    theta = 1.0 - (pi_false + pi_unmarked) / 2.0
    return float(max(0.0, min(1.0, theta)))


def run_single(dist_profile):
    gS, gC, gQ, gT = rng.uniform(-np.pi, np.pi, size=4)
    H_traj = np.zeros(T, dtype=float)
    theta = truth_scalar(dist_profile)

    # Aggregate distortion intensity perturbs dynamics away from coherence.
    distort_strength = (
        dist_profile["lie"]
        + dist_profile["omit"]
        + dist_profile["hallucinate"]
        + dist_profile["smooth"]
    ) / 4.0

    for t in range(T):
        g = project(gS, gC, gQ, gT)
        g = np.array([wrap_phase(v) for v in g], dtype=float)

        grad = potential_grad(g)
        noise = rng.normal(0.0, NOISE_SCALE, size=3)

        # Bias away from exact coherence when distortion grows.
        distortion_push = distort_strength * rng.normal(0.0, 0.03, size=3)

        g = g - ETA * grad + noise + distortion_push
        g = np.array([wrap_phase(v) for v in g], dtype=float)

        # Minimal back-map with truth phase as reference gauge.
        gS = wrap_phase(g[0] + gT)
        gC = wrap_phase(g[1] + gT)
        gQ = wrap_phase(g[2] + gT)

        H_traj[t] = holonomy_density(g)

    return H_traj, theta


def summarize_group(name, dist_profile, n_runs=N_RUNS):
    runs = []
    thetas = []
    for _ in range(n_runs):
        traj, theta = run_single(dist_profile)
        runs.append(traj)
        thetas.append(theta)

    runs = np.asarray(runs)
    thetas = np.asarray(thetas)
    final_H = runs[:, -1]

    corr = float(np.corrcoef(final_H, thetas)[0, 1]) if np.std(final_H) > 0 and np.std(thetas) > 0 else float("nan")

    summary = {
        "group": name,
        "n_runs": int(n_runs),
        "mean_final_H": float(np.mean(final_H)),
        "median_final_H": float(np.median(final_H)),
        "std_final_H": float(np.std(final_H)),
        "mean_theta": float(np.mean(thetas)),
        "corr_finalH_theta": corr,
    }
    return runs, thetas, summary


def save_csv(path, arr, header=None):
    np.savetxt(path, arr, delimiter=",", header=header or "", comments="")


def main():
    low_dist = {
        "lie": 0.05,
        "omit": 0.08,
        "hallucinate": 0.04,
        "smooth": 0.06,
        "false": 0.05,
        "unmarked": 0.07,
    }
    high_dist = {
        "lie": 0.55,
        "omit": 0.50,
        "hallucinate": 0.60,
        "smooth": 0.48,
        "false": 0.52,
        "unmarked": 0.58,
    }

    low_runs, low_theta, low_summary = summarize_group("low_distortion", low_dist)
    high_runs, high_theta, high_summary = summarize_group("high_distortion", high_dist)

    mean_low = np.mean(low_runs, axis=0)
    mean_high = np.mean(high_runs, axis=0)
    low_final = low_runs[:, -1]
    high_final = high_runs[:, -1]

    save_csv(OUT / "mean_H_low.csv", mean_low, "mean_H_low")
    save_csv(OUT / "mean_H_high.csv", mean_high, "mean_H_high")
    save_csv(OUT / "final_H_low.csv", low_final, "final_H_low")
    save_csv(OUT / "final_H_high.csv", high_final, "final_H_high")
    save_csv(OUT / "theta_low.csv", low_theta, "theta_low")
    save_csv(OUT / "theta_high.csv", high_theta, "theta_high")

    plt.figure(figsize=(8, 5))
    plt.plot(mean_low, label="low distortion")
    plt.plot(mean_high, label="high distortion")
    plt.xlabel("time step")
    plt.ylabel("mean holonomy density H")
    plt.title("Mean holonomy dynamics")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "mean_holonomy_comparison.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.hist(low_final, bins=30, alpha=0.7, label="low distortion")
    plt.hist(high_final, bins=30, alpha=0.7, label="high distortion")
    plt.xlabel("final H")
    plt.ylabel("count")
    plt.title("Final holonomy distribution")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "final_holonomy_histogram.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(low_final, low_theta, alpha=0.7, label="low distortion")
    plt.scatter(high_final, high_theta, alpha=0.7, label="high distortion")
    plt.xlabel("final H")
    plt.ylabel("Theta")
    plt.title("Final holonomy vs semantic truth scalar")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "finalH_vs_theta.png", dpi=160)
    plt.close()

    summary = {
        "seed": SEED,
        "parameters": {
            "T": T,
            "N_RUNS_per_group": N_RUNS,
            "ETA": ETA,
            "NOISE_SCALE": NOISE_SCALE,
        },
        "groups": [low_summary, high_summary],
        "note": "Synthetic validation only. Not empirical evidence."
    }

    with open(OUT / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    md = []
    md.append("# Synthetic validation summary")
    md.append("")
    md.append("This run is synthetic and tests internal consistency only.")
    md.append("")
    for g in summary["groups"]:
        md.append(f"## {g['group']}")
        md.append(f"- n_runs: {g['n_runs']}")
        md.append(f"- mean_final_H: {g['mean_final_H']:.6f}")
        md.append(f"- median_final_H: {g['median_final_H']:.6f}")
        md.append(f"- std_final_H: {g['std_final_H']:.6f}")
        md.append(f"- mean_theta: {g['mean_theta']:.6f}")
        md.append(f"- corr_finalH_theta: {g['corr_finalH_theta']}")
        md.append("")
    (OUT / "summary.md").write_text("\n".join(md), encoding="utf-8")

    print("Saved results to:", OUT)


if __name__ == "__main__":
    main()
