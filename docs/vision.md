# HIVsim: vision (v0.2)

*2026-10-22. v0.1 is in git history (a18884a).*

**Target:** Nature Health, Article; presubmission enquiry in January. Reach: Nature. Fallback: PNAS.
**Deadline:** submitted by 31 March 2027.

## Thesis

HIV models disagree largely because they make different structural choices: how partnerships form, how risk varies, how people get tested, how they leave and return to care, and how infectious they are on treatment. In most models those choices are fixed in the code. HIVsim makes them **selectable**. It is one calibrated, open-source model in which the structural assumptions that distinguish HIV models can each be switched among the representations used across the field. It is operated through an **AI harness** that, for a given question, identifies which structural choices bear on the answer, runs and recalibrates the alternatives, and reports what the answer depends on.

One sentence: *HIVsim is an AI-operable HIV model in which the structural assumptions that separate HIV models are user choices, so that the dependence of policy-relevant answers on those assumptions becomes explicit, quantified and routine.*

## Contributions

1. **Structural choice as a model feature.** A menu of alternative representations for each key structural dimension (below), each implemented, tested and recalibratable. These are not reconstructions of other groups' models; they are representations of the *choices* that distinguish them, described by mechanism.
2. **An AI harness that operates the model.** It turns a question into a structured analysis, lays out the structural options relevant to it, calibrates and runs each configuration, and writes a report stating what the answer depends on. It builds on the existing stisim plugin (15 skills) and adds validated MCP tools, since Paper2Agent's ablation found tools far more reliable than skill files alone (99% vs 73%).
3. **Safeguards enforced in code:** provenance, parameter and unit checks, mandatory recalibration after a structural change, a decision log, and explicit "outside what I can answer" escalation.
4. **HIVsim itself,** interleaved: core natural history, networks, interventions, validation in Zimbabwe, and composability with other STIs (applied, citing Cliff's lingua franca paper for the framework). The existing references are the vddx_zim paper supplement (Sex Transm Infect) and the docs; there will be no standalone model-description paper.

## Out of scope

- The HIVMC multi-model plugin (possible separate project).
- Rebuilding or verifying other groups' models.
- The lingua franca and multi-disease framework (Cliff's Nature Computational Science paper).
- Claims of autonomy: the harness assists, and modellers decide.

## Structural menu (candidate)

Status levels: V = implemented and validated; I = implemented, not validated; F = feasible, still to build.

| Dimension | HIVsim default | Alternatives | Status |
|---|---|---|---|
| Partnership formation | StructuredSexual (risk groups × partnership types, sex work) | risk-group mixing without persistent partnerships (compartmental-style); higher-concurrency variants | default V; alternatives F |
| Risk heterogeneity | 3 risk groups | none / 2 groups / continuous propensity | I (parameters exist) |
| Testing | rate-based uptake | risk-targeted; fixed test volume; symptom- and ANC-driven only | partly I |
| ART interruption | duration-based | age-dependent adherence | I / F |
| ART re-engagement | via coverage correction only | explicit re-engagement rate | F |
| Infectiousness on ART | suppressive vs non-suppressive | VL thresholds (<200 / <400 / <1000); continuous VL | I / F |
| Acute-phase infectiousness | ×5.3, 1.7 months | literature range | V (parameters) |
| Transmission attribution | tracked source partner | cascade-weighted; counterfactual zeroing | F (analyzer port) |
| Solver | ABM | compartmental, via v4, where supported | depends on v4 |

## Results (planned)

- **R1. HIVsim reproduces Zimbabwe:** HIV, jointly calibrated with STIs, plus a hold-out validation (e.g. ZIMPHIA 2020).
- **R2. Structural sensitivity.** For 2–3 policy-relevant quantities, each configuration is recalibrated to the same targets:
  - share of transmission from undiagnosed people;
  - share of transmission from sex work (tPAF);
  - ranking of testing vs retention interventions.

  The spread is decomposed by dimension and compared against published ranges between models (MIHPSA Zimbabwe 29.8–64.6%; Silhol et al. 2026 for sex work).
- **R3. Harness evaluation.**
  - A predefined set of 20–30 questions.
  - Harness answers vs a Claude-with-repo baseline.
  - Graded blind by HIV modellers from several groups for correctness and for whether the relevant structural dependencies were identified.
  - Safeguard triggers, failures, time and cost reported.
- **R4 (optional). Worked case:** cost-effectiveness under funding shocks (Eswatini, from Daniel's paper).

## Figures (draft)

1. The structural choices that distinguish HIV models, as switches in one model, operated by the harness.
2. HIVsim core and validation.
3. Structural sensitivity: answers across configurations against published inter-model ranges, with the decomposition.
4. The harness end to end: question → structural options → runs → a "depends on" answer.
5. Evaluation and safeguards.

## Open questions

- Should the paper run on v3 or v4? If v4 is released by January, use v4.
- Naming: describe switches by mechanism only. Mapping them to named models belongs in a table that the relevant groups review.
- How external modellers take part: as graders, as reviewers of switch descriptions, or as co-authors (see `collaboration.md`).
