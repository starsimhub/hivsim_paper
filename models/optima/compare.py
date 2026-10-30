"""Compare Optima′ with Optima, one component test at a time (references from optima_ref/component_ref.py)"""
import sys
from pathlib import Path
import numpy as np, sciris as sc
import optima_prime as opp

REFS = Path(__file__).resolve().parents[2] / 'optima_ref' / 'component_refs.obj'
COMPONENTS = dict(A=('demography', 'natural_history'))
WINDOWS = dict(A=(1991, 2000)) # Without transmission, people with HIV die out: compare while there are some

def summarise(people, years):
    """ Stocks from a (states × pops × years) array """
    hiv = people[2:]
    out = dict(popsize=people.sum(axis=(0, 1)), plhiv=hiv.sum(axis=(0, 1)))
    for i, k in enumerate(opp.CD4):
        out[f'plhiv_{k}'] = hiv[i::6].sum(axis=(0, 1))
    out['plhiv_15_49'] = None
    return {k: v for k, v in out.items() if v is not None}

def prime_people(sim, years):
    """ Optima′'s compartments as a (states × pops × years) array, at whole years """
    r = sim.results.optima
    names = [s.replace('-', '_') for s in opp.load().settings['statelabels']]
    out = []
    for n in names:
        res = r[n].by('pop') # One series per population (on its own time points)
        t = np.array([d.years for d in res.timevec])
        out.append(np.asarray(res)[[np.argmin(abs(t - y)) for y in years]].T)
    return np.array(out)

def gaps(a, b, years, window):
    """ Max difference over the window, as a % of the largest value of the reference in the window """
    sel = (years >= window[0]) & (years <= window[1])
    return {k: 100*np.max(np.abs(b[k][sel] - a[k][sel]))/np.max(np.abs(a[k][sel])) for k in a}

if __name__ == '__main__':
    refs = sc.load(REFS)
    for name in sys.argv[1:] or COMPONENTS:
        ref = refs[name]
        years = ref['original']['years']
        T = sc.timer()
        sim = opp.make_sim(components=COMPONENTS[name], dt=ref['dt'], end=int(years[-1])).run()
        print(f'Test {name} ({", ".join(COMPONENTS[name])}): Optima′ ran in {T.toc(output=True):.1f} s')
        o, h = summarise(ref['original']['people'], years), summarise(ref['harness']['people'], years)
        p = summarise(prime_people(sim, years), years)
        window = WINDOWS[name]
        print(f'Max difference, {window[0]}-{window[1]}, as % of the reference:')
        print(f'{"":28s}' + ''.join(f'{k[6:] or k:>9s}' for k in o))
        for label, a, b in [('harness vs original', o, h), ("Optima′ vs harness", h, p), ("Optima′ vs original", o, p)]:
            g = gaps(a, b, years, window)
            print(f'{label:28s}' + ''.join(f'{g[k]:9.2f}' for k in o))
