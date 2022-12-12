data = open('AOC_2022\Day-10-Cathode-Ray-Tube\input.txt').read().strip()
lines = [x for x in data.split('\n')]

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
