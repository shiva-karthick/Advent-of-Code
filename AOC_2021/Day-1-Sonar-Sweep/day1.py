class Solution():
    def __init__(self):
        self.previous = 0
        self.count = 0

    def part1(self):
        with open(r"input.txt", "r") as reader:
            self.previous = int(reader.readline())
            for line in reader:
                if int(line) > self.previous:
                    self.count += 1
                    self.previous = int(line)
                else:
                    self.previous = int(line)
        print(self.count)

    def part2(self):
        self.lst = []
        self.previous = 0

        with open(r"input.txt", "r") as reader:
            for line in reader:
                self.lst.append(int(line.strip()))

        for index in range(len(self.lst) - 2):
            if (self.lst[index] + self.lst[index + 1] + self.lst[index + 2]) > self.previous:
                self.count += 1
            self.previous = self.lst[index] + \
                self.lst[index + 1] + self.lst[index + 2]

        print(self.count - 1)


solution = Solution()
solution.part2()

# 2nd solution

with open(r'input.txt') as f:
    # list comprehension
    items = [int(line.strip()) for line in f]


def qn1():
    increased = 0
    for i in range(1, len(items)):
        if items[i - 1] < items[i]:
            increased += 1
    return increased


def qn2():
    increased_sums = 0
    for i in range(3, len(items)):
        if items[i] > items[i - 3]:
            increased_sums += 1
    return increased_sums


print(f"Part 1: {qn1()}")
print(f"Part 2: {qn2()}")
