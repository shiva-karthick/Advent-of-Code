def solve(pts, folds, p1=False):
    for axis, t in folds:
        pts = set((x, y) if (x, y)[axis] < t else (
            (t-(x-t), y), (x, t-(y-t)))[axis] for x, y in pts)
        if p1:
            break
    print(len(pts))
    if not p1:
        for y in range(max(y for _, y in pts)+1):
            for x in range(max(x for x, _ in pts)+1):
                print('.#'[(x, y) in pts], end='')
            print()


with open('input.txt') as f:
    a, b = f.read().split('\n\n')
nums = set(tuple(map(int, line.split(','))) for line in a.split('\n'))
folds = []
for line in b.splitlines():
    r, t = line.split('=')
    folds.append((r.endswith('y'), int(t)))

solve(nums, folds, True)
solve(nums, folds, False)
