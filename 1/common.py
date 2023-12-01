def get_digit(c):
    try:
        return str(int(c))
    except ValueError:
        return None


def calibration(line):
    digits = [d for c in line if (d := get_digit(c))]
    return int(digits[0] + digits[-1])
