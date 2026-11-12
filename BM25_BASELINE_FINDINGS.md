# BM25 Baseline Evaluation — Preliminary Findings

**Project:** FIST Rotating Machinery RAG Proof of Concept  
**Date:** 12 November 2026  
**Evaluation Method:** BM25 (Top-5 retrieval)

## 1. Dataset

Three publicly available U.S. Bureau of Reclamation FIST manuals were used:

- FIST 2-1: Alignment of Rotating Machinery (109 pages, 251 chunks)
- FIST 2-4: Lubrication of Equipment (48 pages, 115 chunks)
- FIST 2-12: Mechanical Maintenance of Hydroelectric and Large Pump Units (62 pages, 145 chunks)

**Total:** 219 pages and 511 text chunks.

## 2. Evaluation Results

The initial evaluation used 12 questions with manually assigned expected source documents.

| Metric | Result |
|---|---|
| Expected-source Hit@1 | 91.67% (11/12) |
| Expected-source Hit@5 | 100% (12/12) |
| First expected-source reciprocal rank (MRR@5) | 0.9583 |
| Mean retrieval latency | 0.212 ms |

## 3. Qualitative Findings

Eleven questions retrieved a chunk from their expected document at Rank 1. Question 11 retrieved its expected document at Rank 2.

For Question 11, the Rank 1 passage came from FIST 2-4 and discussed turbine oil temperature and oxidation in hydroelectric generating units. Although it came from a different manual, the passage was relevant to the question.

The Rank 2 passage from FIST 2-12 discussed general mechanical maintenance concerns, including component wear, inspections and unexpected outages.

Some lower-ranked passages contained cover information and table-of-contents text rather than useful technical evidence.

## 4. Limitations

- The evaluation contains only 12 questions.
- Ground truth is assigned at document level rather than passage level.
- The benchmark does not measure generated-answer accuracy.
- Some questions may have valid supporting evidence in multiple manuals.
- Retrieval latency reflects local in-memory retrieval rather than end-to-end application response time.

## 5. Next Steps

1. Implement and evaluate dense retrieval.
2. Compare BM25 and hybrid retrieval.
3. Review preprocessing of non-informative PDF content.
4. Expand the benchmark with passage-level relevance annotations.
5. Integrate Qwen3 for evidence-grounded question answering.

**Research note:** All current results are based on public FIST documentation and do not represent evaluation using internal TNB REMACO data.