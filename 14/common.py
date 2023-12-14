from collections import Counter


def parse():
    with open('input.txt') as data:
        return [list(line.strip()) for line in data]


def get_col(x, area):
    return [area[y][x] for y in range(len(area))]


def move_blocks(line, direction):
    blocks = line.split('#')
    new_blocks = []
    for block in blocks:
        items = Counter(block)
        if direction in ('up', 'left'):
            new_blocks.append(items['O'] * 'O' + items['.'] * '.')
        else:
            new_blocks.append(items['.'] * '.' + items['O'] * 'O')
    return '#'.join(new_blocks)


def move_cols(area, direction):
    for x in range(len(area[0])):
        col = ''.join(get_col(x, area))
        new_col = move_blocks(col, direction)
        for y in range(len(col)):
            area[y][x] = new_col[y]


def weight(area):
    w = 0
    for x in range(len(area[0])):
        col = get_col(x, area)
        for i in range(len(col), 0, -1):
            if col[len(col) - i] == 'O':
                w += i
    return w
