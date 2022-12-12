grid = [["?" for _ in range(6)] for _ in range(40)]

tick_value = 40
screen = ""
cycles = 41
X = 1

for r in range(6):
    for c in range(40):
        if 1 <= tick_value <= 40:
            row = 0
            column =
        elif 41 <= tick_value <= 80:
            row = 1
        elif 81 <= tick_value <= 120:
            row = 2
        elif 121 <= tick_value <= 160:
            row = 3
        elif 161 <= tick_value <= 200:
            row = 4
        elif 201 <= tick_value <= 240:
            row = 5


if cycles % 40 == 0:
    screen += "\n"  # add a new line. go to the next paragraph
else:
    # if left side of the sprite < cycles % 40 < X + 3
    screen += " #"[X <= cycles % 40 < X+3]

print(screen)
