def parse():
    patterns = []
    with open('input.txt') as data:
        lines = data.readlines()
    blocks = ''.join(lines).split('\n\n')
    patterns = [[line for line in block.split('\n') if line] for block in blocks]
    return patterns


def get_col(x, pattern):
    return [pattern[y][x] for y in range(len(pattern))]


def is_mirrored(side_a, side_b, smudge=False):
    return sum(a[i] != b[i] for a, b in zip(side_a, side_b) for i in range(len(a))) - smudge < 1


def find_vertical_mirror(pattern, skip=None, smudge=False):
    for col in range(1, len(pattern[0])):
        if skip != col:
            left = ([pattern[y][x] for y in range(len(pattern))] for x in range(col - 1, 0 - 1, -1))
            right = (get_col(x, pattern) for x in range(col, len(pattern[0])))
            if left and right and is_mirrored(left, right, smudge):
                return col


def find_horizontal_mirror(pattern, skip=None, smudge=False):
    for row in range(1, len(pattern)):
        if skip != row:
            up = (pattern[y] for y in range(row - 1, 0 - 1, -1))
            down = (pattern[y] for y in range(row, len(pattern)))
            if up and down and is_mirrored(up, down, smudge):
                return row


def find_mirrors(patterns, old_vertical_mirrors=None,
                 old_horizontal_mirrors=None, smudge=False):
    vertical_mirrors = {}
    horizontal_mirrors = {}
    for n, pattern in enumerate(patterns):
        skip_vertical = old_vertical_mirrors and old_vertical_mirrors.get(n)
        skip_horizontal = old_horizontal_mirrors and old_horizontal_mirrors.get(n)
        if vertical_mirror := find_vertical_mirror(pattern, skip_vertical, smudge):
            vertical_mirrors[n] = vertical_mirror
        elif horizontal_mirror := find_horizontal_mirror(pattern, skip_horizontal, smudge):
            horizontal_mirrors[n] = horizontal_mirror
    return vertical_mirrors, horizontal_mirrors


def value(vertical_mirrors, horizontal_mirrors):
    return sum(vertical_mirrors.values()) + sum(100 * v for v in horizontal_mirrors.values())
