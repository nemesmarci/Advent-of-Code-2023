from copy import deepcopy
from dataclasses import dataclass
from common import drop


@dataclass
class Value:
    value: int


def remove(b, bricks, removed):
    removed.value += 1
    for s in bricks[b].supporting:
        bricks[s].supported_by.remove(b)
        if not bricks[s].supported_by:
            remove(s, bricks, removed)


bricks = drop()
total = 0
for b in bricks:
    new_bricks = deepcopy(bricks)
    removed = Value(0)
    remove(b, new_bricks, removed)
    total += removed.value - 1
print(total)
