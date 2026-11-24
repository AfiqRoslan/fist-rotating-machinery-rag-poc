# FYP Documentation Hub — Academic Session 2026/2027

**Project:** Industrial Maintenance / Rotating Machinery RAG Research Prototype
**Status (24 Nov 2026):** Working public-USBR-manual proof of concept; research scope and industrial data access are still to be confirmed by supervisors.

This directory is the **living project record** spanning FYP1 and FYP2. It is not a substitute for official university forms or a formatted thesis. Use official UTM templates and obtain supervisor approval where required.

## Start here

| Goal | Document |
| --- | --- |
| Present progress chronologically | [Development log](DEVELOPMENT_LOG.md) · [Actual commits](https://github.com/AfiqRoslan/fist-rotating-machinery-rag-poc/commits/master/) |
| Explain tomorrow's working demo | [Demonstration guide](DEMO_GUIDE.md) |
| Show baseline metrics and caveats | [Experiment A results](EXPERIMENT_A_RESULTS.md) · [Archived results](../results/experiment_A_USBR/) |
| Set up or reproduce the code | [Reproducibility guide](REPRODUCIBILITY.md) |
| Track meetings and instructions | [Meeting log](MEETING_LOG.md) |
| Track decisions and scope changes | [Decision log](DECISION_LOG.md) |
| Find proof for claims and tables | [Evidence register](EVIDENCE_REGISTER.md) |
| Plan FYP1 research | [Research plan](fyp1/RESEARCH_PLAN.md) |
| Review existing papers / models | [Literature review tracker](fyp1/LITERATURE_REVIEW_TRACKER.md) |
| Meet FYP1 submission milestones | [FYP1 checklist](fyp1/SUBMISSION_CHECKLIST.md) |
| Plan FYP2 development | [Implementation plan](fyp2/IMPLEMENTATION_PLAN.md) |
| Plan defensible evaluation | [FYP2 experiment plan](fyp2/EXPERIMENT_PLAN.md) |

## How to maintain this repository

1. **After each coding session:** commit working source changes with a meaningful message; add a dated entry to `DEVELOPMENT_LOG.md` or an issue/PR.
2. **After each formal meeting:** update the meeting record with date, participants, decisions, action items, and links to evidence. Transfer appropriate information to the **official FYP logbook** and obtain supervisor endorsement as required.
3. **For each experiment:** create a new `results/experiment_X_.../` folder containing dataset provenance, exact parameters, benchmark definition, scripts/commit reference, raw outputs, and an interpretation with limitations. Avoid overwriting Experiment A.
4. **For each research article:** record a real citation, methodological comparison, limitation, and relevance. Do not fabricate publications or references.
5. **Before a formal submission:** verify actual university dates and forms; export the report using the required official template; preserve a copy of the submission and assessment feedback in a private folder if it contains personal/confidential information.

## Important boundaries

- **Public USBR corpus only:** this public repository contains no TNB REMACO internal records.
- **PoC ≠ finished thesis:** the observed success of selected questions is not an established retrieval/answer accuracy rate.
- **Protected information:** do not commit industrial datasets, private emails, personal IDs, credentials, supervisor signatures, Turnitin reports, private assessment feedback, or undisclosed correspondence without permission.
- **Official sources:** the uploaded 2026/27 BAI FYP handbook and the current Semester 1 FYP1 schedule govern requirements; dates below are for planning and should be rechecked against announcements.
