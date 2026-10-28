# Spike: a declared cascade on a coded natural history

*28 Oct 2026. Starsim `v4` (1ce69a13 + PR #1492, which adds `ss.move()` along a transition), stisim `origin/v4` (4aeacec).*

**Question:** can a declared component and a coded one sit behind a shared interface in one agent sim, and where is the friction?

**Setup (`seam.py`):**
- HIVsim's coded HIV (`sti.HIV`), unchanged, except for a 200-year `dur_on_art`.
- A declared Optima-style cascade (`undx → dx → care → svl/usvl`, `lost` and return, failure), whose rates read HIV's CD4 count (faster testing below CD4 200).
- A coded connector (`Seam`) for what has to be code: Optima's number-on-ART target, lowest CD4 first; and keeping HIV's ART status in line with the cascade's.

**Interface used:**
- Natural history → cascade: `hiv.infected`, `hiv.cd4`.
- Cascade → natural history: `hiv.start_art(uids, p_effective_art)`, `hiv.stop_art(uids)`, `hiv.set_suppression(uids, bool)`.

## Result

**It works.** At the end of a 1990–2030 run (5,000 agents), everyone infected is in the cascade, and HIV's on-ART and suppressed sets match the cascade's, except for the few the cascade moved in the last step (2 here), which HIV hears of at the next step (item 3). The declared cascade enters people on HIV's infections (`where=hiv.infected`), and its rates read the coded CD4 (`hivtest + (aidstest - hivtest)*(hiv.cd4 < 200)`). The parameters are made up, so the numbers mean nothing.

## Friction

1. ~~**A split can't be moved by a target.**~~ *Resolved.* A split with no rate raises, deliberately (a forgotten `dur=0` would otherwise move nobody), but `rate=0` says it outright: `ss.Transition(care, [svl, usvl], p=[0.9, None], rate=0)` is moved only by code, and `cas.move(uids, cas.initiate)` splits people in its shares.
2. **The target and its priority are code.** Optima's `numtx`, lowest CD4 first, is about 10 lines in the connector. Stock targets and priority were removed from Starsim on 20 Oct, so this is as intended. It belongs in the shared cascade component, not in Starsim.
3. **A one-step lag from cascade to natural history.** The cascade's own moves (loss, failure) happen in its `step()`, after the connectors, so HIV hears of them at the next step (a month in STIsim). The target's moves are passed on at once. *Options:* run the sync after the cascade (a module after the diseases, via `sim.loop.insert()`), or have the natural history read the cascade's states directly instead of keeping its own copy.
4. **The natural history owns treatment interruption.** HIVsim's `start_art()` draws each person's own time to stop (`dur_on_art`, `ti_stop_art`), so the cascade's loss to follow-up competes with the natural history's own stopping. The spike turns it off with a 200-year `dur_on_art`. *For P4:* in HIVsim, interruption and re-engagement must move out of `sti.HIV` into the cascade component, which the treatment-interruption scenario needs anyway.
5. ~~**Moves by code aren't counted as flows.**~~ *Resolved in Starsim PR #1492:* `ss.move()` (and `disease.move()`) now takes a transition, `cas.move(uids, cas.initiate)`, moving people from its sources along it: counted in its flow and recorded as its event, under every solver (`p=` or `n=` under a compartmental one).
6. **Two copies of ART status.** The cascade's `usvl`/`svl` and HIV's `on_effective_art`/`on_nonsuppressive_art` are kept in line by code. It works, but it's the seam most likely to drift.

## For the paper

- The interface works in agent terms, and declared and coded components can share a sim. Nothing here argues for declaring HIVsim's natural history.
- Items 1 and 5 are resolved (5 by a Starsim change); item 3 has a workaround.
- Item 4 is a HIVsim refactor that P4 has to plan for.
