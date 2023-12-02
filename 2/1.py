from common import parse

limit = dict(red=12, green=13, blue=14)
sum = 0
with open('input.txt') as data:
    for line in data:
        game_id, *cubes = parse(line)
        if all(int(n) <= limit[color] for n, color in map(str.split, cubes)):
            sum += int(game_id.split()[1])
print(sum)
