def parse(data):
    seeds, *maps = ''.join(data.readlines()).split('\n\n')
    return ([int(seed) for seed in seeds.split(':')[1].split()],
            [[(range(int(source), int(source) + int(length)),
               range(int(dest), int(dest) + int(length)))
              for dest, source, length
              in map(str.split, filter(bool, m.split('\n')[1:]))]
             for m in maps])
