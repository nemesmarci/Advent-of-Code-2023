from collections import deque
from math import prod
from common import parse, rule_regex

workflows = parse()[0]
queue = deque([('in', [])])
accepted = []
while queue:
    step, conditions = queue.popleft()
    if step == 'A':
        accepted.append(conditions)
        continue
    if step == 'R':
        continue
    for i, rule in enumerate(workflows[step]):
        if failed := workflows[step][:i]:
            for f in failed:
                match rule_regex.match(f).groups():
                    case field, '<', value, _:
                        value = int(value)
                        conditions.append(f'{field}>{value - 1}')
                    case field, '>', value, _:
                        value = int(value)
                        conditions.append(f'{field}<{value + 1}')
        match rule_regex.match(rule).groups():
            case field, ('<' | '>') as op, value, str(next_step):
                queue.append((next_step, conditions + [f'{field}{op}{value}']))
            case next_step, *_:
                queue.append((next_step, conditions))

xmas = 0
for rules in accepted:
    bounds = {b: range(1, 4001) for b in 'xmas'}
    for rule in rules:
        match rule_regex.match(rule).groups():
            case field, '<', value, _:
                bounds[field] = range(bounds[field].start, min(int(value), bounds[field].stop))
            case field, '>', value, _:
                bounds[field] = range(max(int(value) + 1, bounds[field].start), bounds[field].stop)
    xmas += prod(len(b) for b in bounds.values())
print(xmas)
