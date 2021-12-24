filename = 'AOC_2021\Day-19\sample.txt'

scanners = [[eval(line) for line in scanner.splitlines() if '--' not in line]
            for scanner in open(filename).read().split('\n\n')]

'''
for every point in the first scanner assume it is 0,0,0 and orient it's group
    for every rotation
       for every point in the next scanner assume it is 0,0,0 and orient it's group
           check to see if they have 12+ in common, if they do save this rotation
    rotate all the points using this rotation, add them all to scanner 0
    go to next scanner
'''

'''
a,b are scanners
try all permutations with b
if there's a match:
  ori = orientation from b to a
  off = offset from b to a
  a_loc = location of a from origin
  b_loc = orient(off, ori) + a_loc

all_beacons = first scanner
while some scanners are left:
  for each scanner:
    if match(all_beacons, scanner):
      transform and add all scanner points to all_beacons
      break
'''

# I think a way of seeing the 24 is like: the "directions" UP, DOWN, LEFT, RIGHT, FRONT, BACK (6) * (4) rotations 0, 90, 180, 270 degrees within each direction


def orient(pt, orientation):
    a, b, c = pt
    return (
        (+a, +b, +c), (+b, +c, +a), (+c, +a, +
                                     b), (+c, +b, -a), (+b, +a, -c), (+a, +c, -b),
        (+a, -b, -c), (+b, -c, -a), (+c, -a, -
                                     b), (+c, -b, +a), (+b, -a, +c), (+a, -c, +b),
        (-a, +b, -c), (-b, +c, -a), (-c, +a, -
                                     b), (-c, +b, +a), (-b, +a, +c), (-a, +c, +b),
        (-a, -b, +c), (-b, -c, +a), (-c, -a, +
                                     b), (-c, -b, -a), (-b, -a, -c), (-a, -c, -b)
    )[orientation]


perms = [lambda a, b, c: (a, b, c),
         lambda a, b, c: (b, c, a),
         lambda a, b, c: (c, a, b),
         lambda a, b, c: (-a, -b, c),
         lambda a, b, c: (-b, -c, a),
         lambda a, b, c: (-c, -a, b),
         lambda a, b, c: (-a, b, -c),
         lambda a, b, c: (-b, c, -a),
         lambda a, b, c: (-c, a, -b),
         lambda a, b, c: (a, -b, -c),
         lambda a, b, c: (b, -c, -a),
         lambda a, b, c: (c, -a, -b),


         lambda a, b, c: (-a, -c, -b),
         lambda a, b, c: (-c, -b, -a),
         lambda a, b, c: (-b, -a, -c),
         lambda a, b, c: (a, c, -b),
         lambda a, b, c: (c, b, -a),
         lambda a, b, c: (b, a, -c),
         lambda a, b, c: (a, -c, b),
         lambda a, b, c: (c, -b, a),
         lambda a, b, c: (b, -a, c),
         lambda a, b, c: (-a, c, b),
         lambda a, b, c: (-c, b, a),
         lambda a, b, c: (-b, a, c)]

print(scanners)
