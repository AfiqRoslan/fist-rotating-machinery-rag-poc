# FYP 1 working research scope — discussion draft, 11 November 2026

## Title status

**Previously proposed:** Development and Evaluation of a Transformer-Based Retrieval-Augmented Generation Chatbot for Industrial Knowledge Assistance.

**Suggested narrower working title (not approved):** Development and Evaluation of a Retrieval-Augmented Generation Chatbot for Rotating Machinery Maintenance Knowledge Assistance.

The general chatbot title was previously considered too broad. The refined version ties the academic study to a defined engineering corpus. Do not change the official title without Dr Abdulraqeb's approval and any required administrative process.

## Problem statement (proposed, not yet validated by TNB REMACO)

Technical maintenance information about rotating machinery, shaft alignment, lubrication, and mechanical components is distributed across lengthy engineering manuals. Engineers and trainees must locate relevant procedures and explanations manually, potentially increasing search effort. General-purpose chatbots may answer without verifiable support from the designated manuals. An evidence-grounded RAG knowledge assistant could improve document access, but its retrieval effectiveness, factual grounding, and handling of unsupported questions need systematic evaluation.

**Important:** This is an academic problem formulation grounded in public technical documents and the industrial knowledge-assistance idea discussed after the site visit. It is **not** a verified statement that TNB REMACO experiences these exact problems or that a tool improves their operations.

## Research objectives (proposed)

1. **Develop** a transformer-based RAG prototype for question answering over a selected corpus of publicly available rotating-machinery and mechanical-maintenance technical manuals, with traceable PDF-page citations.
2. **Compare** BM25 lexical retrieval, transformer dense retrieval, and reciprocal-rank-fusion hybrid retrieval on a manually curated, domain-specific question dataset using ranking and relevance metrics.
3. **Evaluate** answer groundedness, citation accuracy, unsupported-question behavior, and retrieval/generation response times against clearly described test cases and baselines.

## Research questions

- Does hybrid retrieval return more relevant passage evidence than lexical BM25 or transformer dense retrieval for maintenance-manual questions?
- How accurately does the RAG system answer questions with traceable evidence, compared with an appropriate baseline, and how often does it fail to refuse unsupported queries?
- What trade-offs exist between retrieval effectiveness and response latency under local inference constraints?

## Data and system boundaries

**Independent fallback corpus:** three published U.S. Bureau of Reclamation Facilities Instructions, Standards, and Techniques (FIST) manuals: 2-1, 2-4 and 2-12 (May 2024; PDF page counts 109, 48, 62 respectively).

**Target users:** students, trainee engineers, engineering maintenance learners, and researchers needing document-grounded explanations (not operational maintenance execution).

**Included:** text extraction; chunking; embedding index; document retrieval; local model grounded QA; page citations; comparison; evaluation.

**Not included:** real-time sensor analytics, predictive maintenance diagnosis, rotor fault classification, work-order approval, instructions authorizing hazardous operations, production integration, private company content, equipment-control interfaces, SCADA integration.

**Industrial migration path:** if Thanaraj provides a permitted corpus, keep the same pipeline and conduct a separate case study or domain-adaptation experiment after permission, quality checks and supervisor agreement. Public data remain a separate training/evaluation cohort and are never described as company data. If no company data are received, academic research and deployment remain scoped to public manuals.

## Methods

| Stage | Initial implementation | Planned academic evaluation |
|---|---|---|
| Data | PDF extraction via PyMuPDF, page metadata | Document quality/coverage check |
| Chunking | 165-word overlapping windows, 35-word overlap | Sensitivity study e.g. chunk size/overlap |
| Lexical retrieval | BM25 (k1=1.5, b=0.75) | Passage Recall@5 and MRR with labeled gold chunks |
| Dense retrieval | all-MiniLM-L6-v2 (transformer embedding) | Same gold set; report model versions |
| Hybrid retrieval | Reciprocal Rank Fusion (k=60) | Same gold set, compare baselines |
| Generation | Locally run Qwen3:4b through Ollama | Answer accuracy/grounding, citations, refusal |
| UI | Streamlit | Demonstration only, not performance benchmark |

Page numbers in the UI are *physical PDF pages* so links are reproducible. Future evaluation should manually identify which chunk IDs contain sufficient support for each query. Use 40–60 manually validated questions, including out-of-scope questions, or the number agreed with the supervisor.

## A defensible novelty/contribution (do not overclaim)

A controlled, reproducible comparison of evidence retrieval strategies and citation-grounded answers on an industrial mechanical-maintenance corpus, especially the trade-off between retrieval quality, groundedness and local runtime. The contribution must be supported by experimental evidence and related-work review; building a chatbot alone is insufficient evidence of research novelty.

## Friday discussion: questions requiring approval

1. Confirm the title and research scope, and whether a title amendment is necessary.
2. Confirm the independence of the USBR public-document fallback dataset.
3. Agree on the evaluation protocol and criteria for answer correctness.
4. Determine whether any domain expert will validate question-answer pairs.
5. Determine if the industrial co-supervisor remains formally involved despite unavailable data.
6. Confirm whether a working PoC plus preliminary retrieval metrics are adequate Week 5 progress.
