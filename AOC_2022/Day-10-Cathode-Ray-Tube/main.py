data = open('AOC_2022\Day-10-Cathode-Ray-Tube\input.txt').read().strip()
lines = [x for x in data.split('\n')]
test_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

X = 1
ticker = 0
result = 0
grid = [["?" for _ in range(40)] for _ in range(6)]


def tick(tick_value: int, X: int):
    global result
    global grid

    if tick_value in [x for x in range(20, 260, 40)]:
        result += (X * tick_value)

    column = (tick_value - 1) % 40  # get the column number
    row = (tick_value - 1) // 40

    if column == X:  # X
        grid[row][column] = ("█")
    elif column == X - 1:  # X - 1
        grid[row][column] = ("█")
    elif column == X + 1:  # X + 1
        grid[row][column] = ("█")
    else:
        grid[row][column] = (" ")
    # X AND COLUMN ARE BOTH 0-INDEXED
    # grid[row][column] = ('█' if abs(X - column) <= 1 else ' ')


for line in lines:
    word = line.split()
    if word[0] == 'noop':
        ticker += 1
        tick(ticker, X)
    elif word[0] == 'addx':
        ticker += 1
        tick(ticker, X)
        ticker += 1
        tick(ticker, X)
        X += int(word[1])  # add after 2 complete cycles

print(result)

for r in range(6):
    print(''.join(grid[r]))
