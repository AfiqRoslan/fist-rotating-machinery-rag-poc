# Experiment A — Public USBR FIST Retrieval Baseline

**Status:** Archived preliminary research experiment, not a production accuracy validation.
**Dataset:** Three public U.S. Bureau of Reclamation (USBR) FIST manuals. **No TNB REMACO data were used.**

## Dataset

| Source manual | PDF pages | Text chunks |
|---|---:|---:|
| FIST 2-1 — Alignment of Rotating Machinery | 109 | 251 |
| FIST 2-4 — Lubrication of Equipment | 48 | 115 |
| FIST 2-12 — Mechanical Maintenance of Hydroelectric and Large Pump Units | 62 | 145 |
| **Total** | **219** | **511** |

The extracted chunks retain PDF physical page numbers. The local embedding array has shape **(511, 384)**, generated with `sentence-transformers/all-MiniLM-L6-v2`.

## Preliminary retrieval benchmark

**Test design:** 12 provisional questions, top-k = 5. A hit is recorded if a result is from the *expected document*, not necessarily if it is the correct passage/page. The following numbers are therefore **document-level proxy metrics**.

| Retrieval approach | Document Hit@5 | Document MRR@5 | Mean retrieval latency |
|---|---:|---:|---:|
| BM25 | 1.0000 | 0.9583 | 0.21 ms |
| Dense (MiniLM) | 1.0000 | 0.8750 | 1,280.63 ms |
| Hybrid (RRF) | 1.0000 | 1.0000 | 453.11 ms |

**Interpretation:** Every strategy retrieved at least one passage from the expected document within five results for all 12 questions. Hybrid ranked the expected document highest more consistently than the other methods on this *specific small benchmark*. These numbers **do not prove** that Hybrid is more accurate at finding the correct passage or generating correct answers.

**Latency caution:** Measurements can include one-time embedding model loading; they are not controlled steady-state comparisons. Do not claim that BM25 is definitively faster or Hybrid definitively best for real industrial use based on these alone.

## Archived evidence

| File | Purpose |
|---|---|
| [`experiment_manifest.json`](../results/experiment_A_USBR/experiment_manifest.json) | Corpus, models, configuration, hashes and limitations |
| [`benchmark_questions.csv`](../results/experiment_A_USBR/benchmark_questions.csv) | Provisional evaluation questions |
| [`retrieval_bm25.csv`](../results/experiment_A_USBR/retrieval_bm25.csv) | BM25 per-question output |
| [`retrieval_dense.csv`](../results/experiment_A_USBR/retrieval_dense.csv) | Dense per-question output |
| [`retrieval_hybrid.csv`](../results/experiment_A_USBR/retrieval_hybrid.csv) | Hybrid per-question output |
| [`retrieval_bm25_summary.json`](../results/experiment_A_USBR/retrieval_bm25_summary.json) | BM25 aggregate metrics |
| [`retrieval_dense_summary.json`](../results/experiment_A_USBR/retrieval_dense_summary.json) | Dense aggregate metrics |
| [`retrieval_hybrid_summary.json`](../results/experiment_A_USBR/retrieval_hybrid_summary.json) | Hybrid aggregate metrics |
| [`rag_responses.jsonl`](../results/experiment_A_USBR/rag_responses.jsonl) | Two generated sample responses; **not formally graded** |
| [`demo_index_USBR.zip`](../results/experiment_A_USBR/demo_index_USBR.zip) | Portable `chunks.json` and `embeddings.npy`, allowing a demonstration without reindexing |

## Functional tests already performed

- Qwen3 provided an answer about vertical-shaft alignment using an excerpt cited as FIST 2-1, PDF page 24.
- Clicking a citation opened the corresponding PDF page.
- A request for TNB REMACO rotor condition was refused because internal company records were absent. This is a **specific test**, not a full safety evaluation.
- Local retrieval and answer generation worked without Wi-Fi; a locally served copy of the PDF also opened at page 24 offline.
- Development-PC test suite: six pytest tests passed. These tests do not replace a labeled retrieval or groundedness study.

## Limitations and planned improvements

- Only **12** provisional questions.
- Expected source **documents** labeled; no verified relevant **passage/page** labels.
- Not yet a systematic evaluation of answer correctness, hallucinations or citation faithfulness.
- Some retrieved content may be unhelpful (including low-text pages).
- No TNB maintenance records, failure labels, SCADA signals or plant-specific procedures.
- Future industrial evaluation depends on authorization, dataset suitability and supervisor scope approval.

**Research approach:** Preserve Experiment A unchanged as a public baseline. If TNB REMACO approves a new dataset, evaluate it separately with documented differences in corpus, metrics and access restrictions.
