# HIVsim paper: vision (v0.5)

*Builds on `narrative_draft.md`.*

**Target:** Nature Health (Article). Reach: Nature. Fallback: PNAS.
**Submit by:** 31 March 2027. **Platform:** Starsim v4.

## Problem

Calibrated HIV models agree on what is observed and diverge on the unobserved quantities that policy depends on. In Zimbabwe they attributed 30–65% of transmission to undiagnosed people (Bansi-Matharu 2025), and 35–64% of HIV deaths fell among people on ART (Bansi-Matharu 2026). This is equifinality: calibration targets constrain only a few combinations of inputs, so many parameter sets and structures fit equally well. Isolating assumptions one at a time is the only way to explain a divergence, and today it is very costly because each assumption is embedded in its own codebase.

## Idea

Make model differences **decomposable**, not just describable.

- **Re-express each model** in a common framework, as interchangeable components.
- **Substitute components one at a time** from model A to model B, and record each output at every step.
- **Check the endpoint.** The full hybrid *is* model B and must reproduce B's original results. This verifies the re-expression, and guarantees that the steps sum to the total gap.
- **Report order-dependence; don't hide it.** Components interact, so a component's contribution depends on when it is swapped. That is inherent: with many components there is no order-free answer to compute. We report each contribution across several orderings (forward A→B, reverse B→A, and a sample of orderings where compute allows), and flag the components whose contribution is order-sensitive. Those are the interacting assumptions, which is a finding in itself.
- **Use common random numbers** (native to Starsim), so the change from one swap isn't lost in simulation noise.

## Recalibration: the hard part

Ideally every hybrid would be recalibrated, and what it takes to restore fit would be informative in its own right. If A with one of B's components only fits when β moves to 0.99, then the data are telling us that component is tightly constrained. Full recalibration of every hybrid is not feasible, so we propose three tiers:

| Tier | What | Status |
|---|---|---|
| 1. Uncalibrated path | Swap components, including the calibrated parameter set, without refitting. The endpoint identity holds exactly. | core |
| 2. Compensated path | At each step, refit a small fixed set of compensating parameters (e.g. β plus one or two others) to the same targets. Record the **compensation needed** as a diagnostic of how strongly the data constrain each component. | proposed core; a low-dimensional fit per hybrid is cheap |
| 3. Full recalibration | Refit every free parameter of every hybrid. | out of scope; discussed as the ideal |

Tier 2 turns the hard problem into a measurement. The question becomes not only what each component contributes to the gap, but also how much the data push back when it is swapped.

## Demonstration

**Models.** We are authors on all three.

| Model | Type | Notes |
|---|---|---|
| HIVsim | agent-based (ABM) | structured sexual network; tracks the source of each infection |
| EMOD-HIV | ABM | partnership network; tracks the source of each infection |
| Optima HIV | compartmental | mixing between groups; attribution inferred |

**Pairs.** There are three paths: HIVsim↔Optima, HIVsim↔EMOD and EMOD↔Optima. The EMOD↔Optima path decomposes a gap from published MIHPSA results directly. The two ABM↔compartmental paths include the change of paradigm itself (the network vs mixing swap, using the v4 solver; we cite Cliff's paper).

**Setting: Malawi** (my call). It is the only MIHPSA country where both EMOD and Optima ran. It needs a new HIVsim Malawi calibration.

**Components.** More than 6 are expected; the list is finalised at M1. The draft groups are:
- output definition (attribution method);
- demography;
- partnership formation;
- mixing;
- risk heterogeneity;
- sex work;
- condoms;
- VMMC;
- transmission (per act or per partnership);
- natural history (stages, CD4);
- infectiousness on and off ART;
- mortality;
- testing;
- linkage;
- ART initiation;
- interruption and re-engagement;
- viral suppression;
- PMTCT;
- PrEP;
- time step / solver;
- calibrated parameters.

**Outputs:**
- share of transmission from undiagnosed people;
- share of HIV deaths on ART;
- incidence;
- one intervention ranking (to test decision relevance).

## Results

- **R1. Verification.** HIVsim fits Malawi; the v4 re-expressions of Optima and EMOD reproduce their originals within pre-agreed tolerances.
- **R2. Decomposition.** For each of the three pairs and each output: component contributions across orderings, and which components are order-sensitive.
- **R3. Compensation.** The tier-2 compensation each swap requires: which components the data constrain, and which they don't.
- **R4. Decision relevance.** Does the intervention ranking change along any path?
- **R5. Effort.** What it cost to re-express and decompose, compared with the stepwise approach (Hontelez 2013).

## Claims and non-claims

| We claim | We do not claim |
|---|---|
| Model differences can be decomposed along verified substitution paths | An order-free attribution |
| Re-expressions can be verified against originals, and were verified for Optima and EMOD | That a common framework makes models equivalent without verification |
| The compensation each swap needs shows which components the data constrain | Full recalibration of hybrids |
| For three models in Malawi, we quantify what drives the gaps in policy-relevant outputs | That this generalises to every model or setting |

## Open questions

1. **AI's role.** Recommended: agent-assisted re-expression from each model's code and docs, verified against the original, with effort logged (R5).
2. **The compensating parameter set for tier 2.** It must be common across models: β, plus what else?
3. **Feasibility of the EMOD re-expression.** It is the largest model and the biggest risk. The fallback is a partial path: EMOD components swapped into HIVsim, with no endpoint test.

## Out of scope

- A multi-model plugin.
- Re-expressing models from teams who aren't involved.
- The lingua franca framework itself (Cliff's paper).
- A standalone model description.
