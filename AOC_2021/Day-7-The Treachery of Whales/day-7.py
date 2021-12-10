#! /usr/bin/python3


with open(r"input.txt") as reader:
    crabs = [int(i) for i in reader.readline().split(",")]

def part1():
    median = sorted(crabs)[len(crabs) // 2]
    return sum(abs(i-median) for i in crabs)

print(min(crabs))
print(max(crabs))

def part2():
    d = {}
    s = 0
    for i in range(min(crabs), max(crabs)):
        s = 0
        for j in crabs:
            s += abs(j - i)
        d[i] = s
    print(min(d[i] for i in d))


    # print({i: sum(abs(n - i) for n in crabs) for i in range(min(crabs), max(crabs) + 1)}.values())

part2()


# part 1
## print(min({i: sum(abs(n - i) for n in crabs) for i in range(min(crabs), max(crabs) + 1)}.values()))
# part 2


# Notes


# Given:
#    triangular(x) = x * (x + 1) / 2
#    i in CRAB_POSITIONS
#    n = len(CRAB_POSITONS)
#
# We need to minimize the following cost function:
#    Cost(x) = Sum_i triangular(|x - i|) =>
#
#    (Absolute values dropped as we approximate (x - i + 1) as (x - i) and the signs cancel.)
#    Sum_i (x - i) * (x - i) / 2  =>
#    Sum_i (x**2 - 2ix + i**2) / 2
#
# To minimize we use gradient descent. Take the derivative with respect to x and set to 0:
#    0 = Sum_i x - i =>  0 = (Sum_i -i) + n * x
#    x * n = Sum_i i  =>
#    x = (Sum_i i) / n
#
# x is approximately the mean of the positions

# Median being the most common works linearly because it's the dead center of all the different values, outliers don't have any difference in travel

# Mean works for part 2 because, in a normal distribution, you should get a bell curve around the mean, and now because distance matters, you want as many crabs as possible to travel as little as possible

