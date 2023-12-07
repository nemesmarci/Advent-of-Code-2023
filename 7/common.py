from itertools import chain


def parse(face_mapping, line):
    hand, bet = line.split()
    for k, v in face_mapping.items():
        hand = hand.replace(k, v)
    return hand, int(bet)


def winnings(buckets):
    return sum(((rank + 1) * hand[1]
                for rank, hand in enumerate(chain(sorted(buckets['high_cards']),
                                                  sorted(buckets['one_pairs']),
                                                  sorted(buckets['two_pairs']),
                                                  sorted(buckets['three_of_a_kinds']),
                                                  sorted(buckets['full_houses']),
                                                  sorted(buckets['four_of_a_kinds']),
                                                  sorted(buckets['five_of_a_kinds'])))))
