from common import parse


def has_symbol(schematic, part, y, x):
    return any((c := schematic[(i, j)]) != '.' and not c.isnumeric()
               for i in range(y - 1, y + 2)
               for j in range(x - 1, x + len(str(part)) + 1))


schematic, parts = parse()
print(sum(part for coord, part in parts.items()
          if has_symbol(schematic, part, *coord)))
