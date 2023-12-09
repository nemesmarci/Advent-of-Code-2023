def parse():
    with open('input.txt') as data:
        return [[int(x) for x in line.strip().split()] for line in data]


def predict(sequence, index):
    predictions = []
    while True:
        predictions.append(sequence[index])
        if not all(x == 0 for x in sequence):
            new_sequence = []
            for i in range(1, len(sequence)):
                new_sequence.append(sequence[i] - sequence[i - 1])
            sequence = new_sequence
        else:
            return predictions
