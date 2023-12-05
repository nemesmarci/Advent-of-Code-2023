from common import parse

with open('input.txt') as data:
    seeds, map_ranges = parse(data)

locations = []
for target in seeds:
    for m in map_ranges:
        target = next((dest[target - source.start] for source, dest in m
                       if target in source), target)
    locations.append(target)
print(min(locations))
