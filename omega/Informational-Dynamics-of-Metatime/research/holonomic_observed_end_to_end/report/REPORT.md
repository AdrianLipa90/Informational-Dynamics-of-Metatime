# Holonomic Relations — observed-data end-to-end analysis

## Scope

This package runs an end-to-end analysis on observed benchmark data from HaluEval using a **proxy phase encoding** of the Holonomic Relations formalism.

## What was actually done

Three observed datasets were processed:

- `general_data.json`
- `qa_data.json`
- `summarization_data.json`

For each example, the pipeline computed:

- `query_response_jaccard`
- `source_response_support`
- `truth_proxy`
- holonomy defect `H`
- semantic truth scalar `Theta`

## Critical methodological note

The phases are **not directly measured** in these datasets.

They are engineered from observed textual properties:
- lexical alignment between query and answer,
- support of the answer in source/evidence text,
- provided hallucination labels.

This means the package delivers a **real observed-data analysis under a proxy observable model**, not a direct physical or ontological measurement of phases.

## Main results

### 1. General split (observed hallucination labels)

- non-hallucinated mean `H`: **0.2187**
- hallucinated mean `H`: **2.1289**
- non-hallucinated mean `Theta`: **1.0000**
- hallucinated mean `Theta`: **0.5000**

Effect test on `H`:
- mean difference (hallucinated − non-hallucinated): **1.9102**
- Cohen's d: **28.4194**
- Mann–Whitney p: **0.0**

### 2. QA split (truthful vs hallucinated answers)

- truthful mean `H`: **0.2540**
- hallucinated mean `H`: **2.2189**
- truthful mean `Theta`: **1.0000**
- hallucinated mean `Theta`: **0.5000**

Effect test on `H`:
- mean difference (hallucinated − truthful): **1.9649**
- Cohen's d: **8.0559**
- Mann–Whitney p: **0.0**

### 3. Summarization split (truthful vs hallucinated summaries)

- truthful mean `H`: **0.0077**
- hallucinated mean `H`: **2.7827**
- truthful mean `Theta`: **1.0000**
- hallucinated mean `Theta`: **0.5000**

Effect test on `H`:
- mean difference (hallucinated − truthful): **2.7750**
- Cohen's d: **39.1144**
- Mann–Whitney p: **0.0**

## Interpretation

Under this proxy encoding, higher hallucination burden is associated with higher `H` in all three observed-data settings.

That means the present formalization is at least **directionally consistent** with benchmark truth/hallucination labels.

## What this does not prove

It does **not** prove:
- that the phase variables are physically real,
- that the chosen encoding is unique,
- that the formalism is empirically established.

It only shows that an end-to-end observable pipeline can be built and that, on these benchmark datasets, the derived `H` behaves in the intended direction.

## Files to inspect first

- `results/summary.json`
- `results/summary.md`
- `results/mean_H_by_dataset_case.png`
- `results/mean_theta_by_dataset_case.png`
- `results/general_hallucination_hist.png`
- `results/H_vs_support_scatter.png`
