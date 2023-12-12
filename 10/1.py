from common import parse, find_loop

print(max(find_loop(*parse())[0].values()))
