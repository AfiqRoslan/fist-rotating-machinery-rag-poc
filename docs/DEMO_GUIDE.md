# Demonstration Guide — 25 November 2026

**Audience:** TNB REMACO industrial co-supervisor. **Purpose:** Show an operational research PoC, explain measured preliminary results, and request guidance on a suitable industrial problem and authorized dataset.

## Key message

> This is a working, locally hosted proof of concept for searching rotating-machinery maintenance manuals with Hybrid RAG. It uses public USBR FIST documentation, **not TNB REMACO data**. The goal of this meeting is to identify a practical industrial use case and confirm whether suitable records can be shared for an FYP study.

## Five-minute walkthrough

1. **Context and scope (30 seconds):** Three public maintenance manuals, 219 pages, 511 chunks. Explain the limitation: it cannot establish live equipment condition or company procedures.
2. **Architecture (45 seconds):** PDF -> page-preserving chunks -> BM25 + MiniLM -> RRF Hybrid -> source passages -> local Qwen3 -> cited answer. Show [`rag_core.py`](../rag_core.py) and [`app.py`](../app.py) on GitHub.
3. **Positive test (90 seconds):** Ask `What are the objectives of vertical-shaft alignment?`, use Hybrid / Top-5 / Ollama on, expand Source [1], and open FIST 2-1 PDF page 24. Click **local PDF** link for offline access, or official link when online.
4. **Unsupported query (45 seconds):** Ask `What is the current condition of TNB REMACO's turbine rotor, and what maintenance should be performed?` The prototype should refuse company-specific claims. This is a narrow programmed safeguard, not a comprehensive safety guarantee.
5. **Results and next steps (90 seconds):** Open [Experiment A results](EXPERIMENT_A_RESULTS.md). Clarify that the 12-question scores are *document-level proxies*, not answer-level performance. Request domain problem and authorized data guidance.

## Questions for TNB REMACO

- Which maintenance knowledge-retrieval problem is useful to engineers or technicians?
- Are any **already-existing** and shareable maintenance manuals, SOPs, work orders, historical fault descriptions, inspection reports or text/tabular datasets available?
- Can non-sensitive or anonymized samples be shared? Who can authorize access and approve research use?
- Is there a specific equipment class or maintenance workflow that makes a feasible Bachelor of AI FYP?
- What would count as success for an industrial user: relevant-document retrieval, correct cited passages, less search time or something else?
- If internal data cannot be provided, would feedback on a public-manual-only study be useful?

## Laptop pre-demo check

1. Ensure the correct repository is open and latest Git commit is present.
2. Confirm Ollama is running and `qwen3:4b-instruct-2507-q4_K_M` is present.
3. Ensure `data/index/chunks.json` and `embeddings.npy` are restored from the archive.
4. Ensure three public PDFs exist in `static/` for offline page navigation. This folder is deliberately **not committed** to GitHub.
5. From the project virtual environment, run `python -m streamlit run app.py`.
6. Open `http://localhost:8501`, test a known question and its local citation; keep the Streamlit process running.
7. Internet is not required for tested local retrieval, local generation and locally served citation PDFs. Online source links may require Wi-Fi.

## Reproducing the offline PDF setup on another computer

```powershell
python download_data.py
New-Item -ItemType Directory -Path '.\static' -Force | Out-Null
Copy-Item '.\data\pdfs\*.pdf' '.\static\' -Force
```

The committed `.streamlit/config.toml` enables local static serving. **Only public USBR manuals** should be placed in the exposed static folder; do not publish confidential TNB REMACO files here.

## Evidence and limitations

- [Development log](DEVELOPMENT_LOG.md)
- [Results and limitations](EXPERIMENT_A_RESULTS.md)
- [Raw archived experiment](../results/experiment_A_USBR/)
- [Complete commit history](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commits/master/)

This prototype is for research demonstration and educational reference only. It must not be used for operational maintenance authorization, real-time condition diagnosis or safety-critical decisions.
