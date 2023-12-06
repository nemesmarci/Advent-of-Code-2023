from common import wins

with open('input.txt') as data:
    times, distances = map(str.split, data.readlines())
time = int(''.join(map(str, times[1:])))
print(wins(int(''.join(map(str, times[1:]))),
           int(''.join(map(str, distances[1:])))))
