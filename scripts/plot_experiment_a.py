"""Reproduce the FYP Experiment A document-level MRR@5 bar chart.

Reads the original archived summary JSONs; does not alter experimental data.
Requirements: matplotlib (free, install with: python -m pip install matplotlib).
Run from any working directory: python scripts/plot_experiment_a.py
"""
from pathlib import Path
import json

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "experiment_A_USBR"
OUTPUT = ROOT / "docs" / "figures" / "experiment_a_document_mrr_at5.png"

names = ["BM25", "Dense", "Hybrid"]
keys = ["bm25", "dense", "hybrid"]
summaries = [
    json.loads((RESULTS / f"retrieval_{name}_summary.json").read_text(encoding="utf-8"))
    for name in keys
]
for name, s in zip(names, summaries):
    if s["k"] != 5 or s["n_questions"] != 12:
        raise ValueError(f"Unexpected experimental setup for {name}")
    if not 0 <= s["document_mrr_at_k"] <= 1:
        raise ValueError(f"Invalid MRR for {name}")

values = [float(s["document_mrr_at_k"]) for s in summaries]
fig, ax = plt.subplots(figsize=(10.4, 6.4), dpi=180)
fig.subplots_adjust(top=0.80, bottom=0.25, left=0.12, right=0.97)
bars = ax.bar(names, values, width=0.56)
ax.set_ylim(0, 1.12)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_ylabel("Document-level MRR@5 (higher is better)", fontsize=11)
ax.grid(axis="y", alpha=0.22)
ax.set_axisbelow(True)
for bar, value in zip(bars, values):
    ax.annotate(f"{value:.4f}", (bar.get_x() + bar.get_width()/2, value),
                xytext=(0, 8), textcoords="offset points", ha="center",
                va="bottom", fontsize=14, weight="bold")
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
fig.suptitle("Experiment A | Retrieval Strategy Comparison", fontsize=18,
             weight="bold", y=0.96)
fig.text(0.5, 0.86, "12 benchmark questions  |  Top-5  |  Three public USBR FIST manuals",
         ha="center", fontsize=11)
fig.text(0.5, 0.11, "All three approaches recorded document Hit@5 = 1.0000.",
         ha="center", fontsize=10)
fig.text(0.5, 0.07,
         "Document-level proxy only: NOT passage relevance or generated-answer accuracy.",
         ha="center", fontsize=9)
fig.text(0.5, 0.035,
         "Source: results/experiment_A_USBR/retrieval_{bm25,dense,hybrid}_summary.json",
         ha="center", fontsize=8)
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT, dpi=180, facecolor="white")
plt.close(fig)
print(f"Generated: {OUTPUT}")
