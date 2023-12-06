from math import prod
from common import wins

with open('input.txt') as data:
    times, distances = map(str.split, data.readlines())
print(prod(wins(time, record) for time, record
           in zip(map(int, times[1:]), map(int, distances[1:]))))
