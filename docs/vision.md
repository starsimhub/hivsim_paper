# HIVsim paper: vision (v0.4)

*Builds on `narrative_draft.md`.*

**Target:** Nature Health (Article). Reach: Nature. Fallback: PNAS.
**Submit by:** 31 March 2027.
**Platform:** Starsim v4.

## Problem

Calibrated HIV models agree on what is observed and diverge on the unobserved quantities that policy depends on. In Zimbabwe they attributed 30–65% of transmission to undiagnosed people (Bansi-Matharu 2025); in another comparison, 35–64% of HIV deaths were among people on ART (Bansi-Matharu 2026). This is equifinality: calibration targets constrain only a few combinations of inputs, so many parameter sets and many structures fit the data equally well. The usual responses are to propagate structural uncertainty, test whether it changes the decision, collect data that targets the disputed quantity, or isolate assumptions one at a time. The last of these is the only one that explains a divergence, and today it is very costly because each assumption is embedded in its own codebase.

## Idea

**Make model differences decomposable, not just describable.**

- **Re-express models as components.** Each model is written in a common framework as interchangeable components: demography; network and partnership formation; natural history and infectiousness; the testing and treatment cascade; interventions; and calibrated parameters.
- **Decompose by substitution.** Start from model A and replace its components one at a time with model B's, recording each policy-relevant output after every swap.
- **The endpoint is a test.** When every component has been swapped, the hybrid *is* model B. It must reproduce B's original results, which verifies the re-expression. It also guarantees that the stepwise changes sum exactly to the total gap.
- **Handle order-dependence.** Components interact, so a swap's contribution depends on when it is made. With *k* components, running all 2^k hybrids gives an exact, order-free (Shapley) attribution plus the interaction terms; for *k* = 6 that is 64 configurations.
- **Use common random numbers** (native to Starsim) so the change from one swap is not swamped by simulation noise.

HIVsim on Starsim v4 provides what this needs: separable modules with shared interfaces, and components that can be swapped without rewriting the surrounding model.

## Demonstration (proposed; to settle at M1)

- **Models**
  - **A: HIVsim.** Agent-based, with a structured sexual network, partnership-level transmission and a tracked source partner.
  - **B: Optima HIV.** Compartmental, with mixing and inferred attribution; we co-authored it, so there is no sensitivity about using it. It is re-expressed in v4 and verified against the original Optima HIV in Zimbabwe (Optima took part in MIHPSA Zimbabwe). The existing v4 translation of Atomica's `hiv_dyn` is a demo framework, not the full Optima HIV, so it is only a starting point.
- **Setting:** Zimbabwe.
- **Outputs**
  - share of transmission from undiagnosed people;
  - share of HIV deaths among people on ART;
  - incidence;
  - one intervention ranking (e.g. testing vs retention), to show whether the gap matters for the decision.
- **The hard swap: partnership network vs compartmental mixing.** This swap is also a swap of modelling paradigm. v4 runs one spec as either an agent-based or a compartmental model, so paradigm becomes a component of its own (cite Cliff's lingua franca paper).
- **The path to more models (roadmap only).** Further models, e.g. "PopART-IBM with EMOD's network", are added only with each owning team taking part (see `collaboration.md`).

## Results

- **R1. Both models verified.**
  - HIVsim reproduces Zimbabwe.
  - Optima in v4 reproduces the original Optima HIV within pre-agreed tolerances.
- **R2. Decomposition of the HIVsim–Optima gap**, for each output, into per-component contributions and interactions.
- **R3. Decision relevance:** does the intervention ranking change along the substitution path?
- **R4. Cost.** The effort to re-express a model and run the decomposition, against the stepwise approach (Hontelez 2013), with the AI harness's role measured (see open questions).

## Claims and non-claims

| We claim | We do not claim |
|---|---|
| Model differences can be decomposed exactly into component contributions, with the endpoint as a verification test | That a common framework makes models equivalent or interchangeable without verification |
| Re-expressing a model is verifiable, and was verified for Optima | That we can re-express any model; nor that we did so for others without their teams |
| For one pair of models in Zimbabwe, we quantify what drives the gap in policy-relevant outputs | That the result generalises to every model pair |
| HIVsim on v4 is built for this | That this is a model-description paper |

## Open questions

1. **Should hybrids be recalibrated?** Without recalibration (parameters treated as one component, swapped last), the decomposition is exact but the intermediate hybrids don't fit the data. With recalibration after each swap, every hybrid is plausible, but exact additivity and the endpoint identity are lost. Options are to report both, or to make "calibrated parameters" the final component.
2. **What is the AI harness's role?** Your draft doesn't mention AI. Options: (a) agent-assisted re-expression of a model from its code and docs, verified Paper2Agent-style, which directly addresses the "very costly" point; (b) the harness runs the decomposition and writes it up; (c) leave AI out of this paper. My recommendation is (a), as the measured method behind R4.
3. **Which outputs and which components?** The component list sets *k*, and with it the number of hybrids.
4. **Is a second pair feasible by March?** For example HIVsim vs an EMOD-like configuration, with Daniel and Anna involved.

## Out of scope

- A multi-model plugin.
- Re-expressing any model without its team.
- The lingua franca framework itself (Cliff's paper).
- A standalone model description.
