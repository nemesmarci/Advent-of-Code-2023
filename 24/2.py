import z3
from common import parse

hails = parse()
xs, ys, zs, us, vs, ws = z3.Reals('xs, ys, zs, us, vs, ws')
T = z3.RealVector('t', len(hails))
solver = z3.Solver()
for t, ((xh, yh, zh), (uh, vh, wh)) in zip(T, hails):
    solver.add(t >= 0)
    solver.add(xh + uh * t == xs + us * t)
    solver.add(yh + vh * t == ys + vs * t)
    solver.add(zh + wh * t == zs + ws * t)

solver.check()
m = solver.model()
print(m[xs].as_long() + m[ys].as_long() + m[zs].as_long())
