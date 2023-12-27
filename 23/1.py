from heapq import heappush, heappop
from common import parse, neighbours


area, max_y, max_x = parse()
start = (0, 1)
end = (max_y, max_x - 1)
distances = {}
max_hike = 0
heap = [(0, start, {start})]
while heap:
    cur_d, (y, x), visited = heappop(heap)
    if (y, x) in distances and distances[(y, x)] <= cur_d:
        continue
    distances[(y, x)] = cur_d
    if (y, x) == end and len(visited) - 1 > max_hike:
        max_hike = len(visited) - 1
        continue
    if (slope := area[(y, x)]) in '^<>v':
        down = ((y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x))['^<>v'.index(slope)]
        if down not in visited:
            visited.add(down)
            heappush(heap, (cur_d - 1, down, visited))
    else:
        for n in (n for n in neighbours(y, x, area) if n not in visited):
            heappush(heap, (cur_d - 1, n, visited | {n}))
print(max_hike)
