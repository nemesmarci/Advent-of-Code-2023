from heapq import heappush, heappop
from collections import defaultdict
from common import parse, neighbours


def paths(area, nodes):
    graph = defaultdict(dict)
    for node in nodes:
        for neighbour in (n for n in neighbours(*node, area)):
            visited = {node}
            cur = neighbour
            while cur not in nodes:
                visited.add(cur)
                cur = next(n for n in neighbours(*cur, area) if n not in visited)
            graph[node][cur] = len(visited)
            graph[cur][node] = len(visited)
    return graph


area, max_y, max_x = parse()
start = (0, 1)
end = (max_y, max_x - 1)
nodes = [start] + [n for n in area if len(neighbours(*n, area)) > 2] + [end]
graph = paths(area, nodes)
max_hike = 0
heap = [(0, start, {start})]
while heap:
    cur_d, (y, x), visited = heappop(heap)
    if (y, x) == end and -cur_d > max_hike:
        max_hike = -cur_d
        continue
    for n in (n for n in graph[(y, x)] if n not in visited):
        heappush(heap, (cur_d - graph[(y, x)][n], n, visited | {n}))
print(max_hike)
