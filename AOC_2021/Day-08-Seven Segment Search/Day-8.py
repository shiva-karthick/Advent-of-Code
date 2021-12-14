#! /usr/bin/python3

from collections import Counter
def part1():
    lst = []
    result = 0
    with open(r"input.txt") as reader:
        for line in reader:
            _, output = line.split(" | ")
            lst.append(output.split())
    for x in lst:
        for y in x:
            if len(y) in (2, 3, 4, 7):
                result += 1
    print(result)

decode = {42: '0', 17: '1', 34: '2', 39: '3', 30: '4', 37: '5', 41: '6', 25: '7', 49: '8', 45: '9'}
def get_decoded(aoc_input):
    with open('input.txt') as reader:
        for left,right in [line.split('|') for line in reader]:
            counts = Counter(left.replace(' ',''))
            yield ''.join(decode[sum(counts[c] for c in k)] for k in right.split())
print('part2', sum(map(int,get_decoded("input.txt"))))

get_decoded("input.txt")


#
#def part_two():
#    s = 0
#    for x,y in [x.split('|') for x in open("input.txt")]:  # split signal and output
#      l = {len(s): set(s) for s in x.split()}    # get number of segments
#
#      n = ''
#      for o in map(set, y.split()):              # loop over output digits
#        match len(o), len(o&l[4]), len(o&l[2]):  # mask with known digits
#          case 2,_,_: n += '1'
#          case 3,_,_: n += '7'
#          case 4,_,_: n += '4'
#          case 7,_,_: n += '8'
#          case 5,2,_: n += '2'
#          case 5,3,1: n += '5'
#          case 5,3,2: n += '3'
#          case 6,4,_: n += '9'
#          case 6,3,1: n += '6'
#          case 6,3,2: n += '0'
#      s += int(n)
#
#    print(s)
#
#
#def solve_system(signal: list[str]) -> dict[str, str]:
#    length_to_signal = {len(s): [] for s in signal}
#    for segment in signal:
#        length_to_signal[len(segment)].append(set(segment))
#
#    (eight,), (one,), (four,), (seven,) = (
#        length_to_signal[7],
#        length_to_signal[2],
#        length_to_signal[4],
#        length_to_signal[3],
#    )
#
#    a, = (*(seven - one),)
#
#    nine, = [segment for segment in length_to_signal[6] if four < segment
#
#    e, = (*(eight - nine),)
#    g, = (*(eight - four - set((a, e))),)
#
#    zero, = (
#        segment
#        for segment in length_to_signal[6]
#        if not (segment == nine or one & (nine ^ segment))
#    )
#
#    d, = (*(eight ^ zero) - set(e),)
#    b, = (*(four - one - set(d)),)
#
#    six, = (
#        segment
#        for segment in length_to_signal[6]
#        if segment != nine and segment != zero
#    )
#
#    f, = (*(six - set((a, e, g, d, b))),)
#
#    c, = (*(one - set(f)),)
#
#    return {a: "a", b: "b", c: "c", d: "d", e: "e", f: "f", g: "g"}
