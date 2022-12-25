import re
def all_numbers(s): return [int(d) for d in re.findall("(-?\d+)", s)]
def md(p, q): return abs(p[0]-q[0])+abs(p[1]-q[1])


data_ = open(
    r'C:\\Users\\shank\\Desktop\\Advent-of-Code\\AOC_2022\\Day-15-Beacon-Exclusion-Zone\\input.txt').read().strip()

data = [all_numbers(line) for line in data_.split("\n")]
radius = {(a, b): md((a, b), (c, d)) for (a, b, c, d) in data}
scanners = radius.keys()

acoeffs, bcoeffs = set(), set()

for ((x, y), r) in radius.items():
    # gradient is 1
    acoeffs.add(y-x+r+1)
    acoeffs.add(y-x-r-1)

    # gradient is -1
    bcoeffs.add(x+y+r+1)
    bcoeffs.add(x+y-r-1)

bound = 4_000_000
for a in acoeffs:
    for b in bcoeffs:
        p = ((b-a)//2, (a+b)//2)
        if all(0 < c < bound for c in p):
            if all(md(p, t) > radius[t] for t in scanners):
                print(4_000_000*p[0]+p[1])