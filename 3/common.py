import re
from collections import defaultdict


def parse():
    schematic = defaultdict(lambda: '.')
    parts = dict()
    with open('input.txt') as data:
        for y, line in enumerate(map(str.strip, data)):
            parsed_number = False
            for x, c in enumerate(line):
                schematic[(y, x)] = line[x]
                if c.isnumeric():
                    if not parsed_number and (parsed_number := True):
                        parts[(y, x)] = int(
                            re.match(r'(\d+).*', line[x:]).group(1))
                else:
                    parsed_number = False
    return schematic, parts
