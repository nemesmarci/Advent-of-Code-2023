from common import parse, area


def parse_line(line):
    c = line.strip().split()[2]
    return 'RDLU'[int(c[-2])], int(c[2:-2], 16)


print(area(*parse(parse_line)))
