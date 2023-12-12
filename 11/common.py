from itertools import combinations


def parse():
    area = dict()
    galaxies = set()
    with open('input.txt') as data:
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                area[(y, x)] = c
                if c == '#':
                    galaxies.add((y, x))
    return area, galaxies, y + 1, x + 1


def solve(offset):
    d = 0
    area, galaxies, max_y, max_x = parse()
    pairs = combinations(galaxies, 2)
    empty_rows = {y for y in range(max_y)
                  if all(area[(y, x)] == '.' for x in range(max_x))}
    empty_cols = {x for x in range(max_x)
                  if all(area[(y, x)] == '.' for y in range(max_y))}
    for (y1, x1), (y2, x2) in pairs:
        if y2 < y1:
            y1, y2 = y2, y1
        if x2 < x1:
            x1, x2 = x2, x1
        d += y2 - y1
        for row in empty_rows:
            if row in range(y1 + 1, y2 + 1):
                d += offset
        d += x2 - x1
        for col in empty_cols:
            if col in range(x1 + 1, x2 + 1):
                d += offset
    return d
