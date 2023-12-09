from common import parse, predict

values = 0
for sequence in parse():
    n = 0
    for x in predict(sequence, 0)[::-1]:
        n = x - n
    values += n
print(values)
