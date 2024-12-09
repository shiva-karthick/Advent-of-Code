a = [[*map(int, r.split())] for r in open("../data/day2-1.txt", "r")]

f = lambda t: sum(
    any(
        (z := [*zip(s := r[:i] + r[i + 1 :], s[1:])])
        * (all(0 < x - y < 4 for x, y in z) + all(0 < y - x < 4 for x, y in z))
        for i in range(len(r) * t, len(r) + 1)
    )
    for r in a
)
print("Part 1:", f(1), "\nPart 2:", f(0))
