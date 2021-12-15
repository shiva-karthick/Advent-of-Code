with open('sample.txt') as f:
    nums, folds = f.read().split('\n\n')


nums = {tuple(map(int, line.split(','))) for line in nums.splitlines()}

folds = [
    (axis[-1], int(num))
    for line in folds.splitlines()
    for axis, num in [line.split('=')]
]

for i, (axis, t) in enumerate(folds):
    if axis == 'x':
        nums = set((x, y) if x < t else (t+t-x, y) for (x, y) in nums)
    else:
        print(nums)
        nums = set((x, y) if y < t else (x, t+t-y) for (x, y) in nums)
        print(f'their nums = {nums}')
    if i == 0:
        print(f"Part 1: {len(nums)}\nPart 2:")

for y in range(max(y for _, y in nums)+1):
    for x in range(max(x for x, _ in nums)+1):
        print('.#'[(x, y) in nums], end='')
    print()
