from collections import defaultdict


def parse():
    rows = []
    descriptions = []
    with open('input.txt') as data:
        for line in data:
            t, d = line.strip().split()
            rows.append(t)
            descriptions.append(list(map(int, d.split(','))))
    return rows, descriptions


def possible_solutions(partial, d):
    """https://www.sciencedirect.com/science/article/pii/S0166218X14000080#s000025"""
    sol = defaultdict(lambda: -1)

    def canPlaceBlock(i, j):
        for m in range(i, i - d[j - 1], -1):
            if partial[m - 1] == '.':
                return False
        if (j > 1) and partial[i - d[j - 1] - 1] == '#':
            return False
        return True

    def solve(i, j):
        if i < 0 or j < 0:
            return 0
        elif i == j == 0:
            return 1
        if sol[(i, j)] != -1:
            return sol[(i, j)]
        else:
            sol[(i, j)] = 0
            if solve(i - 1, j) > 0 and partial[i - 1] != '#':
                sol[(i, j)] = sol[(i,j)] + solve(i - 1, j)
            if solve(i - d[j - 1] - (j > 1), j - 1) > 0 and canPlaceBlock(i, j):
                sol[(i, j)] = sol[(i, j)] + solve(i - d[j - 1] - (j > 1), j - 1)
        return sol[(i, j)]

    return solve(len(partial), len(d))
