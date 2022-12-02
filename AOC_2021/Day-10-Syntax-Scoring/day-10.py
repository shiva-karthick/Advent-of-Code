#! /usr/bin/python3
# DEBUG PRINT
DEBUG_PRINT = True


def dprint(s):
    if DEBUG_PRINT:
        print(s)


with open("input.txt") as reader:
    data = []
    for line in reader:
        data.append(list(line.strip().split()))


def part1():
    maps = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
        "<" : ">",
    }
    ans = 0
    scoring = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137,
    }

    for line in data:
        stack = []
        for character in line[0]:
            if character in maps.keys():
                stack.append(character)
                print(f"{stack}")
            elif character == maps[stack[-1]]:
                stack.pop()
            else:
                # illegal character
                ans += scoring[character]
                break # Stop at the first incorrect closing character on each corrupted line.
    print(ans)


def part2():
    maps = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
        "<" : ">",
    }
    scoring = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4,
    }
    total = []
    for line in data:
        stack = []
        for character in line[0]:
            if character in maps.keys():
                stack.append(character)
            elif character == maps[stack[-1]]:
                stack.pop()
            else:
               break
        else:
            tmp = 0
            for s in stack[::-1]:
                tmp = (tmp * 5) + scoring[maps[s]]
            total.append(tmp)

    total.sort()
    print(total[len(total) // 2])

part2()


