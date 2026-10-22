# Project plan (v0.2)

*2026-10-22. Goes with `vision.md` v0.2.*

## Timeline

| Phase | Dates | Ends with |
|---|---|---|
| Sprint 1 | 26 Oct – 11 Dec | **Interim deliverable:** locked narrative (abstract, figure plan, results outline with pilot figures), structural menu implemented, harness v0 working end to end on one question |
| Break | 14 Dec – 1 Jan | — |
| Sprint 2 | 4 Jan – 19 Feb | full runs, harness evaluation, full draft; Nature Health presubmission enquiry in week 1 |
| Co-author round | 22 Feb – 19 Mar | comments in |
| Revise + submit | 22 – 31 Mar | **submitted** |

## People

| Person | Time | This paper | Own work |
|---|---|---|---|
| Robyn | 50% | lead: narrative, structural menu, harness, sensitivity analysis, writing | — |
| Daniel | 25% | ~2 h/wk: review the network and testing switches; R4 worked case | CE-under-shocks paper (Eswatini), ~8 h/wk |
| Cliff | 10% | v4 support; review the harness/MCP design for overlap with starsim AI and his paper; cross-citation | lingua franca paper |

**Daniel's paper** (his outline: 1 month costing integration, 2 months scenarios, 1 month writing):

| Dates | Milestone |
|---|---|
| Nov | Generic HIV costing + DALY analyzer in stisim (layer 2), built on `stisim/logistics` unit costs; Eswatini cost inputs assembled; PR merged by 11 Dec |
| Dec–Feb | Scenarios in `hivsim_eswatini` or a new analysis repo: ART funding loss, supply disruption, intervention stack-rank by time horizon |
| Mar | Manuscript |

Weekly 30-minute check-in with a written deliverable list. That list doubles as the progress record for the grant aim.

## Sprint 1: 26 Oct – 11 Dec

| Wk | Dates | Robyn (+ agents) | Daniel | Cliff |
|---|---|---|---|---|
| 1 | 26–30 Oct | Abstract + figure plan + claims ledger v1; final structural menu; port `HIVCascadeAnalyzer` into stisim with the 3 attribution methods + tests | CE scoping: interventions, costs, DALY weights, shock scenarios; one-page plan | — |
| 2 | 2–6 Nov | Zimbabwe base refreshed on current stisim (from `sti_notification` / `hivsim_zim`); switch batch 1: re-engagement rate, VL thresholds, testing variants | Costing analyzer design | Agree v3/v4 for the paper |
| 3 | 9–13 Nov | Switch batch 2: partnership formation, risk heterogeneity; per-configuration recalibration pipeline (small fixed budget, posterior as prior) | Costing analyzer build; review batch 1 | — |
| 4 | 16–20 Nov | Harness: MCP tools (configure, calibrate, run, report) over stisim, with skills on top; try `paper2mcp` on stisim as a baseline | Costing analyzer tests | Review MCP design |
| 5 | 23–27 Nov | Local pilot of R2: one quantity (undiagnosed share), all switches one at a time; harness v0 end to end on that question | Eswatini cost inputs | — |
| 6 | 30 Nov–4 Dec | Safeguards v0 (provenance log, range/unit checks, forced recalibration, escalation); draft benchmark question set + grading rubric | Review batch 2 | — |
| 7 | 7–11 Dec | **Interim deliverable:** pilot figs 1–4, narrative draft, recorded harness demo, sprint 2 plan; list of graders and external reviewers | Costing PR merged; scenarios specified | Interim review |

## Sprint 2: 4 Jan – 19 Feb (outline, to be refined at week 7)

| Wk | Focus |
|---|---|
| 1 | Presubmission enquiry; full R2 runs on VM (3 quantities × configurations × posterior) |
| 2–3 | Decomposition + interactions; R1 validation figure; harness v1 |
| 4–5 | R3 evaluation: run the benchmark (harness vs baseline, 5 runs), blinded grading by external modellers |
| 6 | R4 worked case from Daniel's scenarios (if ready); all figures final |
| 7 | Full draft; reproducibility pass (fresh clone → all plots from `results/`) |

## Claims ledger

Levels: V = implemented and validated; I = implemented, not validated; F = feasible, still to build. **Now** is today's level; the last two columns are the targets.

| # | Claim | Now | Dec | Mar | Evidence |
|---|---|---|---|---|---|
| C1 | HIVsim reproduces the Zimbabwe epidemic | I (stale) | V | V | joint calibration; hold-out |
| C2 | Key structural assumptions are selectable and each configuration is recalibratable | F | I | V | menu with tests; recalibration diagnostics |
| C3 | Structural choice changes policy-relevant answers, quantifiably | F | I (pilot) | V | R2 decomposition vs published ranges |
| C4 | The harness identifies relevant structural dependencies and runs them correctly | F | I (demo) | V | R3 blinded benchmark |
| C5 | Safeguards catch errors | F | I | V | logged triggers; injected-error tests |

## Risks

| Risk | Mitigation |
|---|---|
| Recalibration × configurations is expensive | small fixed budget per configuration; VM; reuse the posterior as the prior; pilot locally in Sprint 1 |
| Harness work expands into HIVMC | out of scope by definition; the harness operates HIVsim only |
| Overlap with Cliff's paper | composability and solver choice are presented as applications; cross-cite; Cliff reviews |
| External groups uneasy with switches labelled after their models | switches described by mechanism; model mapping reviewed by the groups |
| Daniel's paper slips into March | it's R4 (optional); the flagship paper doesn't depend on it |

## Decisions (my calls; flag any you want changed)

- **Country: Zimbabwe.** `hivsim_zim`, the joint STI calibration and the vddx_zim paper are already there, and MIHPSA Zimbabwe gives a published range to compare against.
- **Harness design:** MCP tools for anything that runs the model; skills for workflow and judgement.
- **Not planned in Sprint 1:** HIV–TB.
