from collections import defaultdict
from heapq import heappush, heappop


def parse():
    area = defaultdict(lambda: '.')
    with open('input.txt') as data:
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                if c == 'S':
                    start = (y, x)
                area[(y, x)] = c
    return area, start, y, x


def next_in_loop(current, direction, area):
    if direction == 'N':
        next_node = (current[0] - 1, current[1])
        blocked = '-LJ.S'
        free = {'|': 'N', '7': 'W', 'F': 'E'}
    elif direction == 'E':
        next_node = (current[0], current[1] + 1)
        blocked = '|LF.S'
        free = {'-': 'E', 'J': 'N', '7': 'S'}
    elif direction == 'S':
        next_node = (current[0] + 1, current[1])
        blocked = '-7F.S'
        free = {'|': 'S', 'L': 'E', 'J': 'W'}
    else:
        next_node = (current[0], current[1] - 1)
        blocked = '|J7.S'
        free = {'-': 'W', 'L': 'N', 'F': 'S'}
    next_dir = area[next_node]
    return None if next_dir in blocked else (next_node, free[next_dir])


def find_loop(area, start):
    distances = {start: 0}
    loop = {start}
    heap = []
    heappush(heap, (0, start, 'N'))
    heappush(heap, (0, start, 'W'))
    heappush(heap, (0, start, 'S'))
    heappush(heap, (0, start, 'E'))

    while heap:
        cur_d, cur_node, cur_dir = heappop(heap)
        if (next_item := next_in_loop(cur_node, cur_dir, area)) is None:
            continue
        loop.add(next_item[0])
        next_node, next_dir = next_item
        new_d = cur_d + 1
        if next_node not in distances or new_d < distances[next_node]:
            heappush(heap, (new_d, next_node, next_dir))
            distances[next_node] = new_d

    return distances, loop
