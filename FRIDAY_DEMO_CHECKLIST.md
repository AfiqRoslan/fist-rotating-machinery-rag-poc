# FYP 1 — Friday, 13 November 2026: supervisor demonstration

## Current status (code package)
- [x] FYP design recovered: Transformer-based RAG for industrial knowledge assistance
- [x] Public technical manuals identified from official Bureau of Reclamation listing
- [x] Source-downloader, page-preserving extraction, overlap chunking implemented
- [x] BM25, transformer embedding retrieval, hybrid RRF, Qwen3 API modules written
- [x] Streamlit evidence and answer user interface implemented
- [x] Preliminary document-level benchmark/test scripts provided
- [ ] Download the three source PDF files on your PC
- [ ] Run PDF extraction/indexing and inspect the extracted content
- [ ] Pull Qwen3 locally, open Streamlit, test real question answering
- [ ] Execute BM25, Dense and Hybrid retrieval benchmarks on real manuals
- [ ] Manually verify retrieved passages and output citations against PDFs
- [ ] Review scope/title and obtain academic feedback from Abdulraqeb

## Suggested Wednesday/Thursday priority order
1. Complete setup from README.md. If download fails, use browser and manual copy.
2. Show ingestion summary: pages successfully indexed, number of chunks, low-text pages.
3. Test at least three verifiable questions. Open cited official PDF pages.
4. Show one out-of-domain question and discuss unsupported-answer handling.
5. Run three retrieval strategies and save results; do not overclaim document-level proxy scores.
6. Bring title, objective, baseline, evaluation questions, data-source provenance.

## Decisions to request from Dr Abdulraqeb
- Is the original long title acceptable, or should the research scope be narrowed to rotating machinery maintenance?
- Are these USBR FIST manuals a valid fallback dataset for a standalone academic FYP?
- Is BM25 vs dense vs hybrid a sufficient method comparison, or should there be a non-RAG / LLM-only baseline?
- How many manually labelled technical questions and answer references are expected for the final evaluation?
- If Thanaraj provides no data, can the project proceed unchanged as an independent engineering-document RAG research project?
- Does the change need a formal Week 4–7 title amendment?

## What to say accurately
"I have implemented an independent, modular RAG prototype that can ingest publicly available rotating-machinery maintenance manuals. The system includes BM25, transformer-based dense retrieval, hybrid retrieval and a local Qwen3 answer generator. I am now testing it against the real manuals and developing a verified question set. Industrial validation with TNB REMACO remains dependent on confirmed access, so the academic contribution does not rely on their data."

Only say "I have tested it against the real manuals" after you have actually run it and verified results on your computer.
