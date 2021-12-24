from collections import defaultdict

with open('AOC_2021\Day-20-Trench-Map\input.txt') as f:
    data = f.read().split('\n\n')
    algo = [ch == '#' for ch in data[0]]
    image = data[1].splitlines()

# Functions


def on():
    return True


off = bool

pixels = defaultdict(off)  # True/False values, True indicating light pixel

# x is horizontal increasing to right, y is vertical increasing downwards
# x corresponds to j, y corresponds to i
xmin, ymin, xmax, ymax = 0, 0, len(image[0]), len(image)

for i, row in enumerate(image):
    for j, pixel in enumerate(row):
        pixels[(i, j)] = pixel == '#'


def convert(pixels, i, j) -> bool:
    num = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            # What exactly does this line ?
            num = num * 2 + int(pixels[(i + dy, j + dx)])
    return algo[num]


def print_pixels():
    """For debugging only!"""
    for i in range(ymin, ymax):
        for j in range(xmin, xmax):
            print('#' if pixels[(i, j)] else '.', end='')
        print()


print_pixels()
for iteration in range(2):
    xmin -= 1
    ymin -= 1
    xmax += 1
    ymax += 1

    # ONLY WORKS FOR ACTUAL INPUT
    new_pixels = defaultdict(off if iteration % 2 else on)
    # new_pixels = defaultdict(off) ### ONLY FOR SAMPLE INPUT
    for j in range(xmin, xmax):
        for i in range(ymin, ymax):
            new_pixels[(i, j)] = convert(pixels, i, j)

    pixels = new_pixels

    print_pixels()

print(sum(pixels.values()))
