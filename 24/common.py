def parse():
    hails = []
    with open('input.txt') as data:
        for line in map(str.strip, data):
            pos, vel = line.split(' @ ')
            pos = [int(p) for p in pos.split(', ')]
            vel = [int(v) for v in vel.split(', ')]
            hails.append((pos, vel))
    return hails
