# Development Log — Industrial Maintenance RAG Proof of Concept

**Updated: 24 November 2026**
**Status:** Functional public-manual proof of concept, tested on a Windows development PC and Lenovo Legion Pro 5i. Industrial validation and the full FYP evaluation remain pending.

This log summarizes milestones supported by the Git history and archived results. It does not invent individual commits for every uncommitted change or terminal command.

## Development timeline

| Date | Milestone | Evidence |
|---|---|---|
| 11 Nov 2026 | Drafted a narrower research scope for rotating machinery maintenance, using public USBR FIST manuals as an independent baseline | [Research scope](../FYP_RESEARCH_SCOPE.md) |
| 12 Nov 2026 | Created the initial repository with source downloading, PDF extraction and chunking, BM25, dense and hybrid retrieval, Qwen3 integration, Streamlit UI, evaluation utilities and unit tests | [Initial commit](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commit/f85d402) |
| 12 Nov 2026 | Added pytest dependencies and documented the preliminary BM25 document-level findings | [Testing](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commit/18281e7), [BM25 findings](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commit/7e5388f) |
| 13 Nov 2026 | Revised project README to explain the rotating-machinery scope, objectives, architecture and technologies | [README revision](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commit/e2efe98) |
| By 24 Nov 2026 | Indexed 219 PDF pages into 511 page-labelled chunks; generated and numerically checked a 511 × 384 MiniLM embedding matrix; evaluated BM25, Dense and Hybrid retrieval | [PoC/archive commit](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commit/11b2726), [Experiment A](../results/experiment_A_USBR/) |
| 24 Nov 2026 | Archived the public USBR baseline, manifest, retrieval output files, portable index and two sample generated answers. Six unit tests passed on the development PC | [Experiment manifest](../results/experiment_A_USBR/experiment_manifest.json), [Tests](../tests/test_core.py) |
| 24 Nov 2026 | Cloned the project onto a Lenovo Legion Pro 5i, restored the index, installed MiniLM and Qwen3 locally, and validated question answering and a source citation to FIST 2-1 PDF page 24 | [Portable index](../results/experiment_A_USBR/demo_index_USBR.zip) |
| 24 Nov 2026 | Verified company-specific refusal for an unsupported TNB REMACO rotor question and answer generation without Wi-Fi | [RAG source](../rag_core.py) |
| 24 Nov 2026 | Downloaded three public PDFs, configured Streamlit static serving and verified local PDF page navigation offline, preserving an alternative official online source link | [Offline PDF commit](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commit/2771265) |
| 25 Nov 2026 (planned) | Demonstrate the PoC to the industrial co-supervisor and discuss a relevant industrial problem, available data and permissions | [Demo guide](DEMO_GUIDE.md) |

## Code walkthrough — from source files to grounded answers

1. **Source definitions:** [`sources.json`](../sources.json) tracks the three public manuals, titles, file names and official URLs.
2. **Download:** [`download_data.py`](../download_data.py) retrieves public PDFs into `data/pdfs/`.
3. **Preprocessing:** [`build_index.py`](../build_index.py) and [`rag_core.py`](../rag_core.py) extract text and store page-labelled, overlapping chunks.
4. **Embeddings:** The MiniLM model `sentence-transformers/all-MiniLM-L6-v2` generates 384-dimensional representations for semantic search.
5. **Retrieval:** [`rag_core.py`](../rag_core.py) implements BM25 lexical search, Dense retrieval and Hybrid RRF fusion.
6. **Evaluation:** [`evaluate.py`](../evaluate.py) runs the 12-question benchmark; raw and summary files live under [`results/experiment_A_USBR/`](../results/experiment_A_USBR/).
7. **Generation:** Ollama runs local `qwen3:4b-instruct-2507-q4_K_M` to generate an answer from retrieved source excerpts with numbered citations.
8. **Interface:** [`app.py`](../app.py) provides retrieval settings, source excerpts, local/official PDF-page links and an explicit TNB-specific refusal rule.
9. **Offline portability:** The archived index can be restored without rebuilding. The three downloaded PDFs must be copied to `static/` on each machine to enable local PDF links.

## Verification and boundaries

**Demonstrated:** Local end-to-end answer generation; relevant source retrieval for a vertical-shaft alignment question; link to FIST 2-1 PDF page 24; TNB-specific refusal test; answer generation without Wi-Fi; local PDF page navigation without Wi-Fi; archived Experiment A results.

**Not established:** Formally measured passage-level retrieval quality, robust answer/citation accuracy across many questions, universal hallucination prevention, industry-specific validity, or TNB system integration. A small number of successful demonstrations does not establish those outcomes.

## Where to inspect actual development history

[GitHub commit history](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commits/master/) contains the tracked code revisions. A development log explains the sequence but cannot substitute for Git commit history.

## Research next steps

- Confirm an industrial maintenance problem and suitable, authorized dataset with the supervisors.
- Keep public USBR documents as **Experiment A**; preserve them unchanged if an authorized **Experiment B** industrial corpus is later obtained.
- Build manually reviewed passage/page relevance labels and expand the benchmark.
- Formally evaluate groundedness, citation accuracy, unsupported-answer behavior and repeatable latency.
- Do not upload proprietary TNB REMACO information, industrial credentials or confidential documents to a public GitHub repository.
