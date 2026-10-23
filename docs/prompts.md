# Prompts

Two parts:

1. **Plan:** the prompts we expect to run, in order, each with its inputs, outputs, acceptance check and human checkpoint. Drafts, refined before running.
2. **Record:** prompts as actually run, copied exactly as typed, each with a short summary of the response and the commit. Follows `starsim/v4_design/admin/prompts.md`.

## Part 1: Plan (draft)

The order of these prompts is still open; see the dependency question in the grilling notes.

| # | Prompt (short) | Inputs | Output | Acceptance | Human checkpoint |
|---|---|---|---|---|---|
| P1 | Re-express EMOD-HIV (Malawi) in Starsim v4 | EMOD source, Malawi config, Starsim v4, stisim (example) | `models/emod/` | reproduces EMOD Malawi reference outputs | TBD |
| P2 | Re-express Optima HIV (Malawi) in Starsim v4 | Optima source, Malawi project, Starsim v4, stisim | `models/optima/` | reproduces Optima Malawi reference outputs | TBD |
| P3 | Extract calibration targets and adjustable parameters; calibrate HIVsim Malawi | Bansi-Matharu 2025 + supplement, calib plugin | targets file, parameter priors, fitted HIVsim | fit to targets | TBD |
| P4 | List the atomic components of each model; design the sequential swaps | P1–P3 outputs | component map, swap plan | TBD | TBD |

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

## Part 2: Record

*None yet.*
