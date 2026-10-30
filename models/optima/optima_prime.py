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
OPTIONS = sc.objdict(age_skip=True, age_scale=1.0, risk=True, skip_scale=1.0) # For checks: Optima's ageing band-skip, and a factor on ageing rates
TREATED = ['usvl', 'svl']
NEXT = dict(undx='dx', dx='care', care='lost', lost='care') # Where each untreated cascade state moves to
AIDS = CD4.index('gt50') # CD4 stages from here on are AIDS (Optima's settings.aidsind)


def load(reffile=REFFILE):
    """ Optima's inputs (simpars at dt=0.2) and its calibrated run """
    return sc.objdict(sc.load(reffile))


def cascade_probs(sp):
    """
    Optima's probabilities, in a step of 0.2 years, of moving along the cascade for those not on ART (model.py, "Calculate
    probabilities of shifting along cascade"): for each untreated cascade state, an array of CD4 stage × population × time
    """
    shape = sp['death'].shape
    full = lambda x: np.broadcast_to(np.asarray(x, dtype=float), shape)
    aids = lambda base, aidsval: np.array([base if i < AIDS else aidsval for i in range(len(CD4))])
    test, aidstest = full(sp['hivtest']*REF_DT), full(sp['aidstest']*REF_DT)
    link, aidslink = 1 - np.exp(-REF_DT/full(np.maximum(1e-3, sp['linktocare']))), 1 - np.exp(-REF_DT/full(np.maximum(1e-3, sp['aidslinktocare'])))
    ret, loss, aidsloss = full(sp['returntocare']*REF_DT), full(sp['leavecare']*REF_DT), full(sp['aidsleavecare']*REF_DT)
    return dict(
        undx = aids(test, np.maximum(aidstest, test)),
        dx   = aids(link, np.maximum(aidslink, link)),
        care = aids(loss, np.minimum(aidsloss, loss)),
        lost = aids(ret, 1 - (1 - aidstest)*(1 - ret)),
    )


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
        return ss.by(pop={p: ss.timeseries(self.tvec, row, mode='linear') for p, row in zip(self.pops, arr)})

    def series(self, row):
        """ One time series """
        return ss.timeseries(self.tvec, np.asarray(row, dtype=float), mode='linear')


class Transmission:
    """
    Optima's force of infection (model.py, "Calculate probability of getting infected"), worked out once a step from the
    compartments at its start, as Optima does. Returns the rate of infection (per year) for each population, for the
    uncircumcised and circumcised susceptibles: Optima's probability of infection in a step of 0.2 years, divided by 0.2.
    """
    def __init__(self, ref):
        sp, st = ref.simpars, ref.settings
        self.tvec = sp['tvec']
        pops = list(sp['popkeys'])
        self.names = [s.replace('-', '_') for s in st['statelabels']]
        self.eps = 1e-3 # Optima's settings.eps
        male, female = np.asarray(sp['male']), np.asarray(sp['female'])

        # Infectiousness of each state (Optima's alltrans)
        cd4trans = np.array([sp[f'cd4trans{k}'] for k in CD4])*sp['transnorm']
        dxfactor = 1 - sp['effdx']
        alltrans = np.zeros(len(self.names))
        for c, factor in dict(undx=1, dx=dxfactor, care=dxfactor, lost=dxfactor, usvl=dxfactor*(1 - sp['efftxunsupp'])*dxfactor, svl=dxfactor*(1 - sp['efftxsupp'])*dxfactor).items():
            alltrans[[self.names.index(f'{c}_{k}') for k in CD4]] = cd4trans*factor
        self.alltrans = alltrans
        self.hiv = alltrans > 0

        # Effects on susceptibility by population, time, and circumcision status (Optima's alleff)
        prepeff = 1 - sp['effprep']*sp['prep'] - sp['effpep']*np.minimum(sp['pep'], 1 - sp['prep'])
        stieff = 1 + sp['effsti']*sp['stiprev']
        circeff = 1 - sp['propcirc']*sp['effcirc']
        allcirceff = np.outer([1, 1 - sp['effcirc']], male) + np.outer([1, 1], female) # Circumcision status × population
        self.alleff = np.einsum('ab,ab,ab,ca->acb', prepeff, stieff, circeff, allcirceff) # Population × circumcision status × time

        # Partnerships: acts per year, per-act probability, condom effect (Optima's version < 2.12.0 behaviour)
        p1, p2, acts, trans, cond = [], [], [], [], []
        for act in ['reg', 'cas', 'com']:
            for key in sorted(sp[f'acts{act}']):
                i, j = pops.index(key[0]), pops.index(key[1])
                total = np.asarray(sp[f'acts{act}'][key], dtype=float)*np.ones(len(self.tvec))
                if   male[i] and male[j]:   t = (sp['transmmi'] + sp['transmmr'])/2 # Insertive and receptive acts half each
                elif male[i] and female[j]: t = sp['transmfi']
                elif female[i] and male[j]: t = sp['transmfr']
                else: raise ValueError(f'Cannot tell the sexes of {key}')
                c = sp[f'cond{act}'].get(key, sp[f'cond{act}'].get((key[1], key[0]), 0.0))
                p1.append(i); p2.append(j); acts.append(total); trans.append(t*np.ones(len(self.tvec))); cond.append(1 - np.asarray(c)*sp['effcondom']*np.ones(len(self.tvec)))
        self.p1, self.p2 = np.array(p1), np.array(p2)
        self.acts, self.trans, self.cond = np.array(acts), np.array(trans), np.array(cond)
        self.force, self.inhomopar = np.asarray(sp['force'], dtype=float), np.asarray(sp['inhomo'], dtype=float)
        self.bg = sp['death']*REF_DT + sp['propemigrate']*REF_DT
        self.npops = len(pops)
        self._ti, self._rate = None, None

    def at(self, arr, year):
        """ Linear interpolation of a series over Optima's dt=0.2 time points (last axis) """
        i = int(np.clip(np.searchsorted(self.tvec, year, side='right') - 1, 0, len(self.tvec) - 2))
        w = np.clip((year - self.tvec[i])/(self.tvec[i+1] - self.tvec[i]), 0, 1)
        return arr[..., i]*(1 - w) + arr[..., i+1]*w

    def people(self, sim):
        eng = sim.diseases.optima.engine
        return np.array([eng.y[eng.state_comps[n]].sum(axis=0) for n in self.names]) # States × populations

    def rates(self, sim):
        if self._ti == sim.ti:
            return self._rate
        year = sim.now.years
        people = self.people(sim)
        allpeople = people.sum(axis=0)
        effprev = self.alltrans[:, None]*people/allpeople # States × populations
        prev = people[self.hiv].sum(axis=0)/allpeople
        h = self.inhomopar
        inhomo = (h + self.eps)/(np.exp(h + self.eps) - 1)*np.exp(h*(1 - prev))

        acts = self.at(self.acts, year)*REF_DT
        whole, frac = np.floor(acts), acts - np.floor(acts)
        alleff = self.at(self.alleff, year)[self.p1] # Partnerships × circumcision status
        q = (self.at(self.trans, year)*self.at(self.cond, year))[:, None, None]*alleff[:, :, None]*effprev[self.hiv][:, self.p2].T[:, None, :] # Partnerships × circ × infected states
        noinf = (1 - np.minimum(frac[:, None, None]*q, 1))*(1 - np.minimum(q*(whole[:, None, None] != 0), 1))**whole[:, None, None]
        lognoinf = np.zeros((self.npops, self.npops) + q.shape[1:]) # Acquiring pop × partner pop × circ × infected state
        np.add.at(lognoinf, (self.p1, self.p2), np.log(noinf))
        bg = self.at(self.bg, year)
        prob = (1 - np.exp(lognoinf)).sum(axis=(1, 3)).T*self.force*inhomo*(1 - bg) # Circ × acquiring pop
        prob = np.minimum(prob, 1 - self.eps - bg.max())
        self._ti, self._rate = sim.ti, prob/REF_DT
        return self._rate


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

    if 'transmission' in components:
        foi = Transmission(ref)
        for i, s in enumerate([st.susreg, st.progcirc]):
            trs[f'infection_{s.name}'] = s >> st.undx_acute @ ss.by(pop=lambda sim, i=i: ss.peryear(foi.rates(sim)[i]))

    if 'demography' in components:
        for s in st.values(): # Uninfected and on ART: background death only (ART deaths come with treatment)
            if s.name in ('susreg', 'progcirc'):
                trs[f'bgdeath_{s.name}'] = ss.death(s, rate=ss.peryear(1)*inp.by(bg/REF_DT))

    if 'natural_history' in components:
        q = cascade_probs(sp) if 'cascade' in components else {c: np.zeros((len(CD4),) + bg.shape) for c in UNTREATED}
        for c in UNTREATED:
            for i, k in enumerate(CD4):
                s = st[f'{c}_{k}']
                trs[f'hivdeath_{s.name}'] = ss.death(s, rate=ss.peryear(d[i]/REF_DT))
                trs[f'bgdeath_{s.name}'] = ss.death(s, rate=ss.peryear(1)*inp.by(bg*(1 - d[i])/REF_DT))
                survive = (1 - d[i])*(1 - bg) # Optima applies death first, and every other move to those who survive it
                p = prog[i] if i < len(CD4) - 1 else 0 # No progression from CD4<50
                moves = {f'{c}_{CD4[min(i+1, 5)]}': p*(1 - q[c][i]), f'{NEXT[c]}_{k}': (1 - p)*q[c][i], f'{NEXT[c]}_{CD4[min(i+1, 5)]}': p*q[c][i]}
                for dst, prob in moves.items():
                    if dst != s.name and np.any(prob):
                        trs[f'{s.name}_to_{dst}'] = s >> st[dst] @ (ss.peryear(1)*inp.by(prob*survive/REF_DT))

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
        onward = {i: j for i, j in zip(*np.nonzero(at))} # The band each band ages into
        for i, j in onward.items():
            rate = at[i, j]*a[i]
            if OPTIONS.age_skip and j in onward: # Optima's old ageing code (projects before 2.12.0) ages people who arrive in a band again in the same step, so some of those leaving skip it
                k = onward[j]
                skip = rate*at[j, k]*a[j]*REF_DT
                trs[f'skip_{pops[i]}'] = ss.transfer(pop=(pops[i], pops[k]), rate=ss.peryear(1)*inp.series(OPTIONS.skip_scale*skip))
                rate = rate - OPTIONS.skip_scale*skip
            trs[f'age_{pops[i]}'] = ss.transfer(pop=(pops[i], pops[j]), rate=ss.peryear(1)*inp.series(OPTIONS.age_scale*rate))
        rt = np.asarray(sp['risktransit'], dtype=float)
        size = sp['popsize']
        for i, j in zip(*np.nonzero(rt)) if OPTIONS.risk else []:
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
