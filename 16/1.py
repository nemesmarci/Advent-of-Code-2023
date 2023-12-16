from common import parse, energized

area = parse()[0]
match area[(0, 0)]:
    case '/': d = 'U'
    case '|' | '\\': d = 'D'
    case _: d = 'R'

print(energized([((0, 0), d)], area))
