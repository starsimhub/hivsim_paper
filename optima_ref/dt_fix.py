"""Find Optima's step-dependent rules: convert each group to its rate equivalent at dt=0.2 and measure the gap to the calibrated run."""
import sys, numpy as np
import optima as op
import model_dt

op.project.model = model_dt.model
P = op.loadproj('../files/Malawi_20220912.prj', verbose=0)
keys = ['numplhiv', 'numinci', 'numdeath', 'numdiag', 'numtreat', 'numsuppressed']
GROUPS = ['supp', 'acute', 'dwell', 'cascade', 'death', 'usvl', 'age']

def run(dt, fix=()):
    model_dt.FIX = set(fix)
    r = P.runsim(name='20220912', end=2030, dt=dt, verbose=0)
    return r, {k: r.main[k].tot[0] for k in keys}

ref_res, ref = run(0.2)
years = ref_res.tvec
sel = (years >= 2000) & (years <= 2030)
def gap(out):
    return {k: 100*np.max(np.abs(out[k][sel]/ref[k][sel] - 1)) for k in keys}
def show(label, g):
    print(f'{label:34s}' + ''.join(f'{g[k]:9.1f}' for k in keys) + f'{max(g.values()):9.1f}')

_, allfix = run(0.2, GROUPS)
print('dt=0.2, all fixes vs original: max diff', max(max(np.abs(allfix[k]-ref[k])) for k in keys))
print(f'\nMax % difference from calibrated run (dt=0.2), 2000-2030')
print(f'{"":34s}' + ''.join(f'{k[3:]:>9s}' for k in keys) + f'{"max":>9s}')
for dt in [float(a) for a in sys.argv[1:]] or [0.02]:
    print(f'-- dt={dt}')
    show('no fixes', gap(run(dt)[1]))
    for g in GROUPS:
        show(f'only {g}', gap(run(dt, [g])[1]))
    for i in range(2, len(GROUPS)+1):
        show('+'.join(GROUPS[:i]), gap(run(dt, GROUPS[:i])[1]))
