from collections import Counter, defaultdict
from common import parse, winnings

face_mapping = {
    'T': 'B',
    'J': '0',
    'Q': 'D',
    'K': 'E',
    'A': 'F',
}

buckets = defaultdict(list)

with open('input.txt') as data:
    for line in data:
        current = parse(face_mapping, line)
        cards = Counter(current[0])
        jokers = cards.pop('0', 0)
        if not cards:
            buckets['five_of_a_kinds'].append(current)
            continue
        match cards.most_common(1)[0][1]:
            case 1:
                bucket = ('high_cards', 'one_pairs', 'three_of_a_kinds',
                          'four_of_a_kinds', 'five_of_a_kinds')[jokers]
            case 2:
                pairs = len([p for p in cards.values() if p == 2])
                if pairs == 1:
                    bucket = ('one_pairs', 'three_of_a_kinds', 'four_of_a_kinds',
                              'five_of_a_kinds')[jokers]
                else:
                    bucket = ('two_pairs', 'full_houses')[jokers]
            case 3:
                if 2 in cards.values():
                    bucket = 'full_houses'
                else:
                    bucket = ('three_of_a_kinds', 'four_of_a_kinds',
                              'five_of_a_kinds')[jokers]
            case 4:
                bucket = ('four_of_a_kinds', 'five_of_a_kinds')[jokers]
            case 5:
                bucket = 'five_of_a_kinds'
        buckets[bucket].append(current)

print(winnings(buckets))
