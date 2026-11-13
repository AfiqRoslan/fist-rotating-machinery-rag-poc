# Rotating Machinery Maintenance RAG System

### Development and Evaluation of a Hybrid Retrieval-Augmented Generation System for Rotating Machinery Maintenance Using USBR FIST Manuals

A Final Year Project (FYP) research prototype that investigates how **Retrieval-Augmented Generation (RAG)** can support technical knowledge retrieval and question answering for rotating machinery maintenance.

The project focuses specifically on **shaft alignment, equipment lubrication, and mechanical maintenance of hydroelectric and large pump units**, using publicly available Facility Instructions, Standards, and Techniques (FIST) manuals published by the U.S. Bureau of Reclamation (USBR).

The research compares **BM25, transformer-based dense retrieval, and hybrid retrieval** to evaluate how effectively relevant maintenance information can be retrieved and used to generate evidence-grounded answers.

> **Project Status — 13 November 2026:** Document preprocessing, BM25 baseline evaluation, and dense embedding generation have been completed. Phase 6 Step 2 (embedding verification) has not started. Hybrid retrieval evaluation and end-to-end RAG testing remain pending.

---

## 1. Project Overview

Industrial maintenance engineers frequently rely on technical manuals, maintenance procedures, and reference documents when investigating equipment issues.

However, locating specific information within lengthy technical documents can be time-consuming, particularly when the information is distributed across multiple manuals.

Traditional keyword-based retrieval may also struggle when users describe engineering concepts using terminology different from that found in the source documents.

This project investigates whether combining lexical retrieval, transformer-based semantic retrieval, and a locally hosted large language model can improve access to relevant rotating machinery maintenance information.

### Research Focus

The research concentrates on three technical knowledge areas:

1. **Shaft Alignment:** Alignment techniques, shaft concentricity, static runout, reverse indicator methods, and face-and-rim measurements.
2. **Equipment Lubrication:** Lubrication practices, lubricant selection, contamination management, and maintenance considerations.
3. **Hydroelectric and Large Pump Maintenance:** Mechanical maintenance activities, inspections, and equipment-related maintenance considerations.

### Project Objectives

1. Develop a document-processing pipeline for extracting and indexing technical maintenance information from USBR FIST manuals.
2. Implement BM25, transformer-based dense retrieval, and hybrid retrieval for maintenance-related question answering.
3. Evaluate the retrieval effectiveness of each approach using a consistent set of technical questions and relevance judgments.
4. Integrate a local large language model to generate answers grounded in retrieved technical passages.
5. Assess retrieval performance, answer groundedness, citation accuracy, and system limitations.

---

## 2. Dataset and Document Sources

The dataset consists of three publicly available technical manuals published by the **U.S. Bureau of Reclamation (USBR)**.

| Document | PDF Pages | Extracted Chunks |
|---|---:|---:|
| FIST 2-1: Alignment of Rotating Machinery | 109 | 251 |
| FIST 2-4: Lubrication of Equipment | 48 | 115 |
| FIST 2-12: Mechanical Maintenance of Hydroelectric and Large Pump Units | 62 | 145 |
| **Total** | **219** | **511** |

### Official Sources

- [FIST 2-1 — Alignment of Rotating Machinery](https://www.usbr.gov/power/data/fist/FIST_2-1_%285-2024%29.pdf)
- [FIST 2-4 — Lubrication of Equipment](https://www.usbr.gov/power/data/fist/FIST_2-4_%285-2024%29.pdf)
- [FIST 2-12 — Mechanical Maintenance of Hydroelectric and Large Pump Units](https://www.usbr.gov/power/data/fist/FIST_2-12_%285-2024%29.pdf)

The documents were published in 2024. Source metadata is maintained in `sources.json`.

### Data Provenance

All documents used for the current proof of concept are public USBR technical manuals.

**This repository does not contain proprietary documents, maintenance records, or operational data belonging to TNB REMACO Sdn. Bhd.**

The original PDFs and generated embedding indexes are processed locally and excluded from Git version control.

---

## 3. System Architecture

The proposed system follows a retrieval-augmented question-answering pipeline.

```text
        USBR FIST Technical Manuals
                    |
                    v
             PDF Extraction
                (PyMuPDF)
                    |
                    v
             Text Chunking
         + Document Metadata
                    |
                    v
             Indexed Corpus
                    |
          +---------+---------+
          |                   |
          v                   v
     BM25 Retrieval     Dense Retrieval
       (Lexical)         (MiniLM)
          |                   |
          +---------+---------+
                    |
                    v
            Hybrid Retrieval
         Reciprocal Rank Fusion
                    |
                    v
           Top-K Relevant Chunks
                    |
                    v
          Context + User Question
                    |
                    v
             Local LLM (Qwen3)
                    |
                    v
          Evidence-Grounded Answer
             + PDF Citations
```

The architecture supports three retrieval configurations:

| Retrieval Method | Description |
|---|---|
| BM25 | Lexical retrieval based on term frequency and document statistics |
| Dense Retrieval | Semantic retrieval using transformer-generated embeddings |
| Hybrid Retrieval | Combination of BM25 and dense rankings through Reciprocal Rank Fusion (RRF) |

The retrieval methods can be compared using identical questions and source documents.

---

## 4. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| PDF Processing | PyMuPDF |
| Text Processing | Python-based document chunking |
| Lexical Retrieval | BM25 |
| Dense Embeddings | Sentence Transformers |
| Embedding Model | `all-MiniLM-L6-v2` |
| Hybrid Retrieval | Reciprocal Rank Fusion (RRF) |
| Local Language Model | Qwen3:4b |
| LLM Runtime | Ollama |
| User Interface | Streamlit |
| Numerical Operations | NumPy |
| Evaluation | Python, CSV, JSON |
| Version Control | Git and GitHub |

The system is designed to run locally without requiring a paid hosted language-model API.

---

## 5. Implementation Progress

The project is being developed incrementally, beginning with document preprocessing and retrieval before proceeding to full RAG evaluation.

| Phase | Implementation | Status |
|---|---|---|
| Phase 1 | Project setup and research scope | Completed |
| Phase 2 | Technical document collection | Completed |
| Phase 3 | PDF extraction and text chunking | Completed |
| Phase 4 | BM25 retrieval baseline | Completed |
| Phase 5 | Preliminary BM25 evaluation | Completed |
| Phase 6 — Step 1 | Dense embedding generation | Completed |
| Phase 6 — Step 2 | Embedding verification | Not Started |
| Phase 6 — Subsequent Work | Dense and hybrid retrieval evaluation | Pending |
| Subsequent Development | End-to-end RAG evaluation | Pending |

### 5.1 Document Preprocessing

The PDF preprocessing pipeline was implemented using PyMuPDF.

The pipeline performs the following operations:

- Extracts text from each PDF page.
- Divides extracted content into overlapping text chunks.
- Associates chunks with their source documents.
- Preserves page numbers and source URLs for citation.
- Stores processed content in JSON format.

**Recorded preprocessing results:**

| Measurement | Result |
|---|---:|
| Documents processed | 3 |
| Total PDF pages | 219 |
| Total text chunks | 511 |
| Empty chunks | 0 |
| Missing page references | 0 |

The extracted content is stored locally in:

`data/index/chunks.json`

These results confirm that the initial text-processing pipeline completed successfully.

They do not establish whether all diagrams, scanned content, tables, or technical figures were extracted correctly.

### 5.2 BM25 Retrieval Implementation

A BM25 retrieval baseline was implemented to identify relevant maintenance passages using lexical matching.

The baseline supports:

- Query-based passage retrieval.
- BM25 relevance scoring.
- Top-K passage ranking.
- Source-document identification.
- PDF-page metadata for retrieved passages.

The baseline index can be generated using:

```powershell
python build_index.py --bm25-only
```

### 5.3 BM25 Preliminary Evaluation

The BM25 retrieval approach was evaluated locally using 12 provisional maintenance-related questions.

Evaluation command:

```powershell
python evaluate.py --mode BM25
```

**Recorded local results:**

| Evaluation Metric | Result |
|---|---:|
| Number of Questions | 12 |
| Top-K | 5 |
| Document Hit@5 | 1.0000 (100%) |
| Document MRR@5 | 0.9583 |
| Mean Retrieval Time | 0.21 ms |

#### Result Interpretation

The BM25 baseline retrieved at least one chunk from the expected source document within the top five results for all 12 provisional questions.

A document-level MRR@5 of 0.9583 indicates that chunks from the expected source documents generally appeared at high ranking positions.

However, these measurements are **document-level proxy metrics**, not manually verified passage-level relevance metrics.

Retrieving the correct source document does not necessarily mean that the retrieved passage contains the correct answer.

Additional evaluation is required before making conclusions about passage retrieval accuracy or answer quality.

### 5.4 Dense Embedding Generation

Transformer-based embedding generation was implemented using:

`sentence-transformers/all-MiniLM-L6-v2`

The model converts text chunks into numerical vector representations for semantic similarity retrieval.

Execution command:

```powershell
python build_index.py --model sentence-transformers/all-MiniLM-L6-v2
```

**Recorded execution results:**

- Processed 511 text chunks.
- Completed 16 out of 16 embedding-generation batches.
- Executed the embedding-generation process locally on CPU.
- Saved the generated embedding matrix as `data/index/embeddings.npy`.
- Updated the corresponding index metadata.

This confirms successful execution of the embedding-generation process.

**Current boundary:** Numerical verification of the embedding matrix has not yet been performed. Dense and hybrid retrieval performance results are not available at this stage.

---

## 6. Preliminary Research Findings

The current implementation has produced several initial findings.

### 6.1 Document Processing

The three USBR manuals can be processed into a structured text corpus containing document and page references.

This provides a foundation for evidence-based retrieval.

### 6.2 Lexical Retrieval Performance

BM25 achieved a 100% document-level Hit@5 score on the initial 12-question benchmark.

This establishes a preliminary lexical retrieval baseline.

The results are limited by the small benchmark size and the absence of verified passage-level relevance annotations.

### 6.3 Transformer Embedding Feasibility

Dense embeddings were successfully generated locally for all 511 indexed text chunks.

This provides the vector representations required for subsequent semantic retrieval experiments.

Embedding verification and retrieval performance evaluation are still required.

### 6.4 Current Evaluation Limitations

The project has not yet established:

- Whether dense retrieval outperforms BM25.
- Whether hybrid retrieval improves retrieval effectiveness.
- Whether retrieved passages correctly answer the questions.
- Whether generated answers are factually grounded in the manuals.
- Whether PDF citations consistently support generated claims.
- Whether the system can reliably reject unsupported questions.

These questions will be investigated in subsequent experimental stages.

---

## 7. Installation and Setup

### Prerequisites

- Windows 10/11 or another compatible Python environment.
- Python 3.12 recommended.
- Git.
- Internet connection for initial dependencies and model downloads.
- Ollama for local answer generation.

Download Ollama from:

https://ollama.com/download

### Step 1 — Clone the Repository

```powershell
git clone https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc.git
cd fist-rotating-machinery-rag-poc
```

### Step 2 — Create a Virtual Environment

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3 — Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4 — Download Technical Documents

```powershell
python download_data.py
```

The script downloads the three USBR FIST manuals listed in `sources.json`.

PDF files are stored in:

`data/pdfs/`

If automated downloading fails, download the PDFs manually using the official source links and preserve the filenames specified in `sources.json`.

### Step 5 — Build the Retrieval Index

For BM25 only:

```powershell
python build_index.py --bm25-only
```

For BM25 and transformer embeddings:

```powershell
python build_index.py
```

The full indexing command generates text-chunk metadata and a dense embedding matrix.

### Step 6 — Configure the Local LLM

Download the Qwen3 model:

```powershell
ollama pull qwen3:4b
```

Ensure Ollama is running before using answer generation.

### Step 7 — Launch the Application

```powershell
streamlit run app.py
```

Open the local address displayed by Streamlit, normally:

`http://localhost:8501`

The interface provides retrieval configuration options, technical questions, retrieved passages, and optional locally generated answers.

**Note:** The interface and generation integration are implemented in source code. Complete end-to-end answer-generation performance has not yet been evaluated.

---

## 8. Evaluation Methodology

The research aims to compare three retrieval approaches under a consistent experimental setup.

### Retrieval Configurations

| Method | Technique | Evaluation Status |
|---|---|---|
| BM25 | Lexical ranking | Preliminary evaluation completed |
| Dense | Transformer embeddings and similarity ranking | Pending |
| Hybrid | BM25 + Dense using RRF | Pending |

### Preliminary Benchmark

The repository includes:

`benchmark_questions.csv`

This file contains 12 initial questions with expected source-document labels.

These questions are provisional and do not constitute a fully validated passage-relevance benchmark.

### Evaluation Commands

```powershell
python evaluate.py --mode BM25
python evaluate.py --mode Dense
python evaluate.py --mode Hybrid
```

The commands produce retrieval records and summary files in the local `results/` directory.

Dense and Hybrid commands should be executed after the complete index has been built and verified.

### Planned Evaluation Metrics

**Retrieval Evaluation**

- Hit@K / Recall@K with properly defined relevance judgments.
- Mean Reciprocal Rank (MRR).
- Retrieval latency.
- Comparison of BM25, Dense, and Hybrid rankings.

**Answer Generation Evaluation**

- Answer relevance and correctness.
- Faithfulness to retrieved evidence.
- Citation accuracy.
- Handling of unsupported or unanswerable questions.
- Response generation latency.

A larger manually validated benchmark is required before drawing final research conclusions.

---

## 9. Development Roadmap

### Completed

- [x] Define the rotating machinery maintenance research scope.
- [x] Select three public USBR FIST technical manuals.
- [x] Implement PDF text extraction.
- [x] Implement overlapping text chunking.
- [x] Preserve document and page provenance.
- [x] Generate 511 text chunks.
- [x] Implement BM25 retrieval.
- [x] Run preliminary BM25 evaluation.
- [x] Generate transformer embeddings using MiniLM.

### In Progress / Next Development Stage

- [ ] Phase 6 Step 2: Verify the embedding matrix and associated metadata.
- [ ] Validate consistency between chunk count and embedding rows.
- [ ] Confirm numerical validity and expected vector dimensions.
- [ ] Test dense semantic retrieval on maintenance questions.
- [ ] Evaluate hybrid retrieval using Reciprocal Rank Fusion.
- [ ] Compare retrieval performance against the BM25 baseline.

### Future Planning

- [ ] Expand the benchmark to approximately 40–60 manually reviewed questions.
- [ ] Annotate relevant source passages and PDF pages.
- [ ] Introduce unanswerable and out-of-domain test questions.
- [ ] Evaluate local Qwen3 answer generation.
- [ ] Measure answer groundedness and citation accuracy.
- [ ] Compare retrieval strategies using validated relevance judgments.
- [ ] Investigate retrieval and generation latency.
- [ ] Improve extraction of technical tables and diagram-heavy documents.
- [ ] Refine the Streamlit interface based on evaluation findings.
- [ ] Investigate additional industrial maintenance documents where access and usage permissions allow.
- [ ] Document final experimental results and research limitations.

---

## 10. Repository Structure

The main project components include:

```text
fist-rotating-machinery-rag-poc/
|
|-- README.md
|-- requirements.txt
|-- sources.json
|-- download_data.py
|-- build_index.py
|-- rag_core.py
|-- evaluate.py
|-- benchmark_questions.csv
|-- app.py
|-- .gitignore
|
|-- data/                  # Local generated data
|   |-- pdfs/              # Downloaded USBR manuals
|   |-- index/             # Text chunks and embeddings
|
|-- results/               # Local evaluation outputs
```

The `data/` and `results/` entries describe local/generated locations. They are not necessarily populated in a fresh Git clone.

### Main Scripts

| File | Purpose |
|---|---|
| `download_data.py` | Download the source PDF manuals |
| `build_index.py` | Extract text, create chunks, and generate embeddings |
| `rag_core.py` | Retrieval and answer-generation logic |
| `evaluate.py` | Run preliminary retrieval evaluation |
| `benchmark_questions.csv` | Store benchmark questions |
| `sources.json` | Store document metadata and source URLs |
| `app.py` | Streamlit user interface |

---

## 11. Project Limitations

Several limitations must be considered when interpreting the system's results.

**Dataset Scope**

The dataset contains only three public technical manuals. These documents cover specific rotating machinery and maintenance topics and do not represent all industrial maintenance procedures.

**Domain Representation**

The manuals originate from the U.S. Bureau of Reclamation. They do not represent TNB REMACO's internal procedures, operational data, or maintenance approval practices.

**PDF Extraction**

The current preprocessing approach primarily extracts textual information. Technical diagrams, scanned pages, and complex tables may require additional processing.

**Evaluation Dataset**

The initial benchmark contains only 12 questions and uses source-document labels rather than validated relevant passages.

**Model Verification**

The embedding generation process has completed, but numerical verification and comprehensive dense retrieval evaluation remain pending.

**Operational Reliability**

The system is a research prototype. Generated answers must not be used as a replacement for qualified engineering judgment, approved maintenance procedures, or safety-critical operational decisions.

---

## 12. Expected Research Contributions

The project is intended to contribute:

1. A reproducible preprocessing and indexing pipeline for public rotating machinery maintenance manuals.
2. An experimental comparison of lexical, transformer-based semantic, and hybrid retrieval approaches.
3. A locally hosted, citation-aware question-answering prototype for technical maintenance knowledge.
4. An evaluation framework for measuring retrieval quality, evidence grounding, and response limitations.
5. Practical findings on the applicability and limitations of RAG for specialised engineering documentation.

These are intended contributions. Final conclusions will depend on the results of the remaining experiments.

---

## 13. References and Attribution

**Document Publisher**

U.S. Department of the Interior — Bureau of Reclamation.

Facility Instructions, Standards, and Techniques (FIST).

Official publications:

https://www.usbr.gov/power/data/fist_pub.html

**Core Technologies**

- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)
- [Qwen](https://github.com/QwenLM)

The source documents remain the property of their respective rights holders where applicable. Users should review source-specific notices before redistribution.

---

## 14. Author

**Afiq Roslan**

Bachelor of Artificial Intelligence  
Faculty of Artificial Intelligence  
Universiti Teknologi Malaysia (UTM)

Final Year Project (FYP 1)  
Academic Session 2026/2027

**Repository:** [fist-rotating-machinery-rag-poc](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc)

---

**Project Classification:** Academic Research Prototype

**Current Research Stage:** Dense Embedding Generation Completed — Embedding Verification Pending
