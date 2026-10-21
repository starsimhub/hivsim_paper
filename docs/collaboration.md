# Involving other HIV modellers (draft v0.1)

## The concern to design against

Two things are new here: a Gates Foundation group (IDM) and AI agents rebuilding other teams' models. Read together, they can sound like "the funder is replacing your models with bots", and most of these groups are Gates-funded through the HIV Modelling Consortium. That power asymmetry is real and should be said out loud, not managed around.

## Framing

- **The goal is the one this community has had since Eaton 2012:** explaining *why* models disagree. The original teams know their models best, so the work can't be done credibly without them.
- **Rebuilds are scaffolding for experiments, not replacements.** The paper says explicitly that each original model remains the authoritative version.
- **Model diversity is the asset.** The result is a map of which assumptions matter and which data would resolve them; it is not a ranking of the models.
- **AI makes the tedious parts cheap** (translation, bookkeeping, reruns). The scientific judgement stays with the modellers, and the paper reports every human correction.

## Principles

1. **No rebuild without consent.** Each team chooses whether to take part before we publish anything about their model. Code can be open-source and still not be fair game for a paper about that team's model.
2. **The original team verifies their own model.** They agree the tolerance criteria and sign off on the rebuild before any comparison results are shown to anyone.
3. **No surprises.** Teams see results involving their model before co-authors or the public do, and they can respond in the paper.
4. **Co-authorship** for each participating team, plus the MIHPSA/Bansi-Matharu leads. Authorship order is agreed in sprint 1, not at the end.
5. **Outputs flow back.** The rebuilds, the attribution analyzer, the harmonised output spec and `ss.diff` are open and usable by every team on their own models.
6. **No winner language** ("better", "more accurate") anywhere, including talks and preprints.
7. **The consortium's process comes first.** Present to the HIV Modelling Consortium before submission, and offer to run this as a consortium activity if they want it.

## Sequence

| When | Who | Ask |
|---|---|---|
| Sprint 0–1 | **Anna Bershteyn, Daniel Citron** (EMOD, NYU) | Daniel is the bridge. Ask Anna to co-lead the EMOD arm and to sense-check the framing first, since she is a co-senior author of Bansi-Matharu |
| Sprint 1 | **Andrew Phillips, Loveleen Bansi-Matharu** (UCL; MIHPSA leads; Phillips leads the consortium) | Their blessing; access to the harmonised MIHPSA outputs; ideally co-leadership. Pitch: "the follow-up analysis your discussion section called for" |
| Sprint 1 | **John Stover, Robert Glaubius** (Goals, Avenir) | Consent to rebuild; confirm the GoalsARM version and Malawi inputs; agree verification tolerance |
| Sprint 1–2 | **Rowan Martin-Hughes, Debra ten Brink** (Optima, Burnet) | Same, as a second rebuild (Robyn has prior Optima ties) |
| Sprint 2 | **Edinah Mudimu** (consortium secretariat, UNISA) | Put it on the next consortium meeting agenda |
| Sprint 7 | Original teams, then the consortium | Draft review |
| Later | PopART (Pickles/Boily), Thembisa (Johnson), Synthesis | Invite into phase 2 (Zimbabwe and South Africa extension, Paper B); keep them informed now so nobody is blindsided |
| Country | **Rose Nyirenda** (Malawi MoH) | Check that the policy question (testing vs retention) is the one Malawi actually faces |

## Pitch (one paragraph, adapt per team)

> The MIHPSA comparison showed that models calibrated to the same data disagree by 33–75% about how much transmission comes from undiagnosed people, and the reasons couldn't be pinned down. We think we can now run the experiments that would: rebuild models in a common language, have each team verify their own rebuild, then swap one assumption at a time and recalibrate. We'd like to do this with you, as co-authors, with you signing off on how your model is represented. The tools will be open for every team to use on their own models.

## Open questions for Robyn

- Should this be pitched as a consortium activity from the start, or as an IDM-led paper with consortium partners?
- Who sends the first emails? Daniel to Anna and Robyn to Phillips is the obvious split.
- Is there Gates programme-officer context that should shape timing (e.g. MIHPSA follow-on funding)?
