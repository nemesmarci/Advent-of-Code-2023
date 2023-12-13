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
    area[start] = start_pipe_shape(area, start)
    return area, start, y, x


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
    loop = {start}
    if area[start] in '|LJ':
        cur_dir = 'N'
    elif area[start] in 'F7':
        cur_dir = 'S'
    else:
        cur_dir = 'E'
    cur_node = start
    while True:
        cur_node, cur_dir = next_in_loop(cur_node, cur_dir, area)
        loop.add(cur_node)
        if cur_node == start:
            return loop
