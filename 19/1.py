from common import parse, rule_regex


workflows, parts = parse()
xmas = 0
for part in parts:
    step = 'in'
    while True:
        if step == 'A':
            xmas += sum(part.values())
            break
        elif step == 'R':
            break
        for rule in workflows[step]:
            match rule_regex.match(rule).groups():
                case field, '<', value, step:
                    if part[field] < int(value):
                        break
                case field, '>', value, step:
                    if part[field] > int(value):
                        break
                case step, *_:
                    pass
print(xmas)
