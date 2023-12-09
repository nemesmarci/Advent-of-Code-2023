from common import parse, predict

print(sum(sum(predict(sequence, -1)) for sequence in parse()))
