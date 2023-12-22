from common import drop

bricks = drop()
safe = 0
for b in bricks:
    if not bricks[b].supporting:
        safe += 1
    elif all(any(s in bricks[o].supporting for o in bricks if o != b) for s in bricks[b].supporting):
        safe += 1
print(safe)
