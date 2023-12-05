from common import parse

with open('input.txt') as data:
    seeds, map_ranges = parse(data)

min_loc = None
for target in seeds:
    for m in map_ranges:
        target = next((dest[target - source.start] for source, dest in m
                       if target in source), target)
    if min_loc is None or target <= min_loc:
        min_loc = target
print(min_loc)
