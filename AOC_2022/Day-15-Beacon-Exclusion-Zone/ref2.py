from itertools import product
import re
fh = open(r'C:\\Users\\shank\\Desktop\\Advent-of-Code\\AOC_2022\\Day-15-Beacon-Exclusion-Zone\\input.txt')

lines = {}
for line in fh:
    sx, sy, bx, by = map(int, re.findall('-?\d+', line))
    d = abs(bx - sx) + abs(by - sy) + 1

    for endpoints, mb, norm in [
        ((sx - d, sx), (-1, sy - d + sx), -1),
        ((sx, sx + d), (1, sy - d - sx), -1),
        ((sx, sx + d), (-1, sy + d + sx),  1),
        ((sx - d, sx), (1, sy + d - sx),  1),
    ]:
        lines.setdefault(mb, {-1: [], 1: []})[norm].append(endpoints)

slopes = {-1: [], 1: []}
for (m, b), norms in lines.items():
    for (x1, x2), (x3, x4) in product(*norms.values()):
        o1, o2 = max(x1, x3), min(x2, x4)
        if o1 <= o2:
            slopes[m].append((b, (o1, o2)))

for (b1, (x1, x2)), (b2, (x3, x4)) in product(slopes[-1], slopes[1]):
    x = (b2 - b1) // -2
    y = x + b2
    if x1 <= x <= x2 and x3 <= x <= x4:
        print(x * 4000000 + y)
