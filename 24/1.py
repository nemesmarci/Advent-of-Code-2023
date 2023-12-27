from common import parse

hails = parse()
min_v, max_v = 200000000000000, 400000000000000
intersections = 0
for i, ((x1, y1, _), (u1, v1, _)) in enumerate(hails):
    for ((x2, y2, _), (u2, v2, _)) in hails[i + 1:]:
        try:
            m1, m2 = v1 / u1, v2 / u2
            b1, b2 = y1 - m1 * x1, y2 - m2 * x2
            y = (b1 * m2 - b2 * m1) / (m2 - m1)
            x = (y - b2) / m2
            if (min_v <= x <= max_v and min_v <= y <= max_v and
                    (u1 < 0 and x < x1 or u1 > 0 and x > x1) and
                    (u2 < 0 and x < x2 or u2 > 0 and x > x2) and
                    (v1 < 0 and y < y1 or v1 > 0 and y > y1) and
                    (v2 < 0 and y < y2 or v2 > 0 and y > y2)):
                intersections += 1
        except ZeroDivisionError:
            pass
print(intersections)
