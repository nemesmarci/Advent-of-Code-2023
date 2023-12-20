from collections import deque
from common import parse, add_inputs, Value

modules = parse()
add_inputs(modules)
low, high = Value(0), Value(0)
for _ in range(1000):
    queue = deque([('broadcaster', 'button', False)])
    while queue:
        c, m, s = queue.popleft()
        (high if s else low).value += 1
        if c in modules:
            for o, s in modules[c].signals(s, m):
                queue.append((o, c, s))

print(low.value * high.value)
