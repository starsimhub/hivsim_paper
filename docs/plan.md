# HIVsim paper: project plan (v0.5)

*For Robyn, Daniel and Cliff. Read `vision.md` first; the full intro is in `narrative_draft.md`.*

## Milestones

| Milestone | Date | Definition of done |
|---|---|---|
| **M1 Scope locked** | Fri 6 Nov | Component list and interfaces; outputs; tolerances; compensating parameter set; ordering protocol; AI role; issues created |
| **M2 Interim deliverable** | Fri 11 Dec | HIVsim Malawi calibrated; Optima-v4 verified on ≥1 output; first HIVsim↔Optima path (tier 1) for one output; tier-2 prototype; EMOD reference outputs and a re-expression plan; narrative draft; draft figures |
| **EMOD gate** | Fri 22 Jan | EMOD-v4 verified, or we switch to the fallback (EMOD components in HIVsim, no endpoint test) |
| **M3 Full draft** | Fri 19 Feb | All three paths for all outputs, tiers 1 and 2; decision relevance; effort; full manuscript |
| **M4 Submitted** | Wed 31 Mar | Co-author round (22 Feb – 19 Mar) done; submitted |

Sprint 1 runs 26 Oct – 11 Dec. Sprint 2 runs 4 Jan – 19 Feb. The Nature Health presubmission enquiry goes out in Sprint 2, week 1.

## People

| | Time | This paper | Other |
|---|---|---|---|
| Robyn | 50% | lead; HIVsim Malawi; Optima re-expression; decomposition engine; writing | — |
| Daniel | 25% | **EMOD:** original Malawi reference runs, guiding the re-expression, verification, plus reviewing the components | CE-under-shocks paper (Eswatini) |
| Cliff | 10% | v4: component interfaces, solver as a component, CRN across hybrids, tier-2 fitting; cross-citation | lingua franca paper |

**Daniel's split needs a decision.** With EMOD in scope, ~2 h/wk is too little; EMOD probably needs ~4–5 h/wk, which pushes the CE paper back by about a month. Options:
- accept the slip;
- or have agents do most of the EMOD re-expression, with Daniel reviewing.

## Workstreams

| Workstream | What it covers | Lead |
|---|---|---|
| Narrative | intro (drafted), results outline, figures, claims, references | Robyn |
| Components | component list, shared interfaces in HIVsim v4, HIVsim's own components behind them | Robyn, with Cliff and Daniel reviewing |
| HIVsim Malawi | data, calibration, validation | Robyn |
| Optima re-expression | Optima HIV Malawi in v4, verified against the original | Robyn (+ agents) |
| EMOD re-expression | EMOD-HIV Malawi in v4, verified against the original | Daniel (+ agents) |
| Decomposition engine | hybrid builder, path runner with CRN, ordering protocol, tier-2 compensation | Robyn, with Cliff reviewing |
| Analysis | paths, contributions across orderings, compensation, decision relevance, figures | Robyn |
| AI / effort | agent-assisted re-expression with effort logged (if confirmed at M1) | Robyn |
| CE paper | costing and DALY analyzer, Eswatini scenarios, manuscript | Daniel |

## Sprint 1 by week

| Wk | Dates | Robyn (+ agents) | Daniel | Cliff |
|---|---|---|---|---|
| 1 | 26–30 Oct | Results outline; draft component list + interfaces; original Optima HIV Malawi running; Malawi data assembled | EMOD Malawi original: rerun and export reference outputs; CE scoping | Review the interface sketch |
| 2 | 2–6 Nov | **M1:** components, outputs, tolerances, compensating set, ordering protocol, AI role; HIVsim Malawi calibration pilot | Review components; map the EMOD Malawi config onto components | Solver-as-component, CRN, tier-2 approach |
| 3 | 9–13 Nov | Optima-v4 components, batch 1; HIVsim Malawi calibration (VM) | EMOD component mapping, continued | — |
| 4 | 16–20 Nov | Optima-v4 batch 2 + first verification pass; port the attribution analyzer | Costing analyzer build | Unblock v4 issues |
| 5 | 23–27 Nov | Hybrid builder + path runner (CRN); HIVsim components behind the interfaces | EMOD re-expression plan (what to build, in what order) | Review hybrid builder |
| 6 | 30 Nov–4 Dec | First HIVsim↔Optima path, tier 1, one output; tier-2 prototype on a few steps | Costing analyzer tests | — |
| 7 | 7–11 Dec | **M2:** draft figures, narrative draft, Sprint 2 plan | M2 review | M2 review |

## Sprint 2 outline (refined at M2)

| Wk | Focus |
|---|---|
| 1–3 | EMOD-v4 re-expression and verification (**gate 22 Jan**); presubmission enquiry |
| 3–5 | All three paths × outputs × orderings, tiers 1 and 2, on a VM |
| 5 | Decision relevance; effort analysis |
| 6–7 | Full draft; reproducibility pass (fresh clone → all plots from `results/`) |

## GitHub project board

The board is a single Projects (v2) board spanning several repos. Each issue lives in the repo whose code or text it concerns:

| Repo | Issues for |
|---|---|
| `hivsim_paper` | narrative, analysis, figures, the Optima and EMOD re-expressions |
| `stisim` | HIVsim components, the attribution analyzer, the costing analyzer |
| `starsim` | engine work: interfaces, solver, CRN |

**Fields**

| Field | Values |
|---|---|
| Status | Backlog / Ready / In progress / In review / Done |
| Sprint | weekly iteration |
| Workstream | the workstreams above |
| Milestone | M1–M4, plus the EMOD gate |
| Size | S / M / L (split L) |

**Views:** this sprint's board; by workstream; a roadmap timeline; issues assigned to me.

**Conventions:** issue titles start with a verb. Each issue states its acceptance criteria and links the result (R1–R5) it serves.

## Starter issues (Sprint 1)

| # | Issue | Workstream | Milestone | Owner |
|---|---|---|---|---|
| 1 | Draft results outline and figure list | Narrative | M1 | R |
| 2 | Add missing refs (Axtell 1996, Kuntz 2011, van Ballegooijen 2011) | Narrative | M1 | R |
| 3 | Draft component list and shared interfaces | Components | M1 | R, C, D |
| 4 | Choose outputs and harmonised definitions | Analysis | M1 | R |
| 5 | Define ordering protocol (forward, reverse, sampled) | Decomposition | M1 | R |
| 6 | Choose tier-2 compensating parameter set | Decomposition | M1 | R, C |
| 7 | Set verification tolerances per output | Optima / EMOD | M1 | R, D |
| 8 | Decide AI role | AI / effort | M1 | R |
| 9 | Run original Optima HIV Malawi; save reference outputs | Optima | M1 | R |
| 10 | Rerun EMOD Malawi; export reference outputs | EMOD | M1 | D |
| 11 | Assemble Malawi data and calibrate HIVsim Malawi | HIVsim Malawi | M2 | R |
| 12 | Re-express Optima components in v4 (one issue per component, created at M1) | Optima | M2 | R |
| 13 | Verify Optima-v4 against the original | Optima | M2 | R |
| 14 | Map EMOD Malawi config onto components; write the re-expression plan | EMOD | M2 | D |
| 15 | Port cascade attribution analyzer (3 methods) | Components | M2 | R |
| 16 | Put HIVsim components behind shared interfaces | Components | M2 | R |
| 17 | Build hybrid builder + path runner with CRN | Decomposition | M2 | R |
| 18 | Prototype tier-2 compensation | Decomposition | M2 | R, C |
| 19 | Run first HIVsim↔Optima path (tier 1, one output) | Analysis | M2 | R |
| 20 | Log re-expression effort | AI / effort | M2 | R |
| 21 | CE scoping doc; costing and DALY analyzer | CE paper | — | D |

## Collaboration

- Each original model remains the authoritative version, and a re-expression must reproduce it. Decomposition ranks no model, and nothing we write uses "winner" language.
- Keep the wider EMOD and Optima groups informed from the start.
- Any other model is re-expressed only with its team taking part: they verify the re-expression and co-author the paper.
- Anyone whose published results we compare sees the comparison before submission.

## Venue notes

- **Nature Health:** Article of 4,000 words and 6 display items; presubmission enquiries accepted.
- **Nature Medicine:** does not take presubmission enquiries.
- **Code:** goes to reviewers; deposit with a DOI on publication.
- **LLM use:** disclosed in Methods.

## Risks

| Risk | Mitigation |
|---|---|
| The EMOD re-expression is too large | do agents' work first and get Daniel's review early; gate on 22 Jan; fallback is a partial path |
| A re-expression can't reach tolerance | diagnose and report the cause; that's what the endpoint test is for |
| HIVsim Malawi calibration takes too long | start in week 1; reuse the Zimbabwe/Zambia priors and workflow |
| Tier-2 fits are unstable | keep the compensating set small; fall back to tier 1 only |
| Many components × orderings × three pairs gets expensive | a VM; CRN; few replicates; sample orderings rather than enumerate |
| Overlap with Cliff's paper | this paper applies the framework; Cliff reviews; cross-cite |
| The CE paper slips | the flagship paper doesn't depend on it |
