from common import parse, possible_solutions

rows, descriptions = parse()
print(sum(possible_solutions('?'.join([row] * 5), description * 5)
          for row, description in zip(rows, descriptions)))
