def parse(line):
    return line.replace(':', ',').replace(';', ',').split(', ')
