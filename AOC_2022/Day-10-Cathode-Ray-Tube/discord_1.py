res = 0
screen = ""
X = 1
cycles = 0

data = open('AOC_2022\Day-10-Cathode-Ray-Tube\input.txt').read().strip()
lines = [x for x in data.split('\n')]


def tick():
    global cycles, res, screen
    cycles += 1
    if cycles % 40 == 20:
        res += X * cycles

    if cycles % 40 == 0:
        screen += "\n"
    else:
        screen += " █"[X <= cycles % 40 < X+3]


for line in lines:
    if line == "noop":
        tick()
    elif line.startswith("addx"):
        tick()
        tick()
        X += int(line[4:])

print("Part 1:", res)
print("Part 2:")
print(screen)
