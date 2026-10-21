# Project plan: 7 weeks (draft v0.1)

*2026-10-21. Builds on `vision.md` and `recon.md`. For refinement.*

## 1. Strategy

**Split the vision into two papers.** Nat Med does not publish platform papers. It publishes a health question answered with evidence, where the tool is the means.

- **Paper A (Nat Med, with Nature Health as the alternative): "Why do HIV models disagree about where transmission comes from?"**
  - Malawi.
  - Rebuild contrasting models in a common language, verify them against the originals, then run CISNET-style model experiments that decompose the 33–75% spread.
  - Show which policy conclusions (testing vs retention) survive.
  - AI-assisted rebuilding is the method, measured, in one display item.
- **Paper B (Nat Comput Sci): the platform paper.**
  - Composability (HIV + syphilis, and HIV + TB if a TB module is ready).
  - The AI benchmark, an MCP server that runs sims, and safeguards enforced in code.
  - Draft in parallel; submit after A.

What the 7 weeks deliver: **Paper A drafted and circulated to co-authors by 11 Dec**, a preprint shortly after, and submission in January once co-authors have signed off. Submitting before co-authors sign off would undermine the collaboration (see `collaboration.md`).

## 2. Paper A design

The Malawi model set spans the published range. Three to four models are in play, and the experiments will report how many of the four are delivered.

| Model | Role | How |
|---|---|---|
| **HIVsim** | ours; ABM; tracks source partner | stisim v3, calibrated to MPHIA 2015/2020 and UNAIDS |
| **EMOD-HIV** | low end (33%); tracks source partner | original, run by Daniel from the Bansi-Matharu Malawi configuration |
| **Goals** | high end (75%); inferred attribution | **rebuilt in v4 lingua franca**, verified against GoalsARM |
| **Optima** | second rebuild (stretch) | Atomica `hiv_dyn` already in v4; verify against Burnet's Malawi project |

**Model experiments.** Each change is followed by recalibration to the same targets, so that a fitted parameter can't silently absorb the change.

- **E1. Attribution method.** Apply tracked source, cascade-weighted and counterfactual zeroing to each model. This measures how much of the spread is definitional.
- **E2. Infectiousness on ART.** Harmonise the U=U threshold and how viral suppression is generated.
- **E3. Diagnosis process.** Random vs risk-targeted testing; a fixed number of tests vs a fixed coverage.
- **E4. ART interruption and re-engagement.**
- **E5. ABM vs compartmental.** Run the rebuilt Goals with `solver='abm'` and `solver='ode'` from the same spec. This isolates the effect of paradigm, which only a common language can do; it is the one experiment unique to the lingua franca.
- **Decomposition.** One change at a time, then a small factorial. Report the share of the range closed by each change, and interactions.
- **Decision consequence.** Rank Malawi testing scale-up against retention improvement under each harmonised configuration, and show where the ranking flips.
- **Out-of-sample check.** Compare against data held out of calibration: the MPHIA 2020 recent-infection estimate, and phylogenetic source-attribution estimates if any are available for Malawi (to check).

## 3. Claims ledger

Levels: V = implemented and validated; I = implemented, not validated; F = feasible with engineering; A = aspirational. Columns: **now** is the current level; **wk 7** is the target.

| # | Claim (Paper A) | Now | Wk 7 | Evidence / acceptance |
|---|---|---|---|---|
| C1 | HIVsim reproduces the Malawi epidemic | F | V | fit to MPHIA 2015 and 2020 (prevalence by age/sex, diagnosed, on ART, VLS) and UNAIDS incidence; posterior from ≥100 draws |
| C2 | A published compartmental model can be faithfully rebuilt in the common language | I (Atomica) | V (Goals) | pre-specified tolerance vs the original on prevalence, incidence, cascade and attribution shares, 2000–2040; **original team signs off** |
| C3 | Agents speed up rebuilding, with humans verifying | I | V | logged effort (person-hours, agent cost, lines of code, iterations to tolerance), with every human correction recorded |
| C4 | A structural diff surfaces the differences that matter | F | I | `ss.diff(goals, optima)` and the HIVsim spec vs Goals; check that it finds the known differences in the Bansi-Matharu discussion |
| C5 | Model experiments explain a large, quantified share of the disagreement | F | V | E1–E5 decomposition with uncertainty |
| C6 | Some policy conclusions are robust across model structures and some are not | F | V | intervention ranking across harmonised configurations |
| — | EMOD, PopART or Synthesis fully rebuilt | A | A | roadmap only |
| — | HIVsim on v4 | F | F/I | parallel track; not on Paper A's critical path |

Paper B claims (composability, AI benchmark, MCP, safeguards) get their own ledger once Paper A is under way.

## 4. People and time

The team has roughly 34 h/week, about 240 hours over the 7 weeks. Agents do most of the building; people decide, verify and write.

| Person | Time | Owns |
|---|---|---|
| Robyn | 50% (~20 h/wk) | science lead; Malawi HIVsim calibration; experiment design; writing; outreach |
| Daniel | 25% (~10 h/wk) | EMOD Malawi reference runs; harmonised output spec; HIVsim switches for EMOD-like structural choices; liaison with Anna Bershteyn |
| Cliff | 10% (~4 h/wk) | v4 owner: reviews the Goals rebuild and `ss.diff`, and unblocks v4 issues |

## 5. Sprints

Sprint 0 runs Wed 21 to Fri 23 Oct. Sprints 1–7 each run Monday to Friday, from 26 Oct to 11 Dec.

| Sprint | Dates | Goal | Deliverables | Owner(s) |
|---|---|---|---|---|
| 0 | 21–23 Oct | Lock scope | decisions in §7; outreach emails drafted | R |
| 1 | 26–30 Oct | Foundations | `HIVCascadeAnalyzer` upstreamed into stisim with all 3 attribution methods and tests; Malawi data assembled (MPHIA, UNAIDS, ART numbers); harmonised output spec written (Bansi-Matharu definitions); outreach sent to EMOD, Goals and Bansi-Matharu/Phillips | R, D |
| 2 | 2–6 Nov | Malawi HIVsim + EMOD reference | HIVsim Malawi calibration (pilot locally, full run on VM); EMOD Malawi rerun with outputs in the harmonised format; GoalsARM building and running with Malawi inputs; **Gate 1** | R, D |
| 3 | 9–13 Nov | Goals rebuild | Goals in v4 spec, written by an agent from GoalsARM source and docs, all effort logged; first verification pass; `ss.diff` v0 | R, C (review), agents |
| 4 | 16–20 Nov | Verification | Goals rebuild within tolerance, or failures diagnosed; HIVsim switches (U=U, testing process, re-engagement) added; E1 attribution experiment run; Optima Malawi verification if time; **Gate 2** | R, D, C |
| 5 | 23–27 Nov | Model experiments | E2–E5 one at a time, with recalibration; decomposition; intervention ranking; **Gate 3** | R, D |
| 6 | 30 Nov–4 Dec | Figures + draft | Figs 1–4 and Extended Data; Methods; full draft | R |
| 7 | 7–11 Dec | Co-author round | draft circulated to the original model teams and the consortium; reproducibility pass (fresh-clone rerun of all plots from `results/`) | R, D |

**Gates**

- **Gate 1 (6 Nov).** Malawi HIVsim fits the data and the Goals team has engaged. If Goals declines or GoalsARM won't run, switch the second rebuild to Optima (Burnet).
- **Gate 2 (20 Nov).** The rebuild is within tolerance. If not, a diagnosed failure to reproduce is itself a result; report it rather than force agreement.
- **Gate 3 (27 Nov).** Is there a decomposition story? If E1 (attribution method) explains most of the spread, that becomes the headline: much of the published disagreement is definitional.

**Parallel track (not on the critical path).** Agents keep porting HIVsim to v4, with Cliff unblocking engine issues. If it passes the v3 summary-agreement test by Gate 2, the paper's HIVsim results move to v4 and every model then lives in one language. Otherwise HIVsim stays on v3 and the paper says so.

## 6. Risks

| Risk | Mitigation |
|---|---|
| Original teams see this as a threat | `collaboration.md`; they sign off on their rebuild before results are shown; co-authorship |
| GoalsARM ≠ the version used in Bansi-Matharu | ask Stover/Glaubius in week 1; verify against their published Malawi outputs as well as the code |
| Recalibration after each change is expensive | fixed small calibration budget per change; VM; reuse the HIVsim Malawi posterior as the prior |
| A v4 bug (e.g. directional beta) affects the Goals rebuild | Goals is compartmental with per-capita force of infection, so check early in S3; Cliff fixes it on v4-rs |
| Attribution differences dominate, making it a "definitions" paper | still a Nat Med-worthy finding if it changes the policy ranking; otherwise Lancet GH |
| Scope creep into Paper B | Paper B work only after Gate 3 |

## 7. Decisions needed now

1. **Country:** Malawi (widest range, EMOD ran it, no HIVsim model yet) or Zimbabwe (`hivsim_zim` exists, but EMOD didn't run it, so Daniel's model drops out).
2. **Split into two papers:** yes or no.
3. **Second rebuild:** Goals, with Optima as fallback?
4. **HIVsim on v4:** off the critical path, as proposed?
5. **Outreach timing:** contact EMOD/Goals/UCL in week 1 (recommended; it sits on the critical path) or after the first results?
