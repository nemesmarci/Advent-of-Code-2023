from collections import Counter
from common import parse

cards = Counter()
with open('input.txt') as data:
    for line in map(str.strip, data):
        card, winning, numbers = parse(line)
        cards[card] += 1
        for new_card in range(card + 1, card + len(winning & numbers) + 1):
            cards[new_card] += cards[card]
print(sum(cards.values()))
