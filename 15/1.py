from common import parse, lens_hash

print(sum(lens_hash(string) for string in parse()))
