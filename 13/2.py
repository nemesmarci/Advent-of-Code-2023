from common import parse, find_mirrors, value

print(value(*find_mirrors(patterns := parse(), *find_mirrors(patterns), True)))
