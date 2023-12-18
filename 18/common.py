import shapely


def parse(parse_line):
    directions = []
    lengths = []
    with open('input.txt') as data:
        for d, l in map(parse_line, data):
            directions.append(d)
            lengths.append(l)
    return directions, lengths


def area(directions, lengths):
    y, x = 0, 0
    corners = []
    for (i, d), l in zip(enumerate(directions), lengths):
        k = directions[(i - 1) % len(directions)]
        j = directions[(i + 1) % len(directions)]
        if d in 'UD':
            y += -l if d == 'U' else l
            if k == 'L' and j == 'R':
                y -= 1
            elif k == 'R' and j == 'L':
                y += 1
        elif d in 'LR':
            x += -l if d == 'L' else l
            if k == 'D' and j == 'U':
                x -= 1
            elif k == 'U' and j == 'D':
                x += 1
        corners.append((y, x))
    return int(shapely.Polygon(corners).area)
