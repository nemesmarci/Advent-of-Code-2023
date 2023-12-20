import re
from dataclasses import dataclass


def parse():
    module_regex = re.compile(r'([%&])?(\w+) -> (.+)')
    modules = {}
    with open('input.txt') as data:
        for line in map(str.strip, data):
            match module_regex.match(line).groups():
                case _, 'broadcaster', outputs:
                    modules['broadcaster'] = Broadcaster(outputs.split(', '))
                case '%', module, outputs:
                    modules[module] = FlipFlop(outputs.split(', '))
                case '&', module, outputs:
                    modules[module] = Conjunction(outputs.split(', '))
    return modules


def add_inputs(modules):
    for c, m in modules.items():
        if type(m) is Conjunction:
            for o, n, in modules.items():
                if c in n.outputs:
                    m.inputs[o] = False


@dataclass
class Value:
    value: int


class Broadcaster:
    def __init__(self, outputs):
        self.outputs = outputs

    def signals(self, s, _):
        return [(o, s) for o in self.outputs]


class FlipFlop:
    def __init__(self, outputs):
        self.outputs = outputs
        self.state = False

    def signals(self, s, _):
        if s:
            return []
        else:
            self.state = not self.state
        return [(o, self.state) for o in self.outputs]


class Conjunction:
    def __init__(self, outputs):
        self.outputs = outputs
        self.inputs = {}

    def signals(self, s, m):
        self.inputs[m] = s
        v = not all(self.inputs.values())
        return [(o, v) for o in self.outputs]
