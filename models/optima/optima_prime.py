"""
Optima′: Optima HIV (the Malawi project) as a declared Starsim model.

Each rate is Optima's probability per step of 0.2 years divided by 0.2, with Optima's products, so that Optima's
handling of time is kept (see docs/optima_inventory.md). Inputs are Optima's own series at dt=0.2.
"""
from pathlib import Path
import numpy as np, sciris as sc, starsim as ss

REF_DT = 0.2 # The step Optima's Malawi project was calibrated at
REFFILE = Path(__file__).resolve().parents[2] / 'optima_ref' / 'optima_malawi_ref.obj'
CD4 = ['acute', 'gt500', 'gt350', 'gt200', 'gt50', 'lt50']
UNTREATED = ['undx', 'dx', 'care', 'lost'] # Cascade states not on ART
TREATED = ['usvl', 'svl']


def load(reffile=REFFILE):
    """ Optima's inputs (simpars at dt=0.2) and its calibrated run """
    return sc.objdict(sc.load(reffile))


class Inputs:
    """ Optima's input series, as Starsim values by population group and year """
    def __init__(self, ref):
        self.sp = ref.simpars
        self.tvec = self.sp['tvec']
        self.pops = list(self.sp['popkeys'])
        self.npops = len(self.pops)

    def by(self, arr):
        """ A (pops × times) array, or one value per pop, as ss.by(pop=...) """
        arr = np.asarray(arr, dtype=float)
        if arr.ndim == 1:
            return ss.by(pop=dict(zip(self.pops, arr)))
        return ss.by(pop={p: ss.timeseries(self.tvec, row) for p, row in zip(self.pops, arr)})

    def series(self, row):
        """ One time series """
        return ss.timeseries(self.tvec, np.asarray(row, dtype=float))


def make_disease(ref, components=('demography', 'natural_history')):
    """ The Optima′ disease: Optima's 38 states, stratified by its 39 populations """
    inp = Inputs(ref)
    sp, pops = inp.sp, inp.pops
    names = [s.replace('-', '_') for s in ref.settings['statelabels']]
    st = sc.objdict({s.name: s for s in ss.states(' '.join(names))})
    hiv = [st[f'{c}_{k}'] for c in UNTREATED + TREATED for k in CD4]
    trs = sc.objdict()

    # Background death: Optima removes it from everyone (1-bg), after HIV death (1-d)
    bg = sp['death']*REF_DT # Probability per step, by pop and time
    d = np.array([sp[f'death{k}'] for k in CD4])*REF_DT # HIV death probability per step by CD4 (relhivdeath is 1 for every pop here)
    assert np.all(np.asarray(sp['hivdeath']) == 1), 'Relative HIV death rates other than 1 are not handled yet'
    tau = np.array([sp['progacute'], sp['proggt500'], sp['proggt350'], sp['proggt200'], sp['proggt50']])
    prog = 1 - np.exp(-REF_DT/tau) # Probability per step of moving to the next CD4 stage

    if 'demography' in components:
        for s in st.values(): # Uninfected and on ART: background death only (ART deaths come with treatment)
            if s.name in ('susreg', 'progcirc'):
                trs[f'bgdeath_{s.name}'] = ss.death(s, rate=ss.peryear(1)*inp.by(bg/REF_DT))

    if 'natural_history' in components:
        for c in UNTREATED:
            for i, k in enumerate(CD4):
                s = st[f'{c}_{k}']
                trs[f'hivdeath_{s.name}'] = ss.death(s, rate=ss.peryear(d[i]/REF_DT))
                trs[f'bgdeath_{s.name}'] = ss.death(s, rate=ss.peryear(1)*inp.by(bg*(1 - d[i])/REF_DT))
                if i < len(CD4) - 1:
                    trs[f'prog_{s.name}'] = s >> st[f'{c}_{CD4[i+1]}'] @ (ss.peryear(1)*inp.by(prog[i]*(1 - d[i])*(1 - bg)/REF_DT))

    # Births into F0-4 and M0-4, from all women in the mother populations, at Optima's birth rate per woman
    if 'demography' in components:
        bt = np.asarray(sp['birthtransit'])
        mothers = bt.any(axis=1)
        w = inp.by(np.where(mothers[:, None], sp['birth'], 0.0))
        dest = inp.by(bt[mothers].mean(axis=0)) # The share of births to each child population (the same for every mother here)
        assert np.allclose(bt[mothers], bt[mothers][0]), 'Child shares that differ by mother are not handled yet'
        everyone = sum(st.values()[1:], st.values()[0])
        trs['birth'] = ss.null >> st.susreg @ dest*(w*everyone).n

    # Ageing between bands (Optima's agerate per year, by source population), and risk transitions (FSW, Clients <-> general)
    if 'demography' in components:
        at, a = np.asarray(sp['agetransit']), sp['agerate']
        src_of = {j: i for i, j in zip(*np.nonzero(at))} # The band each band is aged into from
        for i, j in zip(*np.nonzero(at)):
            trs[f'age_{pops[i]}'] = ss.transfer(pop=(pops[i], pops[j]), rate=ss.peryear(1)*inp.series(at[i, j]*a[i]))
            if i in src_of: # Optima's old ageing code (projects before 2.12.0) ages people who arrived in a band earlier in the same step again: a skip of two bands
                h = src_of[i]
                trs[f'skip_{pops[h]}'] = ss.transfer(pop=(pops[h], pops[j]), rate=ss.peryear(1)*inp.series(at[h, i]*a[h]*at[i, j]*a[i]*REF_DT))
        rt = np.asarray(sp['risktransit'], dtype=float)
        size = sp['popsize']
        for i, j in zip(*np.nonzero(rt)):
            r = 1 - np.exp(-REF_DT/rt[i, j]) # Probability per step
            trs[f'risk_{pops[i]}_{pops[j]}'] = ss.transfer(pop=(pops[i], pops[j]), rate=ss.peryear(r/REF_DT))
            trs[f'risk_{pops[j]}_{pops[i]}'] = ss.transfer(pop=(pops[j], pops[i]), rate=ss.peryear(1)*inp.series(r/REF_DT*size[i]/size[j])) # Balanced: as many move back (population sizes are forced)

    # Initial state: Optima's own, as the share of each population in each state
    people0 = ref.raw['people'][:, :, 0]
    shares0 = people0/people0.sum(axis=0)
    init = {name: inp.by(shares0[i]) for i, name in enumerate(names) if shares0[i].any()}

    dis = ss.Disease(*st.values(), **trs, init=init, name='optima')
    dis.stratify(pop=dict(zip(pops, people0.sum(axis=0)/people0.sum())))
    return dis, st


class ForcePopsize(ss.Intervention):
    """
    Optima's population forcing, applied to the compartments each step: populations with no inflows from ageing or births
    gain or lose susceptibles to match their size; every population then has everyone not on ART scaled to match it.

    Rescaling compartments has no public Starsim interface yet, so this writes the engine's compartments directly.
    """
    def __init__(self, ref, **kwargs):
        super().__init__(**kwargs)
        sp = ref.simpars
        self.tvec, self.popsize = sp['tvec'], sp['popsize']
        inflows = np.asarray(sp['agetransit']).sum(axis=0) + np.asarray(sp['birthtransit']).sum(axis=0)
        self.noinflows = np.nonzero(inflows == 0)[0]
        self.statelabels = [s.replace('-', '_') for s in ref.settings['statelabels']]

    def step(self):
        eng = self.sim.diseases.optima.engine
        y, comps = eng.y, eng.state_comps
        rows = lambda names: np.concatenate([comps[n] for n in names])
        sus = rows(['susreg', 'progcirc'])
        notart = rows([n for n in self.statelabels if not n.startswith(tuple(TREATED))])
        art = rows([n for n in self.statelabels if n.startswith(tuple(TREATED))])
        year = self.sim.now.years if hasattr(self.sim.now, 'years') else float(self.sim.now)
        target = np.array([np.interp(year, self.tvec, row) for row in self.popsize])
        j = self.noinflows
        allsus = y[np.ix_(sus, j)].sum(axis=0)
        new = target[j] - y[:, j].sum(axis=0)
        y[np.ix_(sus, j)] *= 1 + new/allsus # Add (or remove) susceptibles, in proportion
        wanted = target - y[art].sum(axis=0)
        y[notart] *= wanted/y[notart].sum(axis=0)
        return


def make_sim(ref=None, components=('demography', 'natural_history'), dt=0.02, end=2030, **kwargs):
    ref = ref or load()
    dis, st = make_disease(ref, components)
    total = ref.raw['people'][:, :, 0].sum()
    interventions = [ForcePopsize(ref, name='force_popsize')] if 'demography' in components and ref.simpars['forcepopsize'] else []
    sim = ss.Sim(dis, interventions=interventions, solver='ode', start=1990, stop=end, dt=dt, total_pop=total, verbose=0, **kwargs)
    return sim


if __name__ == '__main__':
    T = sc.timer()
    sim = make_sim().run()
    T.toc('Optima′ run')
    r = sim.results.optima
    print({k: v for k, v in list(r.items())[:5]})
