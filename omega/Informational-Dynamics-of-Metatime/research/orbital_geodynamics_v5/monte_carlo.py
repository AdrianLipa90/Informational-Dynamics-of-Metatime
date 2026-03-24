from __future__ import annotations
import json, math, random
from pathlib import Path
from statistics import mean, median
from typing import Dict, List

from registry import load_system
from dynamics import step
from metrics import global_coherence, chord_tension, global_chirality, closure_penalty, spectral_observables
from extract_real_geometry_v3 import build

PARAM_RANGES = {
    'dt': (0.018, 0.035),
    'tau_eta': (0.004, 0.020),
    'tau_reg': (0.0, 0.010),
    'sigma': (0.20, 0.40),
    'beta': (0.60, 1.10),
    'gamma': (0.12, 0.38),
    'I0': (0.0075, 0.0115),
    'mesh_boost': (0.90, 1.15),
    'tension_weight': (0.18, 0.34),
    'closure_weight': (0.06, 0.16),
}


def objective(metrics: dict) -> float:
    return 1.0 * metrics['R_H'] + 0.5 * metrics['T_glob'] + 0.35 * metrics['closure_penalty'] - 0.20 * abs(metrics['Lambda_glob'])


def make_params(rng: random.Random) -> dict:
    return {k: rng.uniform(a, b) for k, (a, b) in PARAM_RANGES.items()}


def snapshot(system) -> dict:
    spec = spectral_observables(system)
    return {
        'R_H': global_coherence(system),
        'T_glob': chord_tension(system),
        'Lambda_glob': global_chirality(system),
        'closure_penalty': closure_penalty(system),
        'spectral_radius_A': spec['spectral_radius_A'],
        'spectral_gap_A': spec['spectral_gap_A'],
        'fiedler_L': spec['fiedler_L'],
    }


def pearson(xs: List[float], ys: List[float]) -> float:
    mx = mean(xs)
    my = mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    deny = math.sqrt(sum((y - my) ** 2 for y in ys))
    den = denx * deny
    if den == 0:
        return 0.0
    return num / den


def run_trial(root: Path, base_params: dict, steps: int) -> dict:
    cfg_dir = root / 'config'
    system = load_system(cfg_dir / 'sectors_real_v4.json', cfg_dir / 'couplings_real_v4.json', params=base_params)
    initial = snapshot(system)
    for _ in range(steps):
        system = step(system, dt=base_params['dt'], tau_eta=base_params['tau_eta'], tau_reg=base_params['tau_reg'])
    final = snapshot(system)
    return {'initial': initial, 'final': final}


def summarize_runs(runs: List[dict]) -> dict:
    keys = ['R_H', 'T_glob', 'Lambda_glob', 'closure_penalty', 'spectral_radius_A', 'spectral_gap_A', 'fiedler_L']
    out = {}
    for k in keys:
        vals = [r['final'][k] for r in runs]
        vals_sorted = sorted(vals)
        out[k] = {
            'mean': mean(vals),
            'median': median(vals),
            'p10': vals_sorted[max(0, int(0.10 * (len(vals_sorted)-1)))],
            'p90': vals_sorted[min(len(vals_sorted)-1, int(0.90 * (len(vals_sorted)-1)))],
            'min': vals_sorted[0],
            'max': vals_sorted[-1],
        }
    return out


def sensitivity(runs: List[dict]) -> dict:
    score = [r['objective'] for r in runs]
    out = {}
    for p in PARAM_RANGES:
        xs = [r['params'][p] for r in runs]
        out[p] = {
            'corr_with_objective': pearson(xs, score),
            'corr_with_R_H': pearson(xs, [r['final']['R_H'] for r in runs]),
            'corr_with_closure_penalty': pearson(xs, [r['final']['closure_penalty'] for r in runs]),
            'corr_with_Lambda': pearson(xs, [r['final']['Lambda_glob'] for r in runs]),
        }
    return out


def main(samples: int = 400, steps: int = 20, seed: int = 42):
    root = Path(__file__).resolve().parent
    repo_root = root.parents[1]
    payload = build(repo_root)
    (root/'config'/'sectors_real_v4.json').write_text(json.dumps(payload['sectors'], indent=2), encoding='utf-8')
    (root/'config'/'couplings_real_v4.json').write_text(json.dumps(payload['couplings'], indent=2), encoding='utf-8')

    rng = random.Random(seed)
    runs = []
    for idx in range(samples):
        params = make_params(rng)
        result = run_trial(root, params, steps)
        score = objective(result['final'])
        runs.append({
            'trial': idx,
            'params': params,
            'initial': result['initial'],
            'final': result['final'],
            'objective': score,
        })

    runs_sorted = sorted(runs, key=lambda r: r['objective'])
    summary = summarize_runs(runs)
    sens = sensitivity(runs)

    out = {
        'engine': 'orbital_geodynamics_v5_monte_carlo_spectral',
        'samples': samples,
        'steps': steps,
        'seed': seed,
        'summary': summary,
        'best_run': runs_sorted[0],
        'worst_run': runs_sorted[-1],
        'top_10_runs': runs_sorted[:10],
        'sensitivity': sens,
    }

    out_dir = root / 'results'
    out_dir.mkdir(exist_ok=True)
    (out_dir / 'v5_monte_carlo_results.json').write_text(json.dumps(out, indent=2), encoding='utf-8')

    md = []
    md.append('# V5 Monte Carlo + Spectral Analysis')
    md.append('')
    md.append(f'- samples: **{samples}**')
    md.append(f'- steps per trial: **{steps}**')
    md.append(f'- seed: **{seed}**')
    md.append('')
    md.append('## Aggregate summary')
    for k, s in summary.items():
        md.append(f'### {k}')
        md.append(f"- mean: {s['mean']:.6f}")
        md.append(f"- median: {s['median']:.6f}")
        md.append(f"- p10: {s['p10']:.6f}")
        md.append(f"- p90: {s['p90']:.6f}")
        md.append(f"- min: {s['min']:.6f}")
        md.append(f"- max: {s['max']:.6f}")
        md.append('')
    md.append('## Best run')
    md.append(f"- objective: {runs_sorted[0]['objective']:.6f}")
    for k, v in runs_sorted[0]['final'].items():
        md.append(f'- {k}: {v:.6f}')
    md.append('')
    md.append('## Parameter sensitivity (corr with objective)')
    ranked = sorted(((abs(v['corr_with_objective']), k, v['corr_with_objective']) for k, v in sens.items()), reverse=True)
    for _, k, c in ranked:
        md.append(f'- {k}: {c:.6f}')
    (out_dir / 'v5_monte_carlo_summary.md').write_text('\n'.join(md), encoding='utf-8')
    print(out_dir / 'v5_monte_carlo_results.json')


if __name__ == '__main__':
    main()
