from math import prod
from common import parse

sum = 0
with open('input.txt') as data:
    for line in data:
        min_cubes = dict(red=0, green=0, blue=0)
        for n, color in map(str.split, parse(line)[1:]):
            if (n := int(n)) > min_cubes[color]:
                min_cubes[color] = n
        sum += prod(min_cubes.values())
print(sum)
