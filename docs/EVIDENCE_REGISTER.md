# Evidence Register — Claims to Defend in Reports and Demos

This register links each technical claim to reproducible source artifacts. Recheck that the referenced files have not changed before copying numbers into a report.

| Claim / evidence | Supporting file(s) | Evidence status / caution |
| --- | --- | --- |
| Public USBR manuals; no industrial internal dataset | [`sources.json`](../sources.json), [`experiment_manifest.json`](../results/experiment_A_USBR/experiment_manifest.json) | Confirmed provenance for Experiment A |
| Three manuals, 219 pages, 511 text chunks | [`experiment_manifest.json`](../results/experiment_A_USBR/experiment_manifest.json) | Recorded preprocessing summary; extraction of figures/tables still limited |
| MiniLM embeddings shape 511 × 384 | Archived [portable index ZIP](../results/experiment_A_USBR/demo_index_USBR.zip), manifest | Numerically checked on PC and laptop; package versions may vary |
| BM25/Dense/Hybrid Hit@5 and document MRR@5 | [`retrieval_*_summary.json`](../results/experiment_A_USBR/), [`retrieval_* .csv`](../results/experiment_A_USBR/), [result discussion](EXPERIMENT_A_RESULTS.md) | **Document-level proxies, 12 questions; not passage relevance or answer accuracy** |
| Two archived generated-answer examples | [`rag_responses.jsonl`](../results/experiment_A_USBR/rag_responses.jsonl) | Samples; **not** formal graded answer quality |
| Current code and local model generation | [`rag_core.py`](../rag_core.py), [`app.py`](../app.py) | Functionally tested; reproducibility guide provides commands |
| PDF citation navigates to page 24 | [`app.py`](../app.py), [`DEVELOPMENT_LOG.md`](DEVELOPMENT_LOG.md) | Manually checked FIST 2-1 p.24; not an exhaustive citation-quality study |
| Unsupported TNB question receives refusal | [`rag_core.py`](../rag_core.py), [demo guide](DEMO_GUIDE.md) | Specific programmed pattern; **not comprehensive hallucination detection** |
| Unit tests passed | [`tests/test_core.py`](../tests/test_core.py) | Six local tests reported; run again and save dated output for official evidence |
| Full offline capability | [Demo guide](DEMO_GUIDE.md), [reproduction guide](REPRODUCIBILITY.md) | Offline answer and local PDF link observed; cold-start needs explicit validation before claiming it |

## Future evidence to collect

- Dated screenshots/screen recording of UI showing a source excerpt and verified PDF page.
- Command outputs with environment versions and git SHA, stored as text without sensitive machine or user identifiers.
- Manually validated question/passage relevance labels and answer reference sheets.
- Measured timing on repeated **warm runs**, with platform/model details.
- Supervisor feedback, approvals, and industrial dataset use permission (private unless publishable).
- Dated logbook submissions, assessment feedback, report/poster revisions, and final submissions (private if sensitive).

## Report figures / tables tracking template

| Figure/table ID | Content | Derived from | Verified? | Intended chapter |
| --- | --- | --- | --- | --- |
| Figure X | RAG architecture | `rag_core.py`, `app.py` | Pending review | Methodology / system design |
| Table X | Experiment A dataset sizes | Experiment manifest | Yes | Dataset/preprocessing |
| Table Y | Preliminary Hit@5 / MRR@5 | Retrieval summaries | Yes, proxy caveat required | Preliminary results |
