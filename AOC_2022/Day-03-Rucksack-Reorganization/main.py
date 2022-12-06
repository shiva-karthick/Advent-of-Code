with open('AOC_2022\Day-03-Rucksack-Reorganization\input.txt') as f:
    text = f.read().strip()
    lines = text.split('\n')


def part1():
    score = 0
    for line in lines:
        a = line[:len(line)//2]
        b = line[len(line)//2:]

        x = set(a) & set(b)  # Find the common letter between the 2 sentences
        y = list(x)[0]  # Extract the common character
        if y.isupper():
            score += ord(y) - ord('A') + 27
        else:
            score += ord(y) - ord('a') + 1
    print(score)


def part2():
    score = 0
    for i in range(0, len(lines), 3):
        x = set(lines[i]) & set(lines[i+2]) & set(lines[i+1])
        y = list(x)[0]
        if y.isupper():
            score += ord(y) - ord('A') + 27
        else:
            score += ord(y) - ord('a') + 1
    print(score)


print("Part 1:", part1())
print("Part 2:", part2())

# def part_1(self) -> str | int | None:
#     """Calculate the answer for part 1."""
#     total = 0
#     for line in self.lines:
#         a = line[0:len(line)//2]
#         b = line[len(line)//2:]
#         inter = (set(a) & set(b)).pop()
#         if 'a' <= inter <= 'z':
#             total += ord(inter) - ord('a') + 1
#         elif 'A' <= inter <= 'Z':
#             total += ord(inter) - ord('A') + 27
#     return total


# def part_2(self) -> str | int | None:
#     """Calculate the answer for part 2."""
#     total = 0
#     for a, b, c in [self.lines[i:i+3] for i in range(0, len(self.lines), 3)]:
#         inter = (set(a) & set(b) & set(c)).pop()
#         if 'a' <= inter <= 'z':
#             total += ord(inter) - ord('a') + 1
#         elif 'A' <= inter <= 'Z':
#             total += ord(inter) - ord('A') + 27
#     return total
