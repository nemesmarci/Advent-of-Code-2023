def parse():
    with open('input.txt') as data:
        return data.readline().strip().split(',')


def lens_hash(string):
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value %= 256
    return value
