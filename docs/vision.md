# Proposal: decomposing disagreement between HIV models

## Motivation

Calibrated HIV models generally agree closely on what is observed (population size, prevalence, numbers diagnosed and on ART), but often diverge on the unobserved quantities that policy depends on. In a recent comparison conducted through the Modelling to Inform HIV Programmes in Sub-Saharan Africa (MIHPSA) Collaboration, six established models were well aligned on population and prevalence, but estimates of the share of 2024 transmissions from undiagnosed people in Malawi ranged from 33% to 75% (Bansi-Matharu et al., 2025). A later analysis found that 35–64% of HIV deaths occurred among people on ART, depending on the model (Bansi-Matharu et al., 2026).

The general problem is that many parameter sets and structures fit the observed data equally well while implying different latent epidemiological states. This is sometimes taken as a motivating call to collect more data that can help elucidate the true epidemiology, and other times taken as a type of structural uncertainty. Both of these can be valuable, but neither of them explains the divergence. Isolating assumptions one at a time can (Hontelez et al., 2013), but it is costly today because each assumption is embedded in its own independently maintained codebase.

## Goals

Make model differences decomposable, not just describable. "Diff away the diffs"!

## Methods

Start with three models (HIVsim, EMOD and Optima HIV), fitted to Malawi. EMOD and Optima HIV were already fitted to Malawi, so we will need to calibrate HIVsim to the same targets.

- **Standardize core architecture.** Formulate each model within a shared modular structure (HIVsim built on Starsim v4) using interchangeable building blocks. These encompass population dynamics, relationship patterns and mixing, biological disease progression and infectiousness, diagnosis and treatment pathways, program interventions, and calibrated parameters.
- **Sequential swapping.** Take model A as a base and systematically substitute its individual modules with those from model B, recording key policy projections after every replacement.
- **Validation.** Following the complete exchange of all elements, the resulting composite system becomes model B and ought to mirror B's baseline outputs. This confirms model translation fidelity and ensures the incremental effects fully account for total variation.
- **Evaluate sequence effects.** Interdependent modules mean a given swap's influence varies according to its placement in the sequence. We detail these impacts across multiple replacement pathways, highlighting elements whose influence changes with sequence position to uncover structural dependencies.
- **Minimize stochastic variation.** Employing identical random number streams prevents minor variations between composite models from being obscured by random noise.

**Outputs:**
- share of transmission from undiagnosed people, and from each other cascade stage;
- share of HIV deaths among people on ART;
- HIV incidence;
- ranking of at least one pair of interventions (for example, testing vs retention), to test whether the gaps matter for decisions.

## Notes and questions

**Calibration.** In principle every hybrid would be recalibrated, and what it takes to restore the fit would be informative in itself. If model A with one of B's components only fits when transmission probability shifts substantially, then the data constrain that component tightly. Full recalibration of every hybrid is not feasible; three tiers are proposed:

1. **Uncalibrated pathway.** Substitute building blocks along with calibrated parameter values directly, without refitting. Under this approach, endpoint equivalence remains perfectly intact.
2. **Compensated pathway.** Re-estimate a limited subset of shared parameters against identical targets following each swap. The magnitude of parameter adjustment required quantifies how tightly empirical data constrain each structural element.
3. **Full recalibration.** Gold standard, but probably not possible.
