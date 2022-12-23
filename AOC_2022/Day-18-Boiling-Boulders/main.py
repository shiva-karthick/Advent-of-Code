cubes = set()
for l in open('AOC_2022\\Day-18-Boiling-Boulders\\input.txt'):
    cubes.add(tuple(map(int, l.split(','))))


def sides(x, y, z):
    return {(x+1, y, z), (x-1, y, z),
            (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)}


result_1 = 0
for c in cubes:
    for s in sides(*c):
        if s not in cubes:
            result_1 += 1
print(result_1)

seen = set()
todo = [(-1, -1, -1)]

while todo:
    here = todo.pop()
    todo += [s for s in (sides(*here) - cubes - seen)
             if all(-1 <= c <= 25 for c in s)]
    seen |= {here}

print(sum((s in seen) for c in cubes for s in sides(*c)))
