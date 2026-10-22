# HIVsim paper: vision (v0.3)

**Target:** Nature Health (Article). Reach: Nature. Fallback: PNAS.
**Submit by:** 31 March 2027. **Platform:** Starsim v4.

## The problem

Validated HIV models, calibrated to the same data, agree on what is observed (prevalence, diagnosis, ART coverage) and disagree on the unobserved quantities that drive policy. In MIHPSA, the share of transmission from undiagnosed people ranged from 30% to 65% in Zimbabwe. Calibration constrains the observables; it does not necessarily constrain the answer.

## The idea

HIVsim, operated through an AI harness, answers a policy question and reports **whether the data actually pin that answer down**.

- **The default model is the modellers' best judgement.** HIVsim comes with its own validated structure and parameters.
- **Structural alternatives are used only to test whether an answer is robust;** they are not a menu of choices for the user. Each alternative represents a choice that distinguishes credible HIV models, and is described by mechanism, not by the name of any other model.
- **A structure only counts if it still fits.** Each alternative is recalibrated to the same targets and must pass the same validation. Structures that can't are ruled out.
- **Every answer comes back sorted.** It is either *robust* (it holds across all structures that still fit) or *dependent on X* (it varies with an assumption current data don't constrain). In the second case the report says what evidence would resolve it.
- **The harness enforces this workflow.** It uses validated tools, checks that alternatives still fit, logs provenance, and escalates questions outside its scope.

## Claims

| We claim | We do not claim |
|---|---|
| Validation constrains structure, but not every policy-relevant quantity | That any structure is valid |
| For specific questions in Zimbabwe, we can quantify which answers are robust and which aren't | That we reproduce or replace other groups' models |
| An AI harness can run this workflow reliably, with safeguards, as shown by a blinded benchmark | That the harness is autonomous, or that it gives policy advice |
| HIVsim (described in the paper) is a validated, open model for this | That this is a model-description paper |

## Results (to be finalised in Sprint 1)

- **R1.** HIVsim on v4 reproduces Zimbabwe, including a hold-out validation.
- **R2.** For 2–3 policy-relevant quantities, the range of answers across structures that still fit, sorted into robust vs dependent on X, compared against published ranges between models.
- **R3.** Blinded benchmark of the harness on a fixed question set.
- **R4 (optional).** A worked cost-effectiveness case, from Daniel's Eswatini paper.

## Out of scope

- A multi-model plugin.
- Rebuilding other groups' models.
- The lingua franca and multi-disease framework (Cliff's paper; we cite it).
- A standalone model description.
