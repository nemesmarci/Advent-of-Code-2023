from common import parse, find_mirrors, value

print(value(*find_mirrors(parse())))
