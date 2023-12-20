import re

rule_regex = re.compile(r'(\w+)([<>]?)(\d*):?(\w*)')


def parse():
    with open('input.txt') as data:
        raw_workflows, raw_parts = ''.join(data.readlines()).split('\n\n')
    workflows = {}
    for workflow in raw_workflows.split('\n'):
        workflow = workflow.replace('}', '')
        name, steps = workflow.split('{')
        workflows[name] = steps.split(',')
    parts = []
    x, m, a, s = 'x', 'm', 'a', 's'
    for part in raw_parts.split('\n'):
        if part:
            parts.append(eval(part.replace('=', ':')))
    return workflows, parts
