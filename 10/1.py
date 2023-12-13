from common import parse, find_loop

print(len(find_loop(*parse()[:2])) // 2)
