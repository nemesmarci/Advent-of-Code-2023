from common import get_digit, calibration

DIGITS = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
}


def replace_first(line):
    min_index = next((i for i, c in enumerate(line)
                      if get_digit(c)), len(line))
    first = None
    for num in DIGITS:
        if 0 <= (index := line.find(num)) < min_index:
            first = num
            min_index = index
    return line.replace(first, DIGITS[first], 1) if first else line


def replace_last(line):
    max_index = len(line) - 1 - next((i for i, c in enumerate(line[::-1])
                                      if get_digit(c)), len(line))
    last = None
    for num in DIGITS:
        if (index := line.rfind(num)) > max_index:
            last = num
            max_index = index
    return DIGITS[last].join(line.rsplit(last, 1)) if last else line


sum = 0
with open('input.txt') as data:
    for line in map(str.strip, data):
        sum += calibration(replace_last(replace_first(line)))
print(sum)
