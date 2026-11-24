# FYP2 Evaluation and Experiment Protocol — Proposed

**Status:** Draft only. Any metric, baseline or comparison in this document must be agreed and justified before final FYP2 experimentation.

## Experimental matrix

| Experiment | Corpus | Method | Outcome | Current stage |
| --- | --- | --- | --- | --- |
| A0 | USBR FIST public manuals | BM25 | Document Hit@5, document MRR@5 | Archived **preliminary**, 12 queries |
| A1 | USBR FIST public manuals | Dense MiniLM | Same document-level proxy metrics | Archived **preliminary**, 12 queries |
| A2 | USBR FIST public manuals | Hybrid RRF | Same document-level proxy metrics | Archived **preliminary**, 12 queries |
| A3 (proposed) | USBR FIST public manuals | All three | **Manually judged passage/page** relevance, P@k/Recall@k/MRR/nDCG as appropriate | Not started |
| A4 (proposed) | USBR FIST public manuals | Local cited RAG | Reference-based answer correctness, groundedness, citation precision, refusal behavior | Not started |
| B (conditional) | **Authorized** industrial text | Baseline and proposed methods | Domain-specific outcome; separate permissions and evaluation | Not available |

## Dataset and query design

- Expand beyond 12 provisional questions; mix fact lookup, definitions, paraphrases, procedures, multi-hop and unanswerable cases.
- Set query-level ground truth at document **and passage/page** granularity; define relevance rubric before judging.
- Record provenance, representative sampling, duplicates, leakage, answer references and annotator agreement where feasible.
- Never describe document-level Hit@5 as passage Recall@5 or answer accuracy.

## Retrieval evaluation

- Use same corpus and test questions for BM25, Dense and Hybrid; log indexed files/hashes and model versions.
- Suggested metrics: P@5, Recall@5, MRR@5 and nDCG@5 **only with correctly specified relevance labels**.
- Separate embedding/model load time from warm retrieval latency; record CPU/GPU hardware.
- Perform per-question error analysis (especially misleading top passages and 'intentionally blank' chunks).

## Generation and safety evaluation

- Build an annotated reference answer/source table. Judge correctness, grounding, citation support and insufficiency/refusal.
- Include questions that are answerable, partly answerable, company-specific and outside corpus scope.
- Existing `TNB|REMACO` refusal rule tests one special case; it is **not a generalized safety classifier**.
- For technical hazards, answer only as educational document search; do not frame generated outputs as maintenance authorization.

## Experiment record template

### Experiment [ID] — [Name]
- **Question / hypothesis:**
- **Dataset provenance / permissions / version:**
- **Commit SHA / environment / model settings:**
- **Evaluation question set and judging rubric:**
- **Methods / comparison baseline:**
- **Raw metrics and links:**
- **Representative successes / failures:**
- **Limitations / confounds:**
- **Conclusion supported by evidence:**
- **Next change and reason:**

## Reporting requirements

Include exact definitions and denominators, dataset scope, baseline descriptions, statistical caveats, error cases, diagrams/tables from raw artifacts, and discussion of what results do **not** establish. A successful visual demo alone does not prove model reliability.
