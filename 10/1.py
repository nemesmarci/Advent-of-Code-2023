from common import parse, find_loop

print(max(find_loop(*parse()[:2])[0].values()))
