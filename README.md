# FYP 1 — Industrial Maintenance RAG Chatbot

**Working research prototype source code**, prepared for discussion with Dr Abdulraqeb on Friday 13 November 2026.

**Previously proposed title:** Development and Evaluation of a Transformer-Based Retrieval-Augmented Generation Chatbot for Industrial Knowledge Assistance.

**Domain:** engineering-document retrieval and question answering using public maintenance manuals, as an independent fallback when proprietary industrial data are unavailable.

## Data provenance and research boundaries

All three source PDFs are published by the **U.S. Bureau of Reclamation (USBR)**, *not* TNB REMACO. Official index: https://www.usbr.gov/power/data/fist_pub.html . URLs and filenames are in `sources.json`.

1. FIST 2-1 — Alignment of Rotating Machinery (2024, 109 PDF pages)
2. FIST 2-4 — Lubrication of Equipment (2024, 48 PDF pages)
3. FIST 2-12 — Mechanical Maintenance of Hydroelectric and Large Pump Units (2024, 62 PDF pages)

The software is designed to download and parse these **real documents on your own computer**; the PDFs are **not bundled** because the authoring environment could not fetch external file bytes. This is not an indication that PDFs are unavailable on the official sites. If downloading via Python fails, open the source links in a browser and save each PDF under the exact filenames in `sources.json`, in `data/pdfs/`.

U.S. federal documents are often public domain, but third-party content may be excluded. Review copyright notices and provide publisher attribution. Do not upload or index confidential company material without permission.

## Requirements

- Windows 10/11, Python 3.11–3.14 (Python 3.12 recommended for easier setup), internet during first installation/indexing.
- **Ollama**, installed separately, for optional local Qwen3 chat generation. https://ollama.com/download
- No hosted LLM API key needed.

## Setup (PowerShell in the project folder)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python download_data.py
python build_index.py
ollama pull qwen3:4b
streamlit run app.py
```

If only Python 3.13/3.14 is available, replace the first line with `py -3.13 -m venv .venv` or `py -3.14 -m venv .venv`.

First setup downloads three PDFs, the `all-MiniLM-L6-v2` sentence-transformer (if not cached), and Qwen3. They require internet and local storage. Open the Streamlit URL displayed in your terminal, usually `http://localhost:8501`. Ensure Ollama is running (`ollama serve` if not automatically started).

**Quick retrieval-only fallback:**

```powershell
python build_index.py --bm25-only
streamlit run app.py
```

This works *without* downloading the transformer model or installing Ollama, but it is **BM25 retrieval only** and is **not** the complete transformer-based RAG experiment. Later run `python build_index.py` to enable Dense and Hybrid.

## Implementation pipeline

1. Download PDFs from the official USBR URLs (or place them in `data/pdfs`).
2. Extract **page-level text** with PyMuPDF. Pages with insufficient extractable text are logged; figures, scanned tables, and diagrams are not yet parsed multimodally.
3. Split each page into overlapping 165-word chunks; store original title, filename, PDF page and URL.
4. Compute baseline **BM25** scores with a reproducible internal implementation.
5. Compute **Transformer dense embeddings** using `sentence-transformers/all-MiniLM-L6-v2` (customisable in `build_index.py --model`).
6. Compare BM25 vs Dense vs **Hybrid** rank fusion (RRF).
7. Provide Top-5 passages with clickable PDF-page citations to local **Qwen3:4b** via Ollama.
8. Prompt model to avoid unsupported claims and request source-number references. A separate rule refuses queries explicitly asking about TNB/REMACO, because no such documents are present. This is not a substitute for rigorous out-of-domain or hallucination evaluation.
9. Test preliminary document-level retrieval; manually label gold passages/pages for publication-quality metrics.

## Experiments

```powershell
python evaluate.py --mode BM25
python evaluate.py --mode Dense
python evaluate.py --mode Hybrid
```

Saves result tables in `results/`. The supplied `benchmark_questions.csv` contains **12 provisional questions and expected source-document labels**, not expert-approved chunk/page relevance judgments. Its metrics (`document_hit_at_k`, `document_mrr_at_k`) are **document-level proxies**, not academically valid passage Recall@5 or passage MRR until a proper gold standard exists. Questions 7–12 need review against the PDFs after indexing.

For the actual FYP, create 40–60 **manually verified** queries, expected relevant PDF passage/page IDs, and answer references (some deliberately unanswerable). Freeze the dataset, queries, retrieval configurations, and model versions before final evaluation. Add answer-groundedness, citation accuracy, refusal behavior, and answer/latency comparisons. The BM25 score and RRF fusion should also be justified in the literature review.

## Demonstration questions

- What is static runout in rotating machinery?
- What is the difference between the face-and-rim and reverse indicator alignment methods?
- Why is lubrication important for rotating equipment?
- What maintenance issues are associated with large pump units?
- What is TNB REMACO's internal maintenance approval process? **Expected out-of-domain question: answer should decline.**

Demo flow: show PDFs → BM25 retrieval → Dense retrieval → Hybrid retrieval → Qwen3 answer with PDF evidence → unanswerable question → preliminary evaluation output.

## Next steps with Dr Abdulraqeb

Ask whether to formally narrow the title to **Development and Evaluation of a Retrieval-Augmented Generation Chatbot for Rotating Machinery Maintenance Knowledge Assistance**. This is a suggested refinement, not an approved title. Confirm whether using public maintenance documents is an acceptable independent FYP corpus, and whether to keep the TNB REMACO collaboration as an optional later case study.

**Known limitations:** public hydropower/pump manuals are industrial maintenance documents but not REMACO company procedures; they are not equivalent to a validated REMACO dataset. Raw PDF extraction can fail on diagram-heavy pages. Local Qwen3 output has not been independently benchmarked. A prototype is not an engineering maintenance approval system.

## Test locally

```powershell
python -m pip install pytest
python -m pytest -q
```

The packaged test suite checks chunk provenance, BM25 ranking, RRF, PyMuPDF extraction, and an offline miniature corpus. It does **not** establish that the real 219-page source corpus was successfully downloaded/indexed on the user's machine.
