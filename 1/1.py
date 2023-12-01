from common import calibration

sum = 0
with open('input.txt') as data:
    for line in map(str.strip, data):
        sum += calibration(line)
print(sum)
