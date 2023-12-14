from common import parse, move_cols, weight


area = parse()
move_cols(area, 'up')
print(weight(area))
