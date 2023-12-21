from numpy.polynomial.polynomial import Polynomial
from common import parse, reachable_plots

area, start, max_y, max_x = parse()
sequence = []
for i in range(3):
    sequence.append(reachable_plots(i * (max_y + 1) + start[0], area, start, True, max_y, max_x, i % 2))
print(int(Polynomial.fit([0, 1, 2], sequence, 2)(26501365 // (max_y + 1))))
