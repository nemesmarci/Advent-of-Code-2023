from heapq import heappush, heappop


def around(y, x):
    return (y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)


def parse():
    area = {}
    with open('input.txt') as data:
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                if c == 'S':
                    start = y, x
                    c = '.'
                area[(y, x)] = c
    return area, start, y, x


def reachable_plots(steps, area, start, infinite, max_y, max_x, even):
    visited = set()
    reachable = 0
    heap = [(0, start, (0, 0))]
    while heap:
        current_steps, current_plot, map_tile = heappop(heap)
        if current_steps > steps:
            continue
        if (current_plot, map_tile) in visited:
            continue
        for n in around(*current_plot):
            (y, x), (map_y, map_x) = n, map_tile
            if infinite:
                if y == - 1:
                    y = max_y
                    map_y -= 1
                elif y == max_y + 1:
                    y = 0
                    map_y += 1
                if x == -1:
                    x = max_x
                    map_x -= 1
                elif x == max_x + 1:
                    x = 0
                    map_x += 1
            if area[(y, x)] == '.':
                heappush(heap, (current_steps + 1, (y, x), (map_y, map_x)))
        if current_steps % 2 != even:
            visited.add((current_plot, map_tile))
            reachable += 1
    return reachable
