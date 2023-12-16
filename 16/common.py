from heapq import heappush, heappop

rules = {'R': {'|': 'UD', '\\': 'D', '/': 'U', '.': 'R', '-': 'R'},
         'L': {'|': 'UD', '\\': 'U', '/': 'D', '.': 'L', '-': 'L'},
         'D': {'-': 'LR', '\\': 'R', '/': 'L', '.': 'D', '|': 'D'},
         'U': {'-': 'LR', '\\': 'L', '/': 'R', '.': 'U', '|': 'U'}}


def parse():
    with open('input.txt') as data:
        area = {}
        for y, line in enumerate(data):
            for x, c, in enumerate(line.strip()):
                area[(y, x)] = c
    return area, y, x


def energized(heap, area):
    seen = set()
    while heap:
        current = heappop(heap)
        if current in seen:
            continue
        seen.add(current)
        (y, x), cur_d = current
        match cur_d:
            case 'R': next_tile = y, x + 1
            case 'L': next_tile = y, x - 1
            case 'D': next_tile = y + 1, x
            case _: next_tile = y - 1, x
        if next_tile in area:
            for tile in ((next_tile, d) for d in rules[cur_d][area[next_tile]]):
                heappush(heap, tile)
    return len({x[0] for x in seen})
