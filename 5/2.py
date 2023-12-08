from common import parse


def transform_ranges(original_ranges, rules):
    new_ranges = []
    for source_range in original_ranges:
        if source_range.start >= rules[-1][0].stop:
            new_ranges.append(source_range)
            continue
        first = next(i for i, rule in enumerate(rules)
                     if source_range.start in rule[0])
        for i in range(first, len(rules)):
            new_start = (rules[i][1].start +
                         max(source_range.start, rules[i][0].start) -
                         rules[i][0].start)
            if source_range.stop in rules[i][0]:
                end_offset = source_range.stop - rules[i][0].start
                new_ranges.append(range(new_start,
                                        rules[i][1].start + end_offset))
                break
            else:
                new_ranges.append(range(new_start, rules[i][1].stop))
    return [r for r in new_ranges if r]


def add_missing_ranges(rules):
    rules.sort(key=lambda x: x[0].start)
    missing_ranges = []
    prev_stop = 0
    for src_range in (rule[0] for rule in rules):
        if prev_stop != src_range.start:
            missing_ranges.append((range(prev_stop, src_range.start),
                                   range(prev_stop, src_range.start)))
        prev_stop = src_range.stop
    rules.extend(missing_ranges)
    rules.sort(key=lambda x: x[0].start)


with open('input.txt') as data:
    seeds, map_ranges = parse(data)
for rules in map_ranges:
    add_missing_ranges(rules)
target_ranges = [range(start, start + length)
                 for start, length in zip(seeds[0::2], seeds[1::2])]
for rules in map_ranges:
    target_ranges = transform_ranges(target_ranges, rules)
print(min(r.start for r in target_ranges))
