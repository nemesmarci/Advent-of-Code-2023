from math import lcm
from common import parse, steps

instructions, nodes = parse()
starting = [node for node in nodes if node[-1] == 'A']
print(lcm(*(steps(node, lambda x: x[-1] == 'Z', instructions, nodes)
            for node in starting)))
