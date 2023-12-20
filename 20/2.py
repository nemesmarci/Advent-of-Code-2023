from collections import deque
from math import lcm
from itertools import count
from common import parse, add_inputs, Conjunction


def rx(modules):
    inputs = {ii: None for i in modules['rx'].inputs for ii in modules[i].inputs}
    for i in count(1):
        queue = deque([('broadcaster', 'button', False)])
        while queue:
            c, m, s = queue.popleft()
            if c in inputs and not s:
                inputs[c] = i
            if all(inputs.values()):
                return lcm(*(inputs.values()))
            if c in modules:
                for o, s in modules[c].signals(s, m):
                    queue.append((o, c, s))


modules = parse()
modules['rx'] = Conjunction([])
add_inputs(modules)
print(rx(modules))
