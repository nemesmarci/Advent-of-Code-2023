from common import parse

with open('input.txt') as data:
    print(sum(int(2 ** (len(set.intersection(*parse(line)[1:])) - 1))
              for line in data))
