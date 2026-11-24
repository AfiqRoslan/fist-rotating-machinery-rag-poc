# FYP1 Literature Review Tracker

**Start with verified academic literature.** Do not invent citations, DOIs, experimental numbers, model comparisons or claims. The table below is a research plan, not a completed literature review.

| Topic / search direction | Example search terms | What to extract from real papers | Status |
| --- | --- | --- | --- |
| RAG foundations | retrieval augmented generation knowledge intensive NLP | Problem, retrieval/generator roles, limitations, references | To research |
| BM25 lexical baselines | BM25 probabilistic information retrieval | Why strong for technical exact terms; weaknesses | To research |
| Sentence-BERT / embeddings | sentence transformers semantic search | Embedding architecture, normalization, evaluation and domain limitations | To research |
| Hybrid retrieval / RRF | reciprocal rank fusion lexical semantic search | Fusion equation, ranking behavior, comparable baselines | To research |
| Technical document QA | industrial maintenance document QA RAG | Data types, user task, relevant metrics, shortcomings | To research |
| Evidence and citation support | RAG faithfulness grounding citation accuracy | Hallucination, evidence fidelity, abstention methods | To research |
| Retrieval evaluation | nDCG MRR Recall at k passage relevance | Query judging protocol, labels, metrics | To research |
| PDF extraction | technical PDF tables figures OCR extraction | Failure cases, layout sensitivity, reproducibility | To research |

## Paper record template

### P-001 — [Verified title]

- **Full citation (authors, year, venue, DOI/URL):**
- **Research problem and domain:**
- **Dataset and size:**
- **Existing model/system described:**
- **Methodological details:**
- **Evaluation metrics and results (with exact cited table/page):**
- **Strengths:**
- **Limitations / unresolved gap:**
- **How it informs this FYP design:**
- **Relevant quote/page for later thesis paraphrase:**
- **Read/verified on:**

## Synthesis template (after reading papers)

| Prior approach | Evidence in papers | Weakness for maintenance manuals | Proposed measurable improvement | Evaluation required |
| --- | --- | --- | --- | --- |
| Pure keyword retrieval | [Citation pending] | Terminology variation | Compare with Dense/Hybrid | Passage relevance at k |
| Dense-only retrieval | [Citation pending] | May lose exact technical identifiers | Add lexical matching via RRF | Rank/relevance metrics |
| Unrestricted LLM answering | [Citation pending] | Unsupported claims and citations | Evidence constrained generator + checks | Human evaluation, refusal cases |

**Gap statement must be evidence-backed.** A lack of evaluation on *this specific small dataset* alone may not establish an academically strong research novelty claim.
