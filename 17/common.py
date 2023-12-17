from heapq import heappush, heappop
from math import inf


def parse():
    area = {}
    with open('input.txt') as data:
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                area[(y, x)] = int(c)
    return area, y, x


def get_next(y, x, d, s, min_straight, max_straight):
    next_steps = []
    if s < max_straight:
        match d:
            case 'E':
                next_steps.append((y, x + 1, d, s + 1))
            case 'W':
                next_steps.append((y, x - 1, d, s + 1))
            case 'S':
                next_steps.append((y + 1, x, d, s + 1))
            case _:
                next_steps.append((y - 1, x, d, s + 1))
    if s >= min_straight:
        if d in 'EW':
            next_steps.append((y - 1, x, 'N', 1))
            next_steps.append((y + 1, x, 'S', 1))
        else:
            next_steps.append((y, x - 1, 'W', 1))
            next_steps.append((y, x + 1, 'E', 1))
    return next_steps


def find_path(area, max_y, max_x, min_straight, max_straight):
    distances = dict()
    distances[(0, 1, 'E', 1)] = 0
    distances[(1, 0, 'S', 1)] = 0
    heap = []
    heappush(heap, (area[(0, 1)], 0, 1, 'E', 1))
    heappush(heap, (area[(1, 0)], 1, 0, 'S', 1))

    while heap:
        current = heappop(heap)
        cur_d, y, x, cur_dir, straight = current
        if (y, x) == (max_y, max_x) and straight >= min_straight:
            return cur_d
        for next_y, next_x, next_dir, next_straight in get_next(y, x, cur_dir, straight, min_straight, max_straight):
            if (next_y, next_x) not in area:
                continue
            next_d = cur_d + area[(next_y, next_x)]
            if distances.get((next_y, next_x, next_dir, next_straight), inf) > next_d:
                heappush(heap, (next_d, next_y, next_x, next_dir, next_straight))
                distances[(next_y, next_x, next_dir, next_straight)] = next_d
