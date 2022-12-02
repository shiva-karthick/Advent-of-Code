import re

'''
Thanks to Mustafa ! 

it's not hard even, just tedious
so basically, You have 2 cubes, represented by the min/max vertices
what you need to do is keep track of a list of disjoint cubes representing the entire space
so if I want to add a new cube to the list, and it doesn't overlap with anything, I can just throw it in
but if it overlaps with anything, I need to split up the "remaining area" into disjoint cubes
easier to think in 2d
let me draw it out <look at pictures in the folder>

# Qn 1 : So rather than turning on or off each individual cube,
you'd say that all the cubes in the defined range are on or off and 
you'd see how that would interact with other ranges you've previously changed ? 
Yes exactly

1. you maintain a list of disjoint cuboids
2. if you every get any overlaps because of adding/subtracting
3. you break up the existing cuboids into more disjoint ones


For the overlaps, you'd essentially just be adding extra "off" cubes in the relevant places then?
yes exactly
lets think of it in 1d
lets assume you have (0, 5) ON and you want to do (2, 8) OFF

in the "splitting method", you'd remove the overlapping part and then you'd keep around (0, 1)
in the "overlaps method", you would store +(0,5)   -(2,5)   +(2,8)
and then when computing the volume (or in this case length), you'd need to subtract off all the negative ones too
and the more ranges (cuboids) you are keeping track of, the more of these "negative" ranges you would add
and if you don't clean them up at some point you might just have some cuboids repeatedly turning on and off the same space, just wasting time

TLDR
+ Instead of splitting a cube, I just add another cube which is the size of the intersection
And store a flag to mark it as "negative"
+ So when I'm computing the area, I just subtract that off

explanation.png
> thanks. here's what I don't get: if I make an on cube, and another on cube, then I can have three cubes, the first two positive, and the intersection is negative, so that it doesn't get double counted. good.
> yes, perfect
the only difference between the ON and OFF cases would be
you don't add the second cube to the set
so in this case if BLUE was off, we'd still do the other 2 intersections and stuff the same way
just not add blue in the end
since we've already effectively "cancelled out" all the cells there

'''


def intersect(a, b):
    return (max(a[0], b[0]), min(a[1], b[1]),
            max(a[2], b[2]), min(a[3], b[3]),
            max(a[4], b[4]), min(a[5], b[5]))


def overlaps(a, b):
    return not (a[1] < b[0] or a[0] > b[1] or
                a[3] < b[2] or a[2] > b[3] or
                a[5] < b[4] or a[4] > b[5])


def area(c):
    return (c[1] - c[0] + 1) * (c[3] - c[2] + 1) * (c[5] - c[4] + 1)


with open('AOC_2021\Day-22-Reactor-Reboot\input.txt') as f:
    data = [(line[1] == 'n', [int(x) for x in re.findall('-?\d+', line)])
            for line in f]


def solve(part1):
    cubes = []
    bounds = (-50, 50, -50, 50, -50, 50)
    for OP, a in data:
        if part1 and not overlaps(bounds, a):
            continue
        # cubes += [(intersect(a, b), -w)
        #           for b, w in cubes if overlaps(a, b)] + [(a, 1)] * OP
        tmp_cubes = []
        for b, w in cubes:
            if overlaps(a, b):
                tmp_cubes += [(intersect(a, b), -w)]
        cubes += tmp_cubes + [(a, 1)] * OP
    print(f'cubes = {cubes}')
    return sum(area(c)*w for c, w in cubes)


# print("Part 1:", solve(True))
print("Part 2:", solve(False))
