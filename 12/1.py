from common import parse, possible_solutions

rows, descriptions = parse()
print(sum(possible_solutions(row, description)
          for row, description in zip(rows, descriptions)))
