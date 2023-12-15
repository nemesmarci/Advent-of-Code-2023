from common import parse, lens_hash

boxes = [dict() for _ in range(256)]

for string in parse():
    if '=' in string:
        label, focal = string.split('=')
        box = lens_hash(label)
        boxes[box][label] = int(focal)
    elif '-' in string:
        label = string.rstrip('-')
        box = lens_hash(label)
        boxes[box].pop(label, None)

print(sum((i + 1) * (j + 1) * focal
          for i, box in enumerate(boxes)
          for j, focal in enumerate(box.values())))

