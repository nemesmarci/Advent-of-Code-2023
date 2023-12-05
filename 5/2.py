from common import parse


def intersection(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop))


def sort_by_src(r):
    return sorted(r, key=lambda x: x[0].start)


def transform_ranges(ranges, rules):
    new_ranges = []
    rules = sort_by_src(rules)
    for r in ranges:
        if r.start >= rules[-1][0].stop:
            new_ranges.append(r)
            continue
        first = next(i for i, rule in enumerate(rules) if r.start in rule[0])
        for i in range(first, len(rules)):
            start_offset = max(r.start, rules[i][0].start) - rules[i][0].start
            if r.stop in rules[i][0]:
                end_offset = r.stop - rules[i][0].start
                new_ranges.append(range(rules[i][1].start + start_offset,
                                        rules[i][1].start + end_offset))
                break
            else:
                new_ranges.append(range(rules[i][1].start + start_offset,
                                        rules[i][1].stop))
    return [r for r in new_ranges if r]


with open('input.txt') as data:
    seeds, map_ranges = parse(data)


for rr in map_ranges:
    source_ranges = [x[0] for x in sort_by_src(rr)]
    prev_stop = 0
    for r in source_ranges:
        if prev_stop != r.start:
            rr.append([range(prev_stop, r.start), range(prev_stop, r.start)])
        prev_stop = r.stop

target_ranges = [range(start, start + r)
                 for start, r in zip(seeds[0::2], seeds[1::2])]
for m in map_ranges:
    target_ranges = transform_ranges(target_ranges, m)

print(min(r.start for r in target_ranges))
