# HIVsim paper: project plan (v0.3)

*For Robyn, Daniel and Cliff. Read `vision.md` first.*

## Timeline

| Milestone | Date | Definition of done |
|---|---|---|
| **M1 Scope locked** | Fri 6 Nov | Narrative structure, quantities of interest, model-feature list and harness spec all agreed and turned into issues |
| **M2 Interim deliverable** | Fri 11 Dec | Pilot R2 result for one quantity; harness v0 end-to-end on that question; draft figs 1–4; narrative draft |
| **M3 Full draft** | Fri 19 Feb | All results; benchmark graded; full manuscript |
| **M4 Submitted** | Wed 31 Mar | Co-author round (22 Feb – 19 Mar) done; submitted |

Sprint 1 runs 26 Oct – 11 Dec (M1, M2). Sprint 2 runs 4 Jan – 19 Feb (M3). The Nature Health presubmission enquiry goes out in Sprint 2, week 1.

## People

| | Time | This paper | Other |
|---|---|---|---|
| Robyn | 50% | lead | — |
| Daniel | 25% | ~2 h/wk: review model features; R4 | cost-effectiveness-under-shocks paper (Eswatini), ~8 h/wk |
| Cliff | 10% | v4 support; harness review; cross-citation with lingua franca paper | lingua franca paper |

## Workstreams

| Workstream | Sprint 1 goal | Lead |
|---|---|---|
| **Narrative** | Abstract, results outline, figure list, claims table, and quantities of interest finalised (M1); narrative draft (M2) | Robyn |
| **Model features** | Final list of structural alternatives, each with acceptance criteria (M1); built and tested on v4 (M2) | Robyn, with Daniel reviewing |
| **Admissibility** | Calibration targets, hold-out and fit criteria for "still fits the data"; per-alternative recalibration pipeline | Robyn |
| **AI harness** | Spec of tools, skills and safeguards (M1); v0 end to end on one question (M2) | Robyn, with Cliff reviewing |
| **Analysis** | Pilot R2 on one quantity (M2); full R2 and R3 (M3) | Robyn |
| **Collaboration** | List of graders and reviewers (M2); invitations (Sprint 2) | Robyn |
| **CE paper** | Costing and DALY analyzer in stisim (Nov); scenarios (Dec–Feb); manuscript (Mar) | Daniel |

## Sprint 1 by week

| Wk | Dates | Narrative / features / harness | Daniel | Cliff |
|---|---|---|---|---|
| 1 | 26–30 Oct | Narrative v1 (abstract, results outline, figure list); candidate quantities of interest; feature inventory: what HIVsim-v4 has vs needs | CE scoping doc | HIVsim-on-v4 status check |
| 2 | 2–6 Nov | **M1:** final feature list with acceptance criteria; admissibility criteria; harness spec; issues created | Review feature list; costing analyzer design | Review harness spec |
| 3 | 9–13 Nov | Build features, batch 1; port the attribution analyzer (3 methods) | Costing analyzer build | — |
| 4 | 16–20 Nov | Features, batch 2; recalibration pipeline | Costing analyzer tests | — |
| 5 | 23–27 Nov | Pilot R2 on one quantity (locally, small budget); harness MCP tools | Eswatini cost inputs | — |
| 6 | 30 Nov–4 Dec | Harness v0 + safeguards v0 on the pilot question; draft benchmark question set | Review batch 2 | Review harness v0 |
| 7 | 7–11 Dec | **M2:** draft figs 1–4, narrative draft, recorded demo, Sprint 2 plan | Costing PR merged; scenarios specified | Interim review |

Sprint 2 is planned at the M2 review.

## GitHub project board

The board is a single Projects (v2) board across repos. Issues live where the code lives:

| Repo | Holds |
|---|---|
| `hivsim_paper` | narrative, analysis, figures, collaboration |
| `stisim` | model features, the attribution analyzer, the costing analyzer |
| `starsim` | engine issues |
| harness repo (TBD at M1) | the AI harness |

**Fields**

| Field | Values |
|---|---|
| Status | Backlog / Ready / In progress / In review / Done |
| Sprint | weekly iteration field (S1W1 … S2W7) |
| Workstream | Narrative / Model features / Admissibility / AI harness / Analysis / Collaboration / CE paper |
| Milestone | M1–M4 (repo milestones with the same names and dates) |
| Size | S (<½ day) / M (1–2 days) / L (>2 days: split it) |

**Views**
- **Sprint board:** this iteration, grouped by Status.
- **By workstream:** grouped by Workstream.
- **Roadmap:** timeline by Milestone.
- **Mine:** filtered by assignee.

**Conventions**
- Issue titles start with a verb.
- Each issue states its acceptance criteria and links the claim (C1–C5) or result (R1–R4) it serves.
- Feature issues stay out of Ready until M1 is done.

## Starter issues (Sprint 1)

| # | Issue | Workstream | Milestone | Owner |
|---|---|---|---|---|
| 1 | Draft abstract, results outline and figure list | Narrative | M1 | R |
| 2 | Choose 2–3 quantities of interest and justify each | Narrative | M1 | R |
| 3 | Inventory HIVsim-v4 structural features vs needs | Model features | M1 | R |
| 4 | Finalise structural-alternatives list with acceptance criteria | Model features | M1 | R, D |
| 5 | Define admissibility: targets, hold-out, fit criteria | Admissibility | M1 | R |
| 6 | Write harness spec: tools, skills, safeguards, escalation | AI harness | M1 | R, C |
| 7 | Decide harness repo location | AI harness | M1 | R, C |
| 8 | Port cascade attribution analyzer to stisim (tracked, cascade-weighted, counterfactual) | Model features | M2 | R |
| 9 | Build structural alternatives, batches 1 and 2 (one issue per feature, created at M1) | Model features | M2 | R |
| 10 | Build per-alternative recalibration pipeline | Admissibility | M2 | R |
| 11 | Run pilot R2 on quantity 1 | Analysis | M2 | R |
| 12 | Build harness MCP tools: configure, calibrate, run, report | AI harness | M2 | R |
| 13 | Implement safeguards v0 (provenance, range and unit checks, admissibility gate, escalation) | AI harness | M2 | R |
| 14 | Draft benchmark question set and grading rubric | Analysis | M2 | R |
| 15 | Shortlist external graders and reviewers | Collaboration | M2 | R |
| 16 | Write CE scoping doc | CE paper | — | D |
| 17 | Build costing and DALY analyzer in stisim | CE paper | — | D |
| 18 | Assemble Eswatini cost inputs | CE paper | — | D |

## Risks

| Risk | Mitigation |
|---|---|
| Recalibrating every alternative is expensive | small fixed budget per alternative; VM; the HIVsim posterior as prior; pilot locally first |
| No structural alternative fits, or all of them do | either outcome is a finding; the pilot at M2 shows which before scaling up |
| Harness scope creeps toward a multi-model plugin | the harness operates HIVsim only |
| Overlap with Cliff's paper | Cliff reviews; cross-cite |
| CE paper slips | R4 is optional; nothing in this paper depends on it |
