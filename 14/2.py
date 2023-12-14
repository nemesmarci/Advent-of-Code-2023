from common import parse, move_cols, move_blocks, weight


def move_rows(area, direction):
    for y in range(len(area)):
        row = ''.join(area[y])
        new_row = move_blocks(row, direction)
        for x in range(len(row)):
            area[y][x] = new_row[x]


def cycle(area):
    move_cols(area, 'up')
    move_rows(area, 'left')
    move_cols(area, 'down')
    move_rows(area, 'right')


area = parse()
seen = dict()
weights = dict()
for i in range(1, 1000000000 + 1):
    cycle(area)
    weights[i] = weight(area)
    state = tuple(tuple(row) for row in area)
    if state in seen:
        offset = seen[state]
        period = i - offset
        print(weights[offset + (1000000000 - offset) % period])
        break
    seen[state] = i
