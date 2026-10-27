# hivsim_paper

This repository holds the work for decomposing disagreement between HIV models. HIVsim, EMOD-HIV and Optima HIV, each fitted to Malawi, are re-expressed as interchangeable components in Starsim v4. Swapping those components one at a time traces how much of the difference in policy-relevant outputs each modelling choice accounts for.

## Docs

| File | What it is |
|---|---|
| [docs/vision.md](docs/vision.md) | The proposal: motivation, goals and methods |
| [docs/narrative_draft.md](docs/narrative_draft.md) | Draft introduction, with references |
| [docs/plan.md](docs/plan.md) | Weekly sprint plan to 15 Dec 2026 |
| [docs/prompts.md](docs/prompts.md) | Agent prompt plan (P0–P5), human checkpoints, decisions, notes on Starsim v4, and a record of prompts run |

## Conventions

- `raw_results/`: large outputs, including runs of the original models. Not committed (gitignored).
- `results/`: committed. Holds everything the plotting scripts need.
