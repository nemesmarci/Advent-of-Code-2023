from common import parse, reachable_plots

area, start, max_y, max_x = parse()
print(reachable_plots(64, area, start, False, max_y, max_x, True))
