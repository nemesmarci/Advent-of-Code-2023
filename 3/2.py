from collections import defaultdict
from common import parse


def near_gear(schematic, part, y, x):
    return next(((i, j)
                for i in range(y - 1, y + 2)
                for j in range(x - 1, x + len(str(part)) + 1)
                if schematic[(i, j)] == '*'), None)


schematic, parts = parse()
gears = defaultdict(list)
for coord, part in parts.items():
    if gear := near_gear(schematic, part, *coord):
        gears[gear].append(part)
print(sum(connected[0] * connected[1] for gear, connected in gears.items()
          if len(connected) == 2))
