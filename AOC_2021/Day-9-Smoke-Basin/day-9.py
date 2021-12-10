#! /usr/bin/python3

# with open("input.txt") as reader:
#     lst = []
#     for line in reader:
#         data = line.split("\n")[0]
#         lst.append(list(map(int, data)))


def part1(data):
    c = 0
    for i in range(len(data)):
        line = data[i]
        for j in range(len(line)):
            n = int(line[j])
            if i - 1 >= 0:
                if n >= int(data[i-1][j]):
                    continue
            if i + 1 < len(data):
                if int(data[i+1][j]) <= n:
                    continue
            if j + 1 < len(line):
                if int(data[i][j+1]) <= n:
                    continue
            if j - 1 >= 0:
                if int(data[i][j-1]) <= n:
                    continue
            c += n + 1
    return c

# BFS (Breadth first search)a


def part2_bfs():
    ans = 0
    arr = []
    for line in open("aoc\Day-9-Smoke-Basin\input.txt").readlines():
        tmp = []
        for value in line:
            if value != '\n':
                tmp.append(int(value))
            else:
                arr.append(tmp)
    arr.append(tmp)
    low_points = []
    visited = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]

    for x, row in enumerate(arr):
        for y, val in enumerate(row):
            queue = [[x, y]]
            size = 0
            while len(queue):
                i, j = queue.pop(0)

                if not visited[i][j]:
                    visited[i][j] = 1
                    if arr[i][j] != 9:
                        size += 1
                        # Find all possible neighbours
                        all_candidates = [
                            [i-1, j], [i+1, j], [i, j-1], [i, j+1]]
                        for candidate in all_candidates:
                            if 0 <= candidate[0] < len(arr):
                                if 0 <= candidate[1] < len(arr[0]):
                                    queue.append(candidate)
            low_points.append(size)

    low_points.sort(reverse=True)
    ans = 1
    for i in range(3):
        ans *= low_points[i]
    print(ans)


part2_bfs()


# DFS
def dfs(i, j):
    if not (0 <= i < 100 and 0 <= j < 100) or marked[i][j]:
        return 0
    marked[i][j] = True
    if x[i][j] == 9:
        return 0
    return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)


def part2_dfs(x):
    basins = []
    marked = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            if marked[i][j]:
                continue
            basins.append(dfs(i, j))

# print(dfs_part2(data))
