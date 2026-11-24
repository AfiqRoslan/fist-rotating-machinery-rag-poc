# Reproducing the Public-Manual PoC on Windows

**Reproduction target:** Source code at Git commit `2771265` (24 November 2026), 3 USBR manuals, 511 indexed chunks, MiniLM embeddings, local Qwen3 Instruct. Recheck current `master` when following these instructions later.

## Requirements

- Windows with Python (the laptop was tested with Python 3.13.17); Git; Ollama.
- Internet required for first install and downloading original PDFs/models; no paid model API required.
- Enough disk for Python/PyTorch packages and the 2.5 GB Qwen3 model.

## Setup (PowerShell in repository root)

```powershell
git clone https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc.git
cd fist-rotating-machinery-rag-poc
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ollama pull qwen3:4b-instruct-2507-q4_K_M
```

If `ollama` is not found in a VS Code terminal opened before installation, restart VS Code; or use the installed executable's complete path.

## Restore Experiment A index (no rebuild necessary)

```powershell
New-Item -ItemType Directory -Path .\data\index -Force | Out-Null
Expand-Archive -Path .\results\experiment_A_USBR\demo_index_USBR.zip -DestinationPath .\data\index -Force
.\.venv\Scripts\python.exe -c "import json,numpy as np; d=json.load(open('data/index/chunks.json',encoding='utf-8')); a=np.load('data/index/embeddings.npy'); print(len(d['chunks']),a.shape,bool(np.isfinite(a).all()))"
```

Expected: `511 (511, 384) True`. First-time dense retrieval requires downloading/caching `sentence-transformers/all-MiniLM-L6-v2`.

## Prepare local PDF citations

```powershell
.\.venv\Scripts\python.exe download_data.py
New-Item -ItemType Directory -Path .\static -Force | Out-Null
Copy-Item .\data\pdfs\*.pdf .\static\ -Force
```

**Do not add private TNB/industrial PDFs to `static/`:** Streamlit makes files in this directory accessible to clients of the app. These three PDFs are public USBR manuals; they are intentionally excluded from Git.

## Start the app

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Visit `http://localhost:8501`. Use Hybrid/Top-5 and ask: `What are the objectives of vertical-shaft alignment?`. Check FIST 2-1 PDF p.24 and the local PDF link. Ask an unsupported TNB-specific question to observe the **specific rule-based refusal**.

## Offline mode

Once Qwen3, MiniLM, the local index, packages, and three PDFs are available, text retrieval and local PDF links can work without internet. Test a **cold start** offline before a high-stakes meeting. Official USBR hyperlinks remain internet-dependent, unless browser caching happens to make them available.

## Testing and evaluation

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe evaluate.py --mode Hybrid
```

The archived results in `results/experiment_A_USBR/` are **historical baseline outputs**. A new run can differ due to model/package versions, startup latency, index state or environment; do not overwrite archived files without preserving a new experiment.

## Windows security note

On one Windows 11 laptop, Smart App Control blocked native NumPy/PyMuPDF DLLs. The user elected to switch it off, then verified those imports worked. This is an **environment-specific security trade-off**, not a general prerequisite. Keep Defender and Firewall on; assess re-enablement separately. Do not disable security protections merely to follow this guide.
