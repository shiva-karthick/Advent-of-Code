from common import *
from math import sqrt

# probe must shoot upwards to get height
# probe goes upwards, dropping 1 from its y velocity each time until it hits its peak at y velocity = 0
# probe then falls down
# each time it drops 1 from its y velocity it has the exact same y values as when it was going up
# probe will fall straight back to exactly y = 0
# at y = 0, probe will have exactly negative initial y velocity
# the fastest probe lands right at the lowest possible negative y in the target zone
# so initial y velocity of the fastest probe must be
# one minus the absolute value of the lowest possible negative y

linux_filename = "sample.txt"
windows_filename = "AOC_2021\Day-17-Trick-Shot\input.txt"

with open(windows_filename) as f:
    text = f.read().strip()

x1, x2, y1, y2 = parse('target area: x={:d}..{:d}, y={:d}..{:d}', text)
# 211 232 -124 -69

max_vy = abs(y1) - 1
min_vy = -max_vy - 1

min_vx = int(sqrt(x1 * 2))
max_vx = x2 + 1

print(f"y1 = {y1}, y2 = {y2} x1 = {x1}, x2 = {x2}")
print(
    f'max_vy = {max_vy}, min_vy = {min_vy}, min_vx = {min_vx}, max_vx = {max_vx}')


def check_vel(vx, vy):
    x, y = 0, 0
    while x <= x2 and y >= y1:
        x, y = x + vx, y + vy
        if vx > 0:
            vx -= 1
        if vx < 0:
            vx += 1

        vy -= 1
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
    return False


count = sum(
    check_vel(vx, vy)
    for vx in range(min_vx, max_vx + 1)
    for vy in range(min_vy, max_vy + 1)
)

print(f"Part 1 : {max_vy * (max_vy + 1) // 2}")
print(f"Part 2 : {count}")
