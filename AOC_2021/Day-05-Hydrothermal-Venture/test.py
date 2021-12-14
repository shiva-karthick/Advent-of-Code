from collections import Counter
from dataclasses import dataclass
from math import gcd
from sys import argv


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_horizontal_or_vertical(self) -> bool:
        return self.x1 == self.x2 or self.y1 == self.y2

    def points(self):
        # Overkill, but this will work for lines which aren't horizontal, vertical or 45 deg diagonals
        dy = self.y2 - self.y1
        dx = self.x2 - self.x1
        d = gcd(dy, dx)
        dy //= d
        dx //= d

        return set((self.x1 + i * dx, self.y1 + i * dy) for i in range(d + 1))


with open(r"input copy.txt") as f:
    # For each row in input, replace with a list containing the four integers
    data = map(lambda row: map(int, row.replace(
        ' -> ', ',').split(',')), f.readlines())
    lines = [Line(*tuple(x)) for x in data]

positions = Counter()
print(lines)
for line in lines:
    if line.is_horizontal_or_vertical():  # Uncomment for PART 1
        positions.update(line.points())

print(positions)
count = 0
for v in positions.values():
    if v > 1:
        count += 1

# print(count)
