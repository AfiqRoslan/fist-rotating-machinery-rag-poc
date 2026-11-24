# FYP1 Research Plan — Living Draft

**Status:** Proposal planning, not an approved final research title or completed academic report. **Updated:** 24 Nov 2026.

## 1. Research background

Industrial maintenance knowledge is documented across manuals and procedures. Searching lengthy documents can involve manual navigation and keyword mismatch. A retrieval-augmented system can retrieve domain text and attach traceable source evidence to model-generated answers. The current feasibility test uses public hydroelectric/rotating-machinery manuals; a specific TNB industrial need is **not yet confirmed**.

## 2. Proposed problem formulation

1. **Document access:** relevant technical passages may be difficult to locate in long, multi-document collections.
2. **Semantic mismatch:** terminology in an engineer's question may differ from the manuals' wording.
3. **Grounding and auditability:** an LLM answer should reference a verifiable original source and handle unsupported questions cautiously.

These are proposed research motivations. Do not assert measured productivity improvements or TNB-specific issues without evidence from literature or the stakeholder.

## 3. Working objectives (academic SV approval pending)

1. Develop a page-cited RAG system over an authorized maintenance document corpus.
2. Compare BM25, transformer embedding Dense, and hybrid RRF retrieval using manually annotated domain questions and relevant passages.
3. Evaluate answer correctness/groundedness, citation support, unsupported-question performance and local inference latency.

## 4. Research questions

- Does hybrid retrieval improve passage relevance beyond BM25 or Dense on a curated technical Q&A set?
- Can locally generated answers be supported by cited source passages, and when should the system abstain?
- How do effectiveness, latency and compute requirements trade off?

## 5. Scope

- **Current corpus:** FIST 2-1, 2-4 and 2-12; 219 pages, 511 chunks (public USBR).
- **Technical stack:** Python; PyMuPDF; BM25; MiniLM; RRF; Ollama/Qwen3; Streamlit.
- **Users:** engineering students/trainees and technical staff researching **documented** knowledge, not performing live equipment diagnosis.
- **Out of scope:** SCADA access, real-time telemetry, machine fault prediction, automatic maintenance approval, engineering safety certification, and current TNB equipment condition.
- **Future data:** any TNB dataset only after permission, anonymization, and security/ethics review as applicable.

## 6. Background work and existing models — to research and cite

- Lexical IR: BM25 baseline, limitations with paraphrases.
- Dense IR: Sentence-BERT style embeddings, similarity and domain mismatch.
- Fusion: reciprocal rank fusion; when hybrid retrieval helps or fails.
- RAG: retrieval and generator separation; hallucination/groundedness issues.
- Domain alternatives: keyword manual search, general-purpose LLM, domain-specific search systems and other published industrial document QA systems.
- Candidate improvements: better chunking, passage-level reranking, stronger abstention, source citation validation, table/figure extraction, domain-specific evaluation and usability testing.

**Do not claim novel architecture** merely for combining standard RAG components. An academic contribution may be a carefully designed and evaluated domain application/comparison.

## 7. Methodology — proposed sequence

1. Define use case and research questions with SV/stakeholder.
2. Review related literature; identify measurable gap and baselines.
3. Document provenance and permissions; ingest PDF sources and preserve original versions.
4. Clean/extract text, chunk by page, record metadata and extraction limitations.
5. Implement/reproduce BM25, MiniLM Dense and RRF Hybrid; control common index and queries.
6. Prepare manually labelled question/passage dataset, including answerable, ambiguous and unanswerable cases.
7. Evaluate retrieval at passage/page level; report appropriate metrics and confidence/limitations.
8. Evaluate generation groundedness, correctness, citations, refusal, runtime and UX; compare justified baselines.
9. Discuss errors and limitations; obtain SV approval for any final FYP1 changes before FYP2.

## 8. Preliminary evidence available now

See [Experiment A](../EXPERIMENT_A_RESULTS.md) and [Development log](../DEVELOPMENT_LOG.md). The 12-question benchmark is **document-level only**. The PoC working on two machines does not complete a formal research evaluation.

## 9. Required decisions / missing work

- Final title and problem statement approved by academic SV?
- Is industrial access feasible? If not, is public-manual-only FYP acceptable?
- What exact research gap do credible papers support?
- Which paper-backed baselines and evaluation scales are expected?
- Are participant/usability/industry validation studies required or feasible?
- Prepare proposal report, poster, required forms and logbook by official dates.

## 10. Suggested report chapter planning

- **Introduction:** background, problem, objectives, scope, contributions, organization.
- **Literature review:** existing systems/models, comparison matrix, limitations, identified research gap.
- **Methodology:** dataset, architecture, algorithms, evaluation protocol, responsible-AI controls, milestones.
- **Preliminary design/results:** PoC evidence clearly distinguished from future evaluation.
- **References:** verified and properly formatted; follow official thesis style.

Check the BAI FYP handbook Chapters 3–8 and supervisor instructions for mandatory format and chapter structure.
