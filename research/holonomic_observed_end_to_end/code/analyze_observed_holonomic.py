import json, math, re, csv
from pathlib import Path
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt

try:
    from scipy.stats import mannwhitneyu
    SCIPY = True
except Exception:
    SCIPY = False

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)

token_re = re.compile(r"\b\w+\b", re.UNICODE)
_token_cache = {}

def tokenize(text):
    text = (text or "").lower()
    if text not in _token_cache:
        _token_cache[text] = token_re.findall(text)
    return _token_cache[text]

def jaccard(a, b):
    sa, sb = set(tokenize(a)), set(tokenize(b))
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)

def containment(a, b):
    sa, sb = set(tokenize(a)), set(tokenize(b))
    if not sb:
        return 1.0
    return len(sa & sb) / len(sb)

def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)

def theta_from_flags(pi_false, pi_unmarked=0.0):
    theta = 1.0 - 0.5 * (pi_false + pi_unmarked)
    return float(max(0.0, min(1.0, theta)))

def holonomy_from_proxies(sim_qc, sim_sc, truth_score):
    """
    Proxy phase encoding:
    - exact equilateral phases (0, 2π/3, 4π/3) represent the ideal coherence manifold
    - deviations are driven by lack of query-response alignment, lack of source support,
      and reduced truth score.

    This is an engineered observable proxy, not a direct measurement.
    """
    a = math.pi / 6          # support-misalignment scale
    b = 2 * math.pi / 3      # truth-penalty scale

    g1 = 0.0
    g2 = 2 * math.pi / 3 + a * (1.0 - max(0.0, min(1.0, sim_qc)))
    g3 = 4 * math.pi / 3 + a * (1.0 - max(0.0, min(1.0, sim_sc))) + b * (1.0 - max(0.0, min(1.0, truth_score)))

    return float(np.abs(np.sum(np.exp(1j * np.array([g1, g2, g3], dtype=float)))) ** 2)

def effect_and_test(vals_a, vals_b):
    a = np.array(vals_a, dtype=float)
    b = np.array(vals_b, dtype=float)
    mean_diff = float(np.mean(a) - np.mean(b))
    pooled = math.sqrt((np.var(a) + np.var(b)) / 2) if (len(a) and len(b)) else float("nan")
    d = mean_diff / pooled if pooled and pooled > 0 else float("nan")
    p = None
    if SCIPY:
        try:
            p = float(mannwhitneyu(a, b, alternative="two-sided").pvalue)
        except Exception:
            p = None
    return {"mean_diff": mean_diff, "cohen_d": d, "mannwhitney_p": p}

# ----------------------------
# General split
# ----------------------------
general_rows = []
for row in read_jsonl(DATA / "general_data.json"):
    query = row.get("user_query", "")
    response = row.get("chatgpt_response", "")
    hallucinated = 1.0 if str(row.get("hallucination", "")).strip().lower() == "yes" else 0.0

    sim_qc = jaccard(query, response)
    # No external evidence field here; use query-response alignment as the support proxy.
    sim_sc = sim_qc
    truth = 1.0 - hallucinated

    H = holonomy_from_proxies(sim_qc, sim_sc, truth)
    Theta = theta_from_flags(pi_false=hallucinated, pi_unmarked=0.0)

    general_rows.append({
        "dataset": "general",
        "case_type": "hallucinated" if hallucinated else "non_hallucinated",
        "label_hallucinated": int(hallucinated),
        "query_response_jaccard": sim_qc,
        "source_response_support": sim_sc,
        "truth_proxy": truth,
        "H": H,
        "Theta": Theta,
    })

# ----------------------------
# QA split
# ----------------------------
qa_rows = []
for row in read_jsonl(DATA / "qa_data.json"):
    knowledge = row.get("knowledge", "")
    question = row.get("question", "")
    right = row.get("right_answer", "")
    hall = row.get("hallucinated_answer", "")

    for ans, truth, case_type in [(right, 1.0, "truthful"), (hall, 0.0, "hallucinated")]:
        sim_qc = jaccard(question, ans)
        sim_sc = containment(knowledge, ans)
        H = holonomy_from_proxies(sim_qc, sim_sc, truth)
        Theta = theta_from_flags(pi_false=1.0 - truth, pi_unmarked=0.0)
        qa_rows.append({
            "dataset": "qa",
            "case_type": case_type,
            "label_hallucinated": int(1 - truth),
            "query_response_jaccard": sim_qc,
            "source_response_support": sim_sc,
            "truth_proxy": truth,
            "H": H,
            "Theta": Theta,
        })

# ----------------------------
# Summarization split
# ----------------------------
summ_rows = []
for row in read_jsonl(DATA / "summarization_data.json"):
    doc = row.get("document", "")
    right = row.get("right_summary", "")
    hall = row.get("hallucinated_summary", "")

    for ans, truth, case_type in [(right, 1.0, "truthful"), (hall, 0.0, "hallucinated")]:
        support = containment(doc, ans)
        H = holonomy_from_proxies(support, support, truth)
        Theta = theta_from_flags(pi_false=1.0 - truth, pi_unmarked=0.0)
        summ_rows.append({
            "dataset": "summarization",
            "case_type": case_type,
            "label_hallucinated": int(1 - truth),
            "query_response_jaccard": support,
            "source_response_support": support,
            "truth_proxy": truth,
            "H": H,
            "Theta": Theta,
        })

all_rows = general_rows + qa_rows + summ_rows

with open(OUT / "observed_holonomic_scores.jsonl", "w", encoding="utf-8") as f:
    for row in all_rows:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

# Compact CSV for spreadsheets
fieldnames = ["dataset", "case_type", "label_hallucinated", "query_response_jaccard", "source_response_support", "truth_proxy", "H", "Theta"]
with open(OUT / "observed_holonomic_scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in all_rows:
        writer.writerow(row)

def summarize(rows):
    groups = defaultdict(list)
    for r in rows:
        groups[r["case_type"]].append(r)
    out = {}
    for k, rs in groups.items():
        H = np.array([r["H"] for r in rs], dtype=float)
        T = np.array([r["Theta"] for r in rs], dtype=float)
        S = np.array([r["source_response_support"] for r in rs], dtype=float)
        out[k] = {
            "n": int(len(rs)),
            "mean_H": float(np.mean(H)),
            "median_H": float(np.median(H)),
            "std_H": float(np.std(H)),
            "mean_Theta": float(np.mean(T)),
            "mean_support": float(np.mean(S)),
        }
    return out

summary = {
    "general": summarize(general_rows),
    "qa": summarize(qa_rows),
    "summarization": summarize(summ_rows),
    "method_note": "Observed benchmark data analyzed with a proxy phase encoding. The phase variables are engineered observables derived from lexical support and truth labels, not directly observed quantities.",
    "encoding_note": "Ideal coherence is represented by equilateral phases (0, 2π/3, 4π/3). Lack of alignment and reduced truth score perturb this configuration.",
}

summary["tests"] = {
    "general_hallucinated_vs_non_hallucinated_H": effect_and_test(
        [r["H"] for r in general_rows if r["case_type"] == "hallucinated"],
        [r["H"] for r in general_rows if r["case_type"] == "non_hallucinated"],
    ),
    "qa_hallucinated_vs_truthful_H": effect_and_test(
        [r["H"] for r in qa_rows if r["case_type"] == "hallucinated"],
        [r["H"] for r in qa_rows if r["case_type"] == "truthful"],
    ),
    "summarization_hallucinated_vs_truthful_H": effect_and_test(
        [r["H"] for r in summ_rows if r["case_type"] == "hallucinated"],
        [r["H"] for r in summ_rows if r["case_type"] == "truthful"],
    ),
}

with open(OUT / "summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

# Human-readable markdown
lines = []
lines.append("# Observed-data analysis summary")
lines.append("")
lines.append(summary["method_note"])
lines.append("")
for ds in ["general", "qa", "summarization"]:
    lines.append(f"## {ds}")
    for case, stats in summary[ds].items():
        lines.append(f"### {case}")
        lines.append(f"- n: {stats['n']}")
        lines.append(f"- mean_H: {stats['mean_H']:.6f}")
        lines.append(f"- median_H: {stats['median_H']:.6f}")
        lines.append(f"- std_H: {stats['std_H']:.6f}")
        lines.append(f"- mean_Theta: {stats['mean_Theta']:.6f}")
        lines.append(f"- mean_support: {stats['mean_support']:.6f}")
        lines.append("")
(Path(OUT / "summary.md")).write_text("\n".join(lines), encoding="utf-8")

# ----------------------------
# Plots
# ----------------------------
labels = []
vals_H = []
vals_T = []
for ds in ["general", "qa", "summarization"]:
    for case, stats in summary[ds].items():
        labels.append(f"{ds}\n{case}")
        vals_H.append(stats["mean_H"])
        vals_T.append(stats["mean_Theta"])

plt.figure(figsize=(10, 5))
plt.bar(labels, vals_H)
plt.ylabel("Mean holonomy defect H")
plt.title("Observed-data holonomy by dataset and case")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(OUT / "mean_H_by_dataset_case.png", dpi=160)
plt.close()

plt.figure(figsize=(10, 5))
plt.bar(labels, vals_T)
plt.ylabel("Mean Theta")
plt.title("Observed-data semantic truth scalar by dataset and case")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(OUT / "mean_theta_by_dataset_case.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
gen_non = [r["H"] for r in general_rows if r["case_type"] == "non_hallucinated"]
gen_hal = [r["H"] for r in general_rows if r["case_type"] == "hallucinated"]
plt.hist(gen_non, bins=40, alpha=0.7, label="general: non-hallucinated")
plt.hist(gen_hal, bins=40, alpha=0.7, label="general: hallucinated")
plt.xlabel("H")
plt.ylabel("Count")
plt.title("General split by observed hallucination label")
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "general_hallucination_hist.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
for name, rows in [("qa", qa_rows), ("summarization", summ_rows)]:
    x = np.array([r["source_response_support"] for r in rows], dtype=float)
    y = np.array([r["H"] for r in rows], dtype=float)
    plt.scatter(x, y, alpha=0.12, label=name)
plt.xlabel("Source-response support proxy")
plt.ylabel("H")
plt.title("Holonomy defect vs source support")
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "H_vs_support_scatter.png", dpi=160)
plt.close()

print("Done. Results saved to", OUT)
