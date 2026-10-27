# Sprint plan

*Weekly sprints, Tuesday to Monday. Read with `vision.md` and `prompts.md`, where the P numbers are defined.*

**Team:** Robyn (lead, Optima), Daniel (EMOD, prompts), Cliff (Starsim v4; Robyn reviews and contributes).

| Sprint | Dates | Robyn | Daniel | Cliff | Deliverable |
|---|---|---|---|---|---|
| **1** | 20–27 Oct | Vision; narrative draft; plan | — | — | ✅ `vision.md`, `narrative_draft.md`, `plan.md`, `prompts.md` |
| **2** | 27 Oct–2 Nov | **P0 Optima:** get the Malawi project files, confirm legacy Optima HIV vs Atomica, rerun, export reference outputs. Inventory Optima's components. Draft the P2 and P3 prompts | **P0 EMOD:** locate the MIHPSA Malawi configuration, campaign, demographics, binary and calibrated parameter sets; rerun; export reference outputs. Inventory EMOD's components. Draft the P4 and P1 prompts | Keep developing v4. Answer the "Ask Cliff" list in `prompts.md`. Agree a commit to pin | Both originals rerun with reference outputs in `results/`; draft prompts P1–P4 |
| **3** | 3–9 Nov | Review P4. Test common random numbers on one real swap (paired vs independent variance). Start re-porting HIVsim onto the pinned v4 | **Run P4:** component map and interface spec, with mechanism, inputs and parameters as separate layers | Review P4 for fit with v4 | **Checkpoint:** component boundaries and interfaces approved by all three; CRN decision |
| **4** | 10–16 Nov | **Run P2:** Optima′ rebuild loop. **P3, first half:** common target set | **Run P1:** EMOD′ rebuild loop | Unblock v4 issues raised by the rebuilds | **Checkpoint:** target set approved; first components of both rebuilds pass |
| **5** | 17–23 Nov | P2 continues. **P3, second half:** calibrate HIVsim to Malawi (pilot locally, full run on VM). Add the explicit re-engagement mechanism to HIVsim | P1 continues; handle escalations | Review the rebuilds' use of v4 | HIVsim Malawi calibrated; rebuilds substantially complete |
| **6** | 24–30 Nov | Verify Optima′: as an ODE against the original (2%), and as an ABM against its own ODE (time-step study). Refactor HIVsim to the interfaces | First fidelity pass for EMOD′ (median inside the original's 90% interval) | Swap runner and endpoint unit test (with Robyn) | **Checkpoint:** Robyn signs off Optima′ |
| **7** | 1–7 Dec | First substitution path, HIVsim ↔ Optima′, uncalibrated | Finish verifying EMOD′, or escalate | Support the swap runner | **Checkpoint:** Daniel signs off EMOD′; first path with endpoint identity confirmed |
| **8** | 8–15 Dec | Results outline and interim figures; plan for the January sprints | Paths EMOD′ ↔ Optima′ (the published gap) and HIVsim ↔ EMOD′ | Interim review | **Interim deliverable (15 Dec):** three verified models, first decompositions, interim figures, January plan |

## Still to schedule

These are left for January:
- the compensated (tier-2) pathway;
- the treatment-interruption scenarios;
- final swap design and orderings;
- the full manuscript, co-author round and submission (by 31 March 2027).

## Risks

| Risk | Fallback |
|---|---|
| Common random numbers don't reduce variance across swaps (`SexualNet` isn't CRN-safe when people are born or die) | more seeds; request a CRN-safe partnership network in Starsim |
| The EMOD′ rebuild can't reach tolerance | report the diagnosed cause; partial path (EMOD components in HIVsim, no endpoint test) |
| v4 API changes mid-rebuild | pin a commit; re-pin deliberately and rerun the endpoint test |
| MIHPSA Optima turns out to be legacy Optima HIV, not Atomica | hand-rebuild; the Atomica importer helps only partly |
