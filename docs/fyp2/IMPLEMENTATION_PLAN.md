# FYP2 Implementation Plan — Draft for Future Semester

**Status:** Future planning only, subject to FYP1 research approval and the FYP2 schedule when published. Do not infer FYP2 deadlines from the FYP1 schedule.

## FYP1 → FYP2 handoff requirements

- [ ] Approved title, problem statement, scope, objectives and research questions.
- [ ] Literature review and clearly stated method comparison / evidence-backed gap.
- [ ] Documented permission and data handling for any industrial dataset.
- [ ] Confirmed benchmark design and evaluation criteria.
- [ ] Saved public USBR Experiment A baseline with code SHA, source versions, and metrics.
- [ ] Supervisor feedback, corrections and official FYP1 report completed.

## Proposed FYP2 workstreams

| Workstream | Scope | Deliverable | Status |
| --- | --- | --- | --- |
| Requirements and data governance | Define precise use case, permitted corpora, anonymization and access | Dataset register, requirements and permissions | Pending |
| Data engineering | Extraction, page-level provenance, cleaning, table/figure handling, versioning | Reproducible ingestion pipeline | Existing PoC; deeper validation pending |
| Retrieval experiments | BM25, Dense, RRF; explore chunking/reranking only if justified | Labelled evaluation set and experiments | Preliminary baseline available |
| Generation and safety | Grounding, citation support, non-answer and unsupported cases | Answer benchmark and safety tests | Limited proof test available |
| End-user evaluation | Relevant stakeholder tasks, usability, task completion time as feasible | Assessment findings | Pending feasibility/approval |
| Engineering quality | Unit/integration checks, failure handling, reproducibility, offline behavior | Test logs and final source tag | Initial tests available |
| Thesis/defense | Write results/discussion/conclusions; document limitations | Supervisor-approved final thesis and demonstration | Pending |

## Industrial data option

If authorized TNB records become available, establish **Experiment B** in a separate data environment. Avoid publishing the files, embeddings, sample excerpts, or identifiable records without permission. Maintain separate preprocessing, versions and evaluation splits so A/B results can be interpreted fairly. The industrial dataset may be unsuitable for a public code repository altogether.

If no authorized industrial data is available, discuss the viability of the public-manual-only FYP with the academic SV; do not silently change the problem statement.

## Evaluation checkpoints

- Review question set and source passage labels with supervisor/domain reader.
- Freeze dataset and method settings before final comparisons.
- Run baselines with consistent query sets and record hardware/software configuration.
- Include error analysis and limitations; do not report preliminary document Hit@5 as answer correctness.
- Confirm the latest official FYP2 assessment schedule and forms when issued.
