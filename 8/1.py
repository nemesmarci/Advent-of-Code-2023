from common import parse, steps

print(steps('AAA', lambda x: x == 'ZZZ', *parse()))
