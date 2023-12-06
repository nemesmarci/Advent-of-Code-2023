def win(t, time, record):
    return t * (time - t) > record


def wins(time, record):
    return sum(1 for t in range(time + 1) if win(t, time, record))
