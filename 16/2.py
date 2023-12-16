from common import parse, energized, rules

area, max_y, max_x = parse()
ranges = {'R': (range(max_y + 1), [0]),
          'L': (range(max_y + 1), [max_x]),
          'D': ([0], range(max_x + 1)),
          'U': ([max_y], range(max_x + 1))}
print(max(energized([((y, x), d) for d in rules[direction][area[(y, x)]]], area)
          for direction in rules
          for y in ranges[direction][0]
          for x in ranges[direction][1]))
