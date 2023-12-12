from collections import defaultdict
from heapq import heappush, heappop
from common import parse, find_loop


def get_neighbours(current):
    return ((current[0] - 1, current[1]),
            (current[0], current[1] - 1),
            (current[0], current[1] + 1),
            (current[0] + 1, current[1]))


def start_pipe_shape(area, start):
    up, left, right, down = get_neighbours(start)
    if area[up] in '|7F':
        if area[down] in '|LJ':
            return '|'
        if area[left] in '-LF':
            return 'J'
        if area[right] in '-J7':
            return 'L'
    if area[down] in '|LJ':
        if area[left] in '-LF':
            return '7'
        if area[right] in '-J7':
            return 'F'
    return '-'


def reduced_coords(y, x):
    ry, n = divmod(y, 3)
    rx, m = divmod(x, 3)
    return (ry, rx) if n == m == 0 else None


def fill(start, area):
    seen = set()
    heap = []
    heappush(heap, start)
    while heap:
        cur_node = heappop(heap)
        if cur_node in seen:
            continue
        seen.add(cur_node)
        neighbours = get_neighbours(cur_node)
        for n in neighbours:
            if n not in seen and area[n] == '.':
                heappush(heap, n)
    return seen


def enclosed(tile, area, enclosed_tiles, max_y, max_x):
    seen = set()
    heap = []
    heappush(heap, (tile[0] * 3, tile[1] * 3))
    while heap:
        cur_node = heappop(heap)
        if (original_tile := reduced_coords(*cur_node)) \
                and original_tile in enclosed_tiles:
            break
        if cur_node in seen:
            continue
        seen.add(cur_node)
        neighbours = get_neighbours(cur_node)
        for n in neighbours:
            if (not (0 <= n[0] < max_y)) or (not (0 <= n[1] < max_x)):
                return False
            if n not in seen and area[n] == '.':
                heappush(heap, n)
    return True


def zoom_in(area):
    zoomed_in = defaultdict(lambda: '.')
    for y, x in loop:
        c = area[(y, x)]
        zoomed_in[(3 * y + 1, 3 * x + 1)] = 'X'
        if c in '|LJ':
            zoomed_in[(3 * y, 3 * x + 1)] = 'X'
        if c in '|7F':
            zoomed_in[(3 * y + 2, 3 * x + 1)] = 'X'
        if c in '-J7':
            zoomed_in[(3 * y + 1, 3 * x)] = 'X'
        if c in '-LF':
            zoomed_in[(3 * y + 1, 3 * x + 2)] = 'X'
    return zoomed_in


area, start = parse()
_, loop = find_loop(area, start)
area[start] = start_pipe_shape(area, start)
max_y = max(b[0] for b in area) * 3
max_x = max(b[1] for b in area) * 3
zoomed_in = zoom_in(area)

enclosed_tiles = set()
for tile in filter(lambda x: x not in loop and x not in enclosed_tiles, area):
    if enclosed(tile, zoomed_in, enclosed_tiles, max_y, max_x):
        enclosed_tiles.add(tile)
        enclosed_tiles |= fill(tile, area)

print(len(enclosed_tiles))
