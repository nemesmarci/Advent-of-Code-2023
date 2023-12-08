from itertools import cycle


def parse():
    with open('input.txt') as data:
        lines = data.readlines()
    return (lines[0].strip(),
            {a: (b, c) for a, b, c
             in map(lambda x: x.translate(
                str.maketrans('=', ',', '() \n')).split(','), lines[2:])})


def steps(current, end_condition, instructions, nodes):
    for i, instruction in enumerate(cycle(instructions)):
        if end_condition(current := nodes[current][instruction == 'R']):
            return i + 1
