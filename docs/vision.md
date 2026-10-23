# Decomposing disagreement between HIV models

*Vision for collaborators. The full introduction draft is in `narrative_draft.md`.*

**Target:** Nature Health. **Submission:** by 31 March 2027.

## Why

Calibrated HIV models agree closely on what is observed (population size, prevalence, numbers diagnosed and on ART). They diverge on the unobserved quantities that policy depends on. In the MIHPSA comparison, Malawi estimates of the share of 2024 transmissions from undiagnosed people ranged from 33% to 75% (Bansi-Matharu et al., 2025). A later analysis found that 35–64% of HIV deaths occurred among people on ART, depending on the model (Bansi-Matharu et al., 2026).

This is equifinality. Calibration targets constrain only a few combinations of inputs, so many parameter sets and structures fit the data equally well while implying different counterfactuals. The usual responses are:
- propagating structural uncertainty;
- testing whether it changes the decision;
- collecting data that target the disputed quantities.

All of these are valuable, but none of them explains the divergence. Isolating assumptions one at a time can (Hontelez et al., 2013), but it is costly today because each assumption is embedded in its own independently maintained codebase.

## What we propose

We want to make model differences **decomposable**, not just describable.

1. **Re-express** each model in a common modular framework (HIVsim on Starsim v4) as a set of interchangeable components. These cover demography, partnership formation and mixing, natural history and infectiousness, the testing and treatment cascade, interventions, and calibrated parameters.
2. **Substitute.** Start from model A and replace its components one at a time with model B's, recording each policy-relevant output after every swap.
3. **Verify at the endpoint.** Once every component has been swapped, the hybrid *is* model B and must reproduce B's original results. This tests the re-expression, and guarantees that the stepwise changes add up to the full gap.
4. **Report order-dependence.** Components interact, so a swap's contribution depends on when it happens. We report contributions across several orderings, and flag the components whose effect is order-sensitive. These mark where assumptions interact.
5. **Control noise.** Common random numbers keep the small differences between hybrids from being lost in stochastic noise.

## Recalibration

In principle every hybrid would be recalibrated, and what it takes to restore the fit would be informative in itself. If model A with one of B's components only fits when transmission probability shifts substantially, then the data constrain that component tightly. Full recalibration of every hybrid is not feasible, so we use three tiers:

1. **Uncalibrated path.** Components, including calibrated parameter sets, are swapped without refitting. The endpoint identity holds exactly.
2. **Compensated path.** At each step, a small parameter set common to all models is refitted to the same targets. The compensation needed is recorded as a measure of how strongly the data constrain each component.
3. **Full recalibration.** Discussed as the ideal; not attempted.

## Models and setting

| Model | Type | Transmission attribution |
|---|---|---|
| HIVsim | agent-based, structured sexual network | tracked source partner |
| EMOD-HIV | agent-based, partnership network | tracked source partner |
| Optima HIV | compartmental, mixing between population groups | inferred |

The setting is **Malawi**, where both EMOD and Optima took part in MIHPSA. HIVsim will be calibrated to the same data.

The three models give three substitution paths:
- **EMOD ↔ Optima** decomposes a published gap directly.
- **HIVsim ↔ EMOD** compares two agent-based network models.
- **HIVsim ↔ Optima** includes the change of modelling paradigm itself (network vs compartmental mixing). Starsim v4 can run a single model specification either way.

## Outputs

- Share of transmission from undiagnosed people, and from each other cascade stage.
- Share of HIV deaths among people on ART.
- HIV incidence.
- The ranking of at least one pair of interventions (for example, testing vs retention), to test whether the gaps matter for decisions.

## Planned results

1. **Verification.** HIVsim fits Malawi, and the re-expressions of EMOD and Optima reproduce their originals within pre-agreed tolerances.
2. **Decomposition.** For each path and output: each component's contribution across orderings, and which components interact.
3. **Compensation.** Which components the data constrain, and which they leave free.
4. **Decision relevance.** Whether intervention rankings change along any path.
5. **Cost.** The effort needed to re-express a model and run the decomposition, compared with building models stepwise.

## Principles

- Each original model remains the authoritative version, and a re-expression must reproduce it.
- The decomposition explains differences between models; it does not rank them.
- Models beyond these three are re-expressed only with their teams taking part.
- All code, re-expressions and outputs will be open.

## Questions for discussion

1. Which components, and at what granularity?
2. Which parameters form the common compensating set, so that they mean the same thing in all three models?
3. What verification tolerances should each output have?
4. Should AI agents assist the re-expressions, with the effort measured and reported?
