"""
Spike: a declared, Optima-style cascade on HIVsim's coded HIV natural history, in one agent sim.

Question: can a declared component and a coded one sit behind a shared interface, and what friction is there
at the seam? The interface used here, in agent terms:
    natural history -> cascade: hiv.infected, hiv.cd4 (CD4 band for AIDS-specific rates and CD4-first ART)
    cascade -> natural history: hiv.start_art(uids, p_effective_art), hiv.stop_art(uids), hiv.set_suppression(uids, bool)

Run: PYTHONPATH=<stisim v4 checkout> python seam.py
"""
import numpy as np
import sciris as sc
import starsim as ss
import stisim as sti

# --- The cascade: declared states and transitions (Optima's cascade axis, without the CD4 crossing) ----------------
def make_cascade(hiv):
    none, undx, dx, care, lost, usvl, svl = ss.states('none undx dx care lost usvl svl')
    aids = hiv.cd4 < 200 # A condition on the coded module's per-agent array
    hivtest = ss.par(ss.peryear(0.3), doc='Testing rate, CD4 above 200')
    aidstest = ss.par(ss.peryear(0.8), doc='Testing rate, CD4 below 200')
    cascade = ss.Disease(
        infection = ss.Transition(none, undx, dur=0, where=hiv.infected), # Enter the cascade when HIV infects them (no transmission of its own)
        testing   = undx >> dx @ hivtest + (aidstest - hivtest)*aids,
        linkage   = dx >> care @ ss.years(0.5),
        loss      = usvl + svl + care >> lost @ ss.peryear(0.05),
        returning = lost >> care @ ss.peryear(0.2),
        failure   = svl >> usvl @ ss.peryear(0.05),
        initiate  = ss.Transition(care, svl), # Undriven: moved by the number-on-ART target (see Seam). FRICTION 1: a split with p= can't be undriven, so the 90/10 split into svl/usvl is the seam's code
        first = 'none', name = 'cascade',
    )
    return cascade

# --- The seam: Optima's number-on-ART target, and passing ART changes to the natural history ------------------------
class Seam(ss.Connector):
    """ Code where the two components meet """
    def __init__(self, numtx, **kwargs):
        super().__init__(**kwargs)
        self.numtx = numtx # Number to have on ART, by year (Optima's numtx)
        self.lag = []      # Steps between a cascade move and the natural history hearing of it
        self.supp = ss.bernoulli(p=0.9) # Share of initiators who suppress (Optima's treatvs)

    def step(self):
        sim = self.sim
        hiv, cas = sim.diseases.hiv, sim.diseases.cascade
        # 1. Bring the natural history's ART status into line with the cascade's. FRICTION 3: the cascade's own moves (loss,
        #    failure) happen in its step(), after the connectors, so the natural history hears of them a step later
        self.sync(hiv, cas)
        # 2. The number-on-ART target, lowest CD4 first
        want = np.interp(sim.t.now('year'), list(self.numtx.keys()), list(self.numtx.values()))
        have = (cas.usvl | cas.svl).count()
        n = int(round(want - have))
        if n > 0:
            eligible = cas.care.uids
            order = np.argsort(hiv.cd4[eligible], kind='stable')
            chosen = eligible[order[:n]]
            supp = self.supp.filter(chosen)
            cas.move(supp, cas.svl)
            cas.move(chosen.remove(supp), cas.usvl)
            self.sync(hiv, cas) # At once, for the moves made here
        return

    def sync(self, hiv, cas):
        """ Make the natural history's ART status match the cascade's: start, stop, and suppression """
        on_art = (cas.usvl | cas.svl) & hiv.infected # Dead agents are in neither
        start = (on_art & ~hiv.on_art).uids
        stop = (hiv.on_art & ~on_art).uids
        if len(start):
            supp = start[cas.svl[start]]
            hiv.start_art(supp, p_effective_art=1.0)
            hiv.start_art(start.remove(supp), p_effective_art=0.0)
        if len(stop):
            hiv.stop_art(stop)
        fail = (cas.usvl & hiv.on_effective_art).uids
        resupp = (cas.svl & hiv.on_nonsuppressive_art).uids
        if len(fail): hiv.set_suppression(fail, False)
        if len(resupp): hiv.set_suppression(resupp, True)
        self.n_changed = len(start) + len(stop) + len(fail) + len(resupp)

numtx = {1990: 0, 2004: 0, 2010: 100, 2020: 400, 2030: 500} # Per 5,000 agents, made up

hiv = sti.HIV(beta_m2f=0.05, init_prev=0.05, dur_on_art=ss.constant(ss.years(200))) # The cascade, not the natural history, decides who stops ART
cascade = make_cascade(hiv)
sim = sti.Sim(diseases=[hiv, cascade], connectors=Seam(numtx, name='seam'), n_agents=5000, start=1990, stop=2030, rand_seed=1, verbose=0)
sim.init()
sim.run()
r = sim.results
for key in ['undx', 'dx', 'care', 'lost', 'usvl', 'svl']:
    print(f'{key:5s}', np.round(r.cascade[key][::40]).astype(int))
hiv = sim.diseases.hiv; cas = sim.diseases.cascade
print('agree at end:', 'on ART', ((cas.usvl | cas.svl).uids.tolist() == hiv.on_art.uids.tolist()), '| suppressed', (cas.svl.uids.tolist() == hiv.on_effective_art.uids.tolist()))
print('in cascade = infected:', (cas.undx | cas.dx | cas.care | cas.lost | cas.usvl | cas.svl).count(), hiv.infected.count())
print('hiv results with art:', [k for k in sim.results.hiv.keys() if 'art' in k][:8])
print('initiate flow total:', r.cascade.initiate.values.sum(), '| on ART at end:', (cas.usvl | cas.svl).count())
print('loss flow total:', r.cascade.loss.values.sum(), '| failure:', r.cascade.failure.values.sum())
