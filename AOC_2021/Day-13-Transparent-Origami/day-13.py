
filename = "input.txt"
# First I make a board

lines = open(filename).read().splitlines()

rules = [list(map(int, line.split(',')))
         for line in lines if line and not line.startswith('fold')]
folds = [line[11:].split('=') for line in lines if line.startswith('fold')]

L, W = zip(*rules)  # L = columns and W = rows, why + 1, cos it's 0 indexed?
board = [[' '] * (max(L)+1) for _ in range(max(W)+1)]
for y, x in rules:
    board[x][y] = '#'

# then I iterate over the folds

for a, f in folds:
    if a == 'y':
        for x, y in [(x, y) for y in range(len(board[0])) for x in range(int(f)+1)]:
            if board[x][y] != '#':
                board[x][y] = board[-(x+1)][y]
        del board[int(f):]

    if a == 'x':
        for x, y in [(x, y) for y in range(int(f), len(board[0])) for x in range(len(board))]:
            if board[x][y] != '#':
                board[x][y] = board[x][-(y+1)]
        for i, row in enumerate(board):
            board[i] = board[i][int(f)+1:]

for row in board:
    print(' '.join(row[::-1]))
