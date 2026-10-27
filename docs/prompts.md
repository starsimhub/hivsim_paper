# Prompts

Two parts:

1. **Plan:** the prompts we expect to run, in order, each with its inputs, outputs, acceptance check and human checkpoint. Drafts, refined before running.
2. **Record:** prompts as actually run, copied exactly as typed, each with a short summary of the response and the commit. Follows `starsim/v4_design/admin/prompts.md`.

## Part 1: Plan (draft)

**Decided (27 Oct):** two separate checks. *Fidelity:* each rebuilt model matches its original, within tolerance. *Endpoint identity:* a fully swapped hybrid equals the rebuilt target model exactly.

**Decided (27 Oct): attribution is computed at the path endpoints only.**
- Each endpoint gets the attribution method its own model used.
- Measurement is reported as one explicit step, so the share of the gap that is purely definitional is a result in its own right.

**Options recorded, if the endpoints show a large gap from definitions alone:**
- (a) compute all three methods (tracked source, cascade-weighted, counterfactual zeroing) on every hybrid;
- (b) compute all three on a few key hybrids only;
- (c) compute only tracked source and cascade-weighted on every hybrid. Both are cheap; counterfactual zeroing needs one extra run per cascade stage.

**Open: swap design.** The proposed starting point for each pair:
1. Each single B component swapped into A.
2. Each single A component swapped into B.
3. One full path from A to B, in outside-in order.
4. The same path in reverse.

Revisit once underway.

**Decided (27 Oct): each functional block has three layers:**
- **mechanism** (the code);
- **inputs** (historical program and demographic data);
- **parameters** (calibrated values).

Each layer is swapped separately. By default, all input swaps form one step, which is split out only where it matters.

Optima's costing module was not used in MIHPSA and is out of scope, so Optima is treated as an epidemiological model only.

**Decided (27 Oct): rebuild agents (P1, P2) run on their own in a test-and-fix loop,** with the fidelity checks as pass/fail. Hard rules:
1. **No changing calibrated parameter values to reach tolerance.** Only structure and logic may be fixed.
2. **No changing the shared interfaces.** A model that doesn't fit an interface stops the agent and escalates to Robyn, Daniel and Cliff.
3. **Log every judgement call** wherever the original code or config is ambiguous.
4. **At most ~5 fix attempts per component,** then escalate.

The model owner signs off at the end: Daniel for EMOD, Robyn for Optima.

**Decided (27 Oct):** all hybrids run as agent-based models. Rebuilt Optima is verified as an ODE against the original Optima, and as an ABM against its own ODE form. The ODE-to-ABM switch is treated as a component of its own, swapped first or last on every Optima path.

**Decided (27 Oct):** the component map comes before any re-expression, so that every model is built against the same component interfaces.

| # | Prompt (short) | Inputs | Output | Acceptance | Human checkpoint |
|---|---|---|---|---|---|
| P0 | **Humans, not agents.** Gather the originals and export their reference outputs | Daniel: EMOD-HIV Malawi (config, campaign, demographics, binary version, calibrated parameter sets). Robyn: Optima HIV Malawi project | `raw_results/originals/` (gitignored); reference outputs summarised into `results/` | both originals rerun and match their MIHPSA outputs | Done by Daniel and Robyn |
| P4 | List the atomic components of each model and propose shared interfaces | EMOD source + Malawi config, Optima source + Malawi project, HIVsim/stisim, Starsim v4 | component map + interface spec | each model's behaviour accounted for by exactly one component | **Approve boundaries:** Robyn, Daniel (EMOD), Cliff (v4) |
| P1 | Re-express EMOD-HIV (Malawi) in Starsim v4, against the interfaces | P4 spec, EMOD source + Malawi config, Starsim v4, stisim | `models/emod/` | for each output and year 2000–2040, the rebuilt model's median lies inside the original's 90% interval across seeds | TBD |
| P2 | Re-express Optima HIV (Malawi) in Starsim v4, against the interfaces | P4 spec, Optima source + Malawi project, Starsim v4, stisim | `models/optima/` | within 2% of the original Optima, for each output and year 2000–2040 | TBD |
| P3 | Build a common target set from the data EMOD and Optima actually used, then calibrate HIVsim Malawi to it (calib plugin); score the EMOD and Optima originals on the same set | P0 calibration inputs, Bansi-Matharu 2025 + supplement, calib plugin | `results/targets.csv`, priors, fitted HIVsim, a fit scorecard for all three models | HIVsim fits the common set; scorecard complete | **Approve target set** (Robyn) before calibrating |
| P5 | Refactor HIVsim to the interfaces; design and run the sequential swaps | P1–P4 outputs | swap plan, path results | endpoint identity is exact (unit test, with common random numbers) | TBD |

### P1 (draft)

```text
Implement EMOD in the Starsim architecture.
```

### P2 (draft)

```text
Implement Optima HIV in the Starsim architecture.
```

### P3 (draft)

```text
Extract all the calibration targets and adjustable parameters from the paper. Use the calib plugin and find a fit.
```

### P4 (draft)

```text
List out the atomic components of each model and design the sequential swapping.
```

## Starsim v4 notes (reviewed 27 Oct, `origin/v4-oct27` = `v4` + 1 commit)

- **Base.** Build on `origin/v4`, pinned to a commit, and rerun the endpoint-identity test on every re-pin. The v4-rs work is already in it, under Cliff's naming. Don't merge local `v4-rs`. The `stisim-v4` port targets the old v4-rs API (`target=`, `ss.Capacity`) and needs re-porting.
- **Interfaces.** Starsim doesn't enforce module interfaces (no reads/writes declarations). The P4 interface contract is our own layer, enforced by our own tests.
- **ODE ↔ ABM.**
  - Works for declared models without networks. `SexualNet` has no compartmental form, and per-agent `ss.attr`, clocks and queues are agents-only.
  - So Optima′ should be built from mixing pools or `ss.contacts`, with CD4 × cascade as declared states.
  - Agents take whole time steps, so the ABM-vs-ODE check needs a dt study, not a tight tolerance.
- **CRN (highest risk).**
  - `SexualNet` isn't CRN-safe when people are born or die, so any swap that changes mortality rewires the network.
  - Cliff measured little variance reduction for declared-agent diseases.
  - Draw keys follow transition order, which changed in the latest commit.
  - Endpoint identity can still be exact if names, graph and module order match; check with `sim.hash().model` and `ss.diff`.
  - **Measure paired vs independent variance on one real swap before relying on CRN.**
- **Spec and diff.** `to_spec`, `to_code`, `hash` and `ss.diff` exist; there is no `from_spec`. Code-written modules show up only as class plus parameters, so make swappable components declared where possible.
- **HIV pieces.**
  - Directional `ss.peract` is exact.
  - Modifiers multiply the hazard, not the probability (about a 1% difference from EMOD's convention for acute-phase multipliers).
  - `SexualNet` has one partnership type per network.
  - There is no stock target for ART numbers and no `ss.program()`.
  - The Atomica `hiv_dyn` importer matches Atomica to 1e-6 but doesn't translate junctions, transfers or interactions.
  - There is no EMOD importer; it's listed in `v4_design/todo.md`.
- **Ask Cliff:**
  - Is the EMOD importer planned?
  - Will a stock ART target or `ss.program()` come back, or does it belong in STIsim?
  - Is a compartmental form of `SexualNet` coming?
  - Can transition and distribution naming be kept stable, for CRN?
  - Would he consider optional interface declarations?
  - Could we have a frozen API window for the paper?
- **To confirm:** was MIHPSA Malawi run on legacy Optima HIV or on an Atomica project? If it was legacy Optima, the Atomica importer helps little.

## Part 2: Record

*None yet.*
