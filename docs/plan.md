# HIVsim paper: project plan (v0.4)

*For Robyn, Daniel and Cliff. Read `vision.md` first; the full intro is in `narrative_draft.md`.*

## Milestones

| Milestone | Date | Definition of done |
|---|---|---|
| **M1 Scope locked** | Fri 6 Nov | Component list and interfaces agreed; outputs agreed; recalibration design and AI role decided; Optima verification tolerances set; issues created |
| **M2 Interim deliverable** | Fri 11 Dec | Optima in v4 passes verification for at least one output; first full substitution path (one ordering) for one output; narrative draft; draft figures |
| **M3 Full draft** | Fri 19 Feb | Full 2^k decomposition for all outputs; decision-relevance result; full manuscript |
| **M4 Submitted** | Wed 31 Mar | Co-author round (22 Feb – 19 Mar) done; submitted |

Sprint 1 runs 26 Oct – 11 Dec (M1, M2). Sprint 2 runs 4 Jan – 19 Feb (M3). The Nature Health presubmission enquiry goes out in Sprint 2, week 1.

## People

| | Time | This paper | Other |
|---|---|---|---|
| Robyn | 50% | lead | — |
| Daniel | 25% | ~2 h/wk: review the component interfaces and the network/cascade components; possible second model pair (EMOD-like) | CE-under-shocks paper (Eswatini), ~8 h/wk |
| Cliff | 10% | v4: component interfaces, solver as a component, CRN across hybrids; cross-citation | lingua franca paper |

## Workstreams

| Workstream | What it covers | Lead |
|---|---|---|
| **Narrative** | Intro (drafted), results outline, figure list, claims; references | Robyn |
| **Components** | Define the component boundaries and shared interfaces in HIVsim v4 so each one can be swapped; one module or option per component per model | Robyn, with Cliff and Daniel reviewing |
| **Optima re-expression** | Optima HIV Zimbabwe in v4 as components; verified against the original Optima run | Robyn (+ agents) |
| **Decomposition engine** | Hybrid builder (pick a component from A or B), 2^k runner with CRN, Shapley attribution and interactions, endpoint check | Robyn, with Cliff reviewing |
| **Analysis** | Outputs, decomposition, decision relevance, figures | Robyn |
| **AI harness** | Depends on the M1 decision: agent-assisted re-expression with logged effort (recommended) | Robyn |
| **Collaboration** | Optima team informed; invitations for future model pairs; co-author round | Robyn |
| **CE paper** | Costing and DALY analyzer in stisim; Eswatini scenarios; manuscript | Daniel |

## Sprint 1 by week

| Wk | Dates | Robyn (+ agents) | Daniel | Cliff |
|---|---|---|---|---|
| 1 | 26–30 Oct | Results outline + figure list; draft component list + interface sketch; get the original Optima HIV Zimbabwe project running; list outputs | CE scoping doc | Review component sketch for v4 fit |
| 2 | 2–6 Nov | **M1:** components and interfaces final; recalibration design; AI role decided; verification tolerances; issues created | Review components; costing analyzer design | Solver-as-component and CRN plan |
| 3 | 9–13 Nov | Optima in v4: demography, natural history, cascade components (agent-assisted, effort logged) | Costing analyzer build | — |
| 4 | 16–20 Nov | Optima in v4: mixing, interventions, parameters; first verification pass | Costing analyzer tests | Unblock v4 issues |
| 5 | 23–27 Nov | Port the attribution analyzer (all 3 methods; needed to compare like with like); hybrid builder; HIVsim components behind the same interfaces | Eswatini cost inputs | Review hybrid builder |
| 6 | 30 Nov–4 Dec | Verification within tolerance on ≥1 output; first substitution path, one output, one ordering | Review network/cascade components | — |
| 7 | 7–11 Dec | **M2:** draft figures, narrative draft, Sprint 2 plan | Costing PR merged; scenarios specified | Interim review |

Sprint 2 (planned at the M2 review): full verification, the 2^k runs on a VM, Shapley decomposition, decision relevance, R4 effort analysis, the full draft, and a reproducibility pass (fresh clone → all plots from `results/`).

## GitHub project board

The board is a single Projects (v2) board across repos. Issues live where their code lives:

| Repo | What its issues cover |
|---|---|
| `hivsim_paper` | narrative, analysis, figures, collaboration, Optima re-expression |
| `stisim` | HIVsim components, the attribution analyzer, the costing analyzer |
| `starsim` | engine work: interfaces, solver, CRN |

**Fields**

| Field | Values |
|---|---|
| Status | Backlog / Ready / In progress / In review / Done |
| Sprint | weekly iteration (S1W1 … S2W7) |
| Workstream | the eight workstreams above |
| Milestone | M1–M4 |
| Size | S (<½ day) / M (1–2 days) / L (split it) |

**Views**
- Sprint board (this iteration, grouped by Status)
- By workstream
- Roadmap (timeline by Milestone)
- Mine

**Conventions**
- Issue titles start with a verb.
- Every issue states its acceptance criteria and links the result (R1–R4) it serves.

## Starter issues (Sprint 1)

| # | Issue | Workstream | Milestone | Owner |
|---|---|---|---|---|
| 1 | Draft results outline and figure list | Narrative | M1 | R |
| 2 | Add missing references (Axtell 1996, Kuntz 2011, van Ballegooijen 2011) | Narrative | M1 | R |
| 3 | Draft component list and shared interfaces | Components | M1 | R, C, D |
| 4 | Choose outputs and harmonised definitions | Analysis | M1 | R |
| 5 | Decide recalibration design for hybrids | Decomposition engine | M1 | R |
| 6 | Decide AI harness role | AI harness | M1 | R |
| 7 | Run original Optima HIV Zimbabwe; save reference outputs to `results/` | Optima re-expression | M1 | R |
| 8 | Set verification tolerances per output | Optima re-expression | M1 | R |
| 9 | Re-express Optima components in v4 (one issue per component, created at M1) | Optima re-expression | M2 | R |
| 10 | Verify Optima-v4 against the original | Optima re-expression | M2 | R |
| 11 | Port cascade attribution analyzer (tracked, cascade-weighted, counterfactual) | Components | M2 | R |
| 12 | Put HIVsim components behind the shared interfaces | Components | M2 | R |
| 13 | Build hybrid builder + single-path runner with CRN | Decomposition engine | M2 | R |
| 14 | Run first substitution path for one output | Analysis | M2 | R |
| 15 | Log re-expression effort (hours, agent cost, corrections) | AI harness | M2 | R |
| 16 | Notify Optima team; shortlist future collaborators | Collaboration | M2 | R |
| 17 | Write CE scoping doc | CE paper | — | D |
| 18 | Build costing and DALY analyzer in stisim | CE paper | — | D |
| 19 | Assemble Eswatini cost inputs | CE paper | — | D |

## Risks

| Risk | Mitigation |
|---|---|
| Optima's original can't be reproduced in v4 within tolerance | diagnose and report the cause; the endpoint test exists for exactly this |
| The network ↔ mixing swap is ill-defined | treat the paradigm (solver) as its own component; define the swap at M1 with Cliff |
| 2^k runs × uncertainty are expensive | k ≤ 6; a VM; CRN keeps replicate counts low |
| Recalibration choice weakens the additivity claim | decide at M1; report both if needed |
| Overlap with Cliff's paper | the paper applies the framework, and Cliff reviews; cross-cite |
| CE paper slips | the flagship doesn't depend on it |
