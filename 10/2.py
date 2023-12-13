from heapq import heappush, heappop
from common import parse, find_loop


def get_neighbours(current):
    return ((current[0] - 1, current[1]),
            (current[0], current[1] - 1),
            (current[0], current[1] + 1),
            (current[0] + 1, current[1]))


def fill(start, loop, max_y, max_x):
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
            if n not in seen and 0 <= n[0] < max_y and 0 <= n[1] < max_x and n not in loop:
                heappush(heap, n)
    return seen


def enclosed(tile, loop, max_y, max_x):
    seen = set()
    heap = []
    heappush(heap, tile)
    while heap:
        cur_node = heappop(heap)
        if cur_node in seen:
            continue
        seen.add(cur_node)
        neighbours = get_neighbours(cur_node)
        for n in neighbours:
            if not 0 <= n[0] < max_y or not 0 <= n[1] < max_x:
                return False
            if n not in seen and n not in loop:
                heappush(heap, n)
    return True


def zoom_in(loop):
    zoomed_in = set()
    for y, x in loop:
        c = area[(y, x)]
        zoomed_in.add((3 * y + 1, 3 * x + 1))
        if c in '|LJ':
            zoomed_in.add((3 * y, 3 * x + 1))
        if c in '|7F':
            zoomed_in.add((3 * y + 2, 3 * x + 1))
        if c in '-J7':
            zoomed_in.add((3 * y + 1, 3 * x))
        if c in '-LF':
            zoomed_in.add((3 * y + 1, 3 * x + 2))
    return zoomed_in


area, start, y, x = parse()
loop = find_loop(area, start)
max_y = y * 3 + 3
max_x = x * 3 + 3
zoomed_in = zoom_in(loop)

enclosed_tiles = set()
enclosed_zoom = set()
free_zoom = set()

for tile in filter(lambda x: x not in loop, area):
    zoom = tile[0] * 3, tile[1] * 3
    if zoom in enclosed_zoom:
        enclosed_tiles.add(tile)
    elif zoom in free_zoom:
        continue
    elif enclosed(zoom, zoomed_in, max_y, max_x):
        enclosed_tiles.add(tile)
        enclosed_zoom |= fill(zoom, zoomed_in, max_y, max_x)
    else:
        free_zoom |= fill(zoom, zoomed_in, max_y, max_x)
print(len(enclosed_tiles))
