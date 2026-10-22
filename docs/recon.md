# Recon: current state, literature, journals

*2026-10-21. Compiled from code audits of stisim, the hivsim_* repos and starsim v4, plus a literature and journal search. Items marked [unverified] are not yet confirmed.*

## 1. Capability inventory

Four levels: **V** = implemented and validated; **I** = implemented, not validated; **F** = feasible with engineering; **A** = aspirational within 7 weeks.

| Capability | Level | Where / notes |
|---|---|---|
| HIVsim natural history (CD4 stages, acute ×5.3, suppressive vs non-suppressive ART, MTCT, CD4 mortality) | V | `stisim/diseases/hiv.py`, 26 tests; calibrated in Zim, Zambia, Eswatini, Kenya |
| Testing, ART, VMMC, PrEP, PN | V | `stisim/interventions/hiv_interventions.py` |
| ART interruption (duration-based) | I | `dur_on_art` |
| ART re-engagement (explicit rate) | F | missing: re-entry happens only through coverage correction |
| StructuredSexual, sex work and MSM networks | V | `stisim/networks/` |
| HIV + syphilis, jointly calibrated | V | `sti_notification` (6 STIs, Zimbabwe, 500-draw LHS) |
| Other HIV–STI connectors (tv, ng, ct, bv) | I | untested |
| HIV + TB | F/A | no TB model or connector in the local ecosystem; check `starsimhub/tbsim` |
| Transmission by the source's cascade state | I (stale) | `hivsim_zim/analyzers.py::HIVCascadeAnalyzer`; reads the removed `hiv.post_art`, so it breaks on stisim 1.7.1 |
| Benchmark against MIHPSA (Zimbabwe) | I (stale) | `hivsim_zim` preprint: undiagnosed 12.0% vs 29.8–64.6% published; driven by 99% diagnosed |
| Malawi HIVsim | F | none exists |
| stisim AI plugin (15 skills) and starsim_ai skills | I | no evaluation |
| MCP server that runs sims | F | only documentation-lookup MCPs exist |
| Programmatic safeguards (units, ranges, provenance, decision log) | F | guidance only |
| AI vs conventional benchmark | F | none |
| v4 one spec → ABM or ODE (`solver=`) | I | ABM/ODE agreement tests on v4-rs |
| v4 engine primitives HIV needs (CD4 `ss.attr`, ART `target=`/`priority=`, events) | I | v4-rs acceptance tests, incl. an HIV CD4 ABM-vs-ODE test |
| Optima/Atomica `hiv_dyn` in v4 | I | matches to rounding; 217 → 67 lines; slower (5.4 → 180 ms) |
| EpiModel `hiv` in v4 | I | agrees within noise; 405 → 62 lines; 54 s → 2.5 s |
| HIVsim ported to v4 | F (high risk) | not started; blocked by the untested stisim-v4 WIP, the events merge (red) and the directional-beta bug |
| `ss.diff` structural diff | F | designed in `design/16-interop.md`; about 1–2 weeks to build on `to_spec()` |
| `to_spec()` / `from_spec()` round trip | I (partial) | networks, interventions and functions not yet supported |
| Importers for other frameworks | A | not started |
| Rebuilding EMOD, PopART-IBM or Synthesis in full | A | each is very large |
| Rebuilding Goals or Thembisa in v4 | F | stratified compartmental; the bottleneck is reference outputs, not the engine |

## 2. The target result: Bansi-Matharu et al. 2025 (Lancet GH)

- Malawi, Zimbabwe and South Africa (MIHPSA, funded through the HIV Modelling Consortium). Six models, though not every model ran every country:
  - **Malawi:** EMOD, Goals, Optima, Synthesis.
  - **Zimbabwe:** Goals, Optima, Synthesis, PopART-IBM.
  - **South Africa:** Goals, Optima, Synthesis, Thembisa.
- Share of 2024 transmission from undiagnosed people: Malawi 33.3% (EMOD) to 75.3% (Goals); Zimbabwe 29.8–64.6%.
- **How transmission is attributed differs by model.** EMOD and PopART-IBM track who actually infected whom; the other four infer it from the cascade distribution or by counterfactual zeroing. The denominator (new infections) differs more than 3-fold.
- Explanations were qualitative only:
  - U=U thresholds (Optima <400 copies/mL, Goals <1000, Synthesis <200; EMOD and PopART-IBM have no threshold);
  - how viral suppression is generated;
  - age-specific adherence;
  - interruption rates;
  - fixed numbers of tests as the population grows;
  - calibration choices.
- No harmonization, and no public archive of the outputs.
- Internal inconsistencies: EMOD's Malawi on-ART share (46.1%) lies outside the stated range; "diagnosed-not-on-ART <5%" contradicts South Africa's 5.6–15.5%.
- **Daniel Citron is an EMOD author on this paper**, with Anna Bershteyn as co-senior.

### The six models

Ease is rated 1–5, higher = easier.

| Model | Type | Code | Rebuild / run original |
|---|---|---|---|
| Optima HIV | compartmental, Python | LGPL (Atomica: MIT) | 4 / 5 |
| EMOD-HIV | network IBM, C++ | MIT; IDM-native | 4 / 4 |
| Goals (GoalsARM) | compartmental, C++ + Python client | MIT [unverified that it is the version used in the paper] | 4 / 3 |
| Thembisa | compartmental, C++ | GitHub, no license; South Africa only | 3 / 3 |
| PopART-IBM | network IBM, C | GPL-3 | 3 / 4 |
| HIV Synthesis | IBM, SAS | unclear license, thin docs | 2 / 1 |

### Precedents

- **CISNET "model experiments"** are the methodological template: stylized scenarios that expose unobserved deep parameters, e.g. breast-cancer tumour-inception timing explained 19–71% of the spread.
- **Hontelez 2013** (PLoS Med) used nested HIV models of increasing complexity.
- **Eaton 2012** admitted that structure "explained only a modest amount" of the differences between models. That unsolved problem is our hook.
- **Paper2Agent** succeeded through scale, measured fidelity to the original papers, and honest failure rates (26% of repos couldn't be converted). No high-tier paper has agents rebuilding or reconciling disease models, so this is open ground.

## 3. Journals

- **Nat Med**
  - Article: 4,000 words, 6 display items, ~60 refs.
  - **No presubmission enquiries.**
  - Code is peer reviewed; LLM use must be disclosed in Methods.
  - Publishes decision-anchored modelling (e.g. Ponce 2025 on Malawi HIV treatment deserts; Zupko 2023) and AI agents with external validation (SPARK, HemaGuide). It has published no platform or infrastructure paper, so a platform-led framing will likely be desk-rejected.
- **Nature Health** (new, 2026): same limits as Nat Med; its scope includes modelling, AI and LMIC; **accepts presubmission enquiries**.
- **Nature Computational Science:** 3,500 words; its Analysis type ("comparative analysis that leads to novel and arresting conclusions") fits; publishes agent papers. Natural home for the platform and AI benchmark.
- **Nature:** long shot unless the AI claim generalises beyond HIV (bar set by Paper2Agent and Virtual Lab).
- **Lancet GH / Lancet HIV:** natural home for the comparison result alone; would give little weight to the platform and AI claims.
- **Recommendation:** split into two papers.
  - **Paper A** (Nat Med or Nature Health): the result, i.e. why the models disagree and what that means for Malawi's decisions.
  - **Paper B** (Nat Comput Sci): the platform, the composability demo and the AI benchmark.
  - Preprint both and cross-cite.

## 4. Paper2Agent and comparators (added 2026-10-21)

Paper2Agent: arXiv 2509.06917; repo jmiao24/Paper2Agent (MIT), now shipped as a Claude Code skill (`paper2mcp`, `paper2skill`).

**Pipeline** (multi-agent, Claude Agent SDK), producing one MCP server per paper:
1. Clone the repo and build its environment.
2. Scan the tutorials, run them, and keep their outputs as ground truth.
3. Extract and parameterise functions as MCP tools.
4. Test-and-fix loop, up to 6 tries per function. A tool passes if numbers are within 3% and figures match by perceptual hash; tools that keep failing are dropped.

The resulting server has three parts: tools (validated functions), resources (paper, supplement, data) and prompts (workflow templates).

**Evaluation**

| Test | Result |
|---|---|
| AlphaGenome, tutorial-derived / novel queries | 98.7% / 100%, vs Claude+Repo 82.7% / 78.7% |
| AlphaGenome, open-ended queries | 82.7% |
| 100 unfiltered papers | 74 agentified, ~$15 per paper; 91.2% on 300 questions |
| Out-of-scope questions | 100% refused |
| Ablation: Markdown skills instead of MCP tools | **73% vs 99%** |
| Ablation: no verifier | 69% |

**Stated open problem:** "evaluating the range of defensible answers". Their benchmarks grade faithful execution against one reference answer, not analytical validity.

**What HIVMC adds beyond Paper2Agent:**
- a multi-model structural registry;
- model selection for a given question;
- divergence explained by structural assumptions ("it depends on X, Y, Z");
- emulators;
- uncertainty;
- escalation to the group that owns a model;
- tests on output distributions for stochastic ABMs (a single 3% match doesn't fit them).

**Comparators**
- **Silhol et al. Lancet HIV 2026;13:e30** (9 models, 15 settings, sex-work tPAF; PMID 41275868). A natural human-generated benchmark for the sex-work question.
- **"Many AI analysts, one dataset"** (PNAS 2026;123(29):e2606495123). LLM analysts reproduce the spread between human analysts and trace it to analytic choices; the closest framing.
- **EPIAGENT** (arXiv 2602.00299). Builds new compartmental simulators; HIVMC instead queries existing, validated models.
- **EpidemIQs** (arXiv 2510.00024).
- **CISNET model profiles.** Precedent for the registry.
- **Safeguards:** Tang et al. Nat Commun 2025 (10.1038/s41467-025-63913-1); SafeScientist; SciGuard.
- No prior LLM + HIV-model work found [needs a final check].

**Venues** (Nature Computational Science excluded):
- **Primary:** Nature Health. Its scope covers modelling, AI and low- and middle-income settings, and it accepts presubmission enquiries.
- **Reach:** Nature, if the benchmark is strong and scales beyond one model.
- **Fallback:** PNAS, framed as the science of model disagreement.
- **Possible:** Science (Biomni precedent); Nature Medicine (its agent papers are all clinical).

## 5. Sources

Full agent reports with URLs are in the session transcript (2026-10-21). Key DOIs:
- Bansi-Matharu 2025: 10.1016/S2214-109X(25)00121-4
- Bansi-Matharu PLoS Med 2026 (deaths by cascade stage, 7 models): 10.1371/journal.pmed.1004864
- Eaton 2012: 10.1371/journal.pmed.1001245
- Hontelez 2013: 10.1371/journal.pmed.1001534
- van den Broek 2018 (CISNET MCLIR): 10.1177/0272989X17743244
- Kuntz 2011: 10.1177/0272989X11408730
- Paper2Agent: arXiv 2509.06917
