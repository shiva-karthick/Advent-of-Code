from common import *

with open('AOC_2021\Day-24-Arithmetic-Logic-Unit\input.txt') as f:
    blocks = [x.strip().split('\n') for x in f.read().strip().split('inp')[1:]]

digits = []
for block in blocks:
    up = block[4].endswith('1')  # div z 1 is either 1 or 26
    sub = int(block[5].split(' ')[-1])  # some numbers are negative
    val = int(block[-3].split()[-1])  # some arbitrary positive integers
    digits.append((up, sub, val))

# Recursion approach


def solve(vars, inc, res=0):
    # Base Case
    if len(vars) == 0 and res == 0:
        return ''
    up, sub, val = vars[0]
    if up:
        for i in list(range(1, 10))[::inc]:  # 9, 8, 7, 6, 5, 4, 3, 2, 1
            if (rest := solve(vars[1:], inc, val + i + 26*res)) is not None:
                # print(rest)
                return str(i) + rest
    else:
        if not 1 <= (digit := (res % 26) + sub) <= 9:
            # print((digit := (res % 26) + sub))
            return None
        if (rest := solve(vars[1:], inc, res // 26)) is not None:
            # print((rest := solve(vars[1:], inc, res // 26)))
            return str(digit) + rest
    return None


print("Part 1:", solve(digits, -1))
print("Part 2:", solve(digits, 1))
