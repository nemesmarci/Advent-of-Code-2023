from collections import defaultdict


class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2
        self.supporting = set()
        self.supported_by = set()


def drop():
    falling_bricks = []
    with open('input.txt') as data:
        for line in data:
            c1, c2 = line.strip().split('~')
            x1, y1, z1 = map(int, c1.split(','))
            x2, y2, z2 = map(int, c2.split(','))
            falling_bricks.append((x1, y1, z1, x2, y2, z2))
    bricks = {}
    tops = defaultdict(set)
    for b, (x1, y1, z1, x2, y2, z2) in enumerate(sorted(falling_bricks, key=lambda x: x[2])):
        assert z1 <= z2 and y1 <= y2 and x1 <= x2
        while z1 > 1 and not any(any(bricks[o].y1 <= y <= bricks[o].y2 for y in range(y1, y2 + 1)) and
                                 any(bricks[o].x1 <= x <= bricks[o].x2 for x in range(x1, x2 + 1))
                                 for o in tops[z1 - 1]):
            z1 -= 1
            z2 -= 1
        bricks[b] = Brick(x1, y1, z1, x2, y2, z2)
        tops[z2].add(b)
        for s in (o for o in tops[z1 - 1]
                  if any(bricks[o].y1 <= y <= bricks[o].y2 for y in range(bricks[b].y1, bricks[b].y2 + 1)) and
                  any(bricks[o].x1 <= x <= bricks[o].x2 for x in range(bricks[b].x1, bricks[b].x2 + 1))):
            bricks[s].supporting.add(b)
            bricks[b].supported_by.add(s)
    return bricks
