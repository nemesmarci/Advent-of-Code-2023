from common import parse, area


def parse_line(line):
    d, l = line.strip().split()[:2]
    return d, int(l)


print(area(*parse(parse_line)))
