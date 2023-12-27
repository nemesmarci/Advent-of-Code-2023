def parse():
    area = dict()
    with open('input.txt') as data:
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                if c != '#':
                    area[(y, x)] = c
    return area, y, x


def neighbours(y, x, area):
    return [n for n in ((y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)) if n in area]
