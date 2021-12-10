from collections import defaultdict

class Board:
    def __init__(self, grid):
        self.grid = grid
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.size = len(grid)
        self.unmarked = sum(map(sum, self.grid))

    def add(self, value):
        for i, row in enumerate(self.grid):
            for j, x in enumerate(row):
                if value == x:
                    self.rows[i] += 1
                    self.cols[j] += 1
                    self.unmarked -= value

    def check_win(self):
        return any(v == self.size for v in (list(self.rows.values()) + list(self.cols.values())))


with open('input.txt') as f:
    draw = list(map(int, f.readline().strip().split(',')))
    data = [list(map(int, line.strip().split())) for line in f if line.strip()]

print(data)

def part1():
    parts = [Board(data[i:i+5]) for i in range(0, len(data), 5)]
    for val in draw:
        for board in parts:
            board.add(val)
            if board.check_win():
                print('Part 1:', board.unmarked * val)
                return

part1()


def part2():
    parts = [Board(data[i:i+5]) for i in range(0, len(data), 5)]
    answer = None
    for val in draw:
        new_parts = []
        for board in parts:
            board.add(val)
            if board.check_win():
                answer = board.unmarked * val
            else:
                new_parts.append(board)
        parts = new_parts

    print("Part 2:", answer)

part2()
