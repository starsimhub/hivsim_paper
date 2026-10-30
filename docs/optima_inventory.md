# Optima HIV Malawi: component inventory

Source: `files/Malawi_20220912.prj`, run on Optima HIV 2.12.2 (`~/src/optima`, conda env `optima`). The project was saved by Optima 2.11.4 on 12 Sep 2022 (branch `updates-june-2022`). Reference run and outputs: `optima_ref/run_optima.py`.

## Project contents

- **One parameter set** (`20220912`). This is the calibrated model, and the only thing that is run.
- **The program set is empty.** No cost or coverage curves, so nothing is driven by budgets. Coverage comes straight from the databook.
- **One scenario** (`default`), a parameter scenario with no overrides, so it is the same as the baseline.
- **One optimisation** (outcomes, 2020–2030, weights: incidence 1, deaths 5). It can't run usefully without programs.

The thing to rebuild is therefore the epidemic model plus its databook inputs. There is no programs layer.

## Structure

- Deterministic compartmental model, 1990–2030, dt = 0.2 years. Run time 0.5 s.
- **39 populations**: FSW, Clients and MSM (all aged 15–49), plus 36 general populations (F/M by 5-year age band from 0–4 to 85+).
  - Ageing moves people between bands (`agerate`, `agetransit`).
  - There are risk transitions between populations (`risktransit`, 14 nonzero entries).
  - Births go into the 0–4 bands (`birthtransit`).
  - Population sizes are forced to follow the input (`forcepopsize = 1`).
- **Infection stages (6)**: acute, CD4 >500, >350, >200, >50, <50.
- **Care states (8)**: susceptible, circumcised susceptible, undiagnosed, diagnosed, in care, lost to follow-up, on ART unsuppressed, on ART suppressed.
- **No migration**: emigration and immigration are zero.

## Components and their inputs

| Component | Optima parameters | Notes |
|---|---|---|
| Demography | `popsize`, `birth`, `death`, `agerate`, `forcepopsize` | Population size is forced to follow the input |
| Sexual mixing | `actsreg` (147 pairs), `actscas` (133), `actscom` (FSW↔Clients), `condreg/cas/com` | Regular, casual and commercial acts per year between pairs of populations |
| Transmission | `transmfi/mfr/mmi/mmr`, `transnorm` 0.43, `cd4trans*` (acute 5.6, CD4<50 7.17), `effsti` 2.65 with `stiprev`, `effcondom`, `effcirc`, `effprep`/`prep`, `effpep`/`pep` | `force` (0.01–10 by population) and `inhomo` scale the force of infection. These are the main calibration knobs |
| Mother-to-child transmission | `mtctbreast`, `mtctnobreast`, `breast`, `numpmtct`, `effpmtct` | |
| Disease progression | `prog*` (acute 0.24 y, then 0.95, 3.0, 3.74, 1.5 y) | Linear chain through the CD4 bands |
| HIV death | `death*` by CD4 band, `hivdeath` (all 1), `deathtb` with `tbprev`, `deathsvl/usvl` | |
| Testing | `hivtest` (rate by population and year), `aidstest` | |
| Linkage and retention | `linktocare`, `aidslinktocare`, `leavecare`, `aidsleavecare`, `returntocare` | **HIVsim has no equivalent** (no in-care or lost-to-follow-up states) |
| ART initiation | `numtx` (total number on ART, data to 2020), `allcd4eligibletx` (no CD4 rule from 2018), `fixproptx` 2020 | Hits the number-on-ART target. After 2020 the proportion of people in care who are on ART is held fixed |
| Viral suppression and failure | `treatvs` 0.2 y, `treatfail` 0.02/y, `numvlmon` (0 throughout), `regainvs`, `fixpropsupp` 2020 | |
| CD4 on ART | `svlrecov*`, `usvlprog*`, `usvlrecov*` | Recovery while suppressed, movement up and down while unsuppressed |
| Circumcision | `propcirc`, `numcirc` (0) | Traditional circumcision only |
| Initialisation | `initprev` by population, `initcd4weight` 0.7 | |
| Not used | injecting (`actsinj`, `sharing`, `numost`), migration | Out of scope for Malawi |
| Outputs only | `disutil*` | Only needed for DALYs |

## Fit to data (reference run)

- Population size and number on ART match the data almost exactly. The ART match is by construction.
- PLHIV fits well (1.13M in 2020).
- HIV deaths have the right shape, but the peak is too low (about 57k modelled against 71k).
- New infections are too low before 2000 (about 85k against 110k at the peak) and slightly too high from 2012 to 2018.
- Prevalence: the data series is adult prevalence. The model's 15–49 prevalence is 11.6% in 1999 against 15.2% in the data, and 8.8% in 2020 against 8.1%. So the model's early peak is too low, which is consistent with its low early incidence.

## Implications for Optima′

- With no programs layer, the rebuild only covers the epidemic model plus the databook time series.
- Several parameters are calibration scale factors, not biology: `force`, `inhomo`, `transnorm`, `initprev`. They have to carry over exactly as values, not be recalibrated.
- From 2020, projections hold the cascade proportions fixed (`fixproptx`, `fixpropsupp`). The treatment-interruption scenario has to change these rules, so they are part of the scenario interface.
- The cascade (linkage, loss to follow-up, return to care) is the main structural gap with HIVsim. See the seam spike notes.

## Time-step dependence (30 Oct)

The calibrated Optima Malawi model is a discrete-time model at dt = 0.2, and its results are not converged in dt (`optima_ref/dt_study.py`). Maximum relative difference from dt = 0.2, 2000–2030:

| dt | PLHIV | New infections | HIV deaths | Diagnosed | On ART |
|---|---|---|---|---|---|
| 0.1 | 3.6% | 15.1% | 23.4% | 3.1% | 4.1% |
| 0.05 | 7.4% | 31.0% | 43.9% | 6.2% | 5.6% |
| 0.02 | 10.6% | 46.0% | 64.8% | 8.8% | 7.6% |

Before ART scale-up (to 2005) the differences are at most 7%. Most of the rest is one mechanism:

- **Viral suppression on ART is a step-size artefact.** People starting ART go straight to suppressed with probability `1 - exp(-dt/treatvs)` (`model.py:1057`). With `treatvs` = 0.2 y that is 63% at dt = 0.2. The only other route from unsuppressed to suppressed is viral load monitoring, and `numvlmon` is 0 throughout. So the share of people on ART who are suppressed in 2006–2010 is 0.65 at dt = 0.2, 0.42 at dt = 0.1 and 0.11 at dt = 0.02.
- Holding that share at 63% (`treatvs = dt`) cuts the gap at dt = 0.02 to 16% for new infections and 12% for deaths after 2005, and 3–8% before. Other step-dependent pieces remain, not yet identified. Candidates: rates used directly as probabilities (`hivtest*dt`, `leavecare*dt`, `treatfail*dt`, death rates), the cascade-proportion rules, and the old ageing code (project version 2.11.4 < 2.12.0, `model.py:891`).

Consequence for P2: a continuous-time ODE re-expression cannot be within 2% of Optima at dt = 0.2 unless these discrete-step behaviours are reproduced or made explicit.

### Making the step explicit (option 1, 30 Oct)

`optima_ref/model_dt.py` is a copy of Optima's `model.py` (2.12.2) with switches (`FIX`) that convert each group of step-dependent rules to a step-independent form that reproduces the calibrated step (`REF_DT = 0.2`). With every switch on, it equals the original at dt = 0.2 (to 3e-8 people). `optima_ref/dt_fix.py` runs the ablations.

| Group | Rule in Optima | Conversion that reproduces dt = 0.2 |
|---|---|---|
| supp | Suppressed at ART start with probability `1-exp(-dt/treatvs)` | Fixed share, `1-exp(-0.2/treatvs)` = 63% |
| acute, dwell | Exponential stays, `1-exp(-dt/tau)` (CD4 progression, ART recovery, linkage, risk transitions) | Keep the time spent at the calibrated step: rate `(1-exp(-0.2/tau))/0.2`, i.e. a stay of about `tau + 0.1` (acute: 0.35 y, not 0.24) |
| cascade, death, usvl, age | Rates used as probabilities, `r*dt` (testing, loss and return to care, treatment failure, deaths, CD4 change on unsuppressed ART, ageing) | Keep the survival over the calibrated step: rate `-ln(1-0.2r)/0.2` |

With all groups on, results converge (dt = 0.02 and 0.01 differ by under 0.2 points). Max difference from the calibrated run in yearly outputs, 2000–2030: PLHIV 1.1%, diagnosed 1.9%, on ART 1.4%, suppressed 1.4%, new infections 3.5% (2018), HIV deaths 3.3% (2030).

Open: the two conversion rules differ (time in state vs survival), with no reason yet why they should. That may mean they are compensating for something else. One candidate already found: switching the project to Optima's newer ageing code (≥ 2.12.0) changes results by 2–7% before 2019 at dt = 0.2.

### Projections are ill-conditioned (30 Oct)

After 2019, new infections and deaths amplify small differences. In the original model, raising `force` by 0.5% changes new infections by +1.8% in 2015 and +12% in 2030, and deaths by +1.3% and +15%. PLHIV changes by only 0.9% and 2.1%. The likely reason: the number on ART does not respond (+0.3%), so the extra people with HIV stay untreated. By 2030 about 0.15M of 1.22M PLHIV are untreated, and they produce most of the new infections and deaths.

Consequence for P2: "within 2% for every output, 2000–2040" can't be met for new infections and deaths in projection years by any re-expression. A difference of 0.1% in PLHIV becomes about 1.5% in 2030 incidence.
