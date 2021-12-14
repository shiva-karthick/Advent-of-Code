
# Part 1
def part1():
    with open(r"input.txt") as reader:
        count = 0
        d = {}
        for line in reader:
            left, right = line.split(" -> ")
            (first, second), (third, fourth) = left.split(","), right.split(",")
            # first = x1
            # second = y1
            # third = x2
            # fourth = y2
            first, second, third, fourth = int(first), int(second), int(third), int(fourth)

            if first == third:
                for i in range(min(second, fourth), max(second, fourth) + 1):
                    d[(first, i)] = d.get((first, i), 0) + 1
            elif second == fourth:
                for i in range(min(first, third), max(first, third) + 1):
                    d[(i, second)] = d.get((i, second), 0) + 1
            else:
                length = abs(third - first)
                # Determine if its Up-Left or Down-Right
                if fourth > second:
                    direction = third > first
                    # if direction is True, the line has a positive gradient
                else:
                    direction = first > third
                    # if direction is False, the line has a negative gradient
                    first = third
                    second = fourth

                if (direction):
                    for i in range(length + 1):
                        d[(first+i, second+i)] = d.get((first+i, second+i), 0) + 1
                else:
                    for i in range(length + 1):
                        d[(first-i, second+i)] = d.get((first-i, second+i), 0) + 1

        for tup in (d):
            if d[tup] >= 2:
                count += 1
        print(count)

part1()

