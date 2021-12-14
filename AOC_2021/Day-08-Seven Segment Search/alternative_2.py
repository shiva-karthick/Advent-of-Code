#! /usr/bin/python3

"""
  x       x               x       x
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....
          x       x       x       x
  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 """


class Solver():

    def parse(self):
        with open(r"input.txt") as reader:
            self.samples = []
            self.outputs = []
            for line in reader:
                s, o = line.strip('\n').split(' | ')
                self.samples.append([set(samp) for samp in s.split()])
                self.outputs.append([set(samp) for samp in o.split()])

    def part1(self):
        count = 0
        for out in self.outputs:
            for o in out:
                if len(o) in [2, 4, 3, 7]:
                    count += 1
        return count

    def part2(self):
        # need to deduce which segment set goes to which digit
        full_sum = 0
        for (sample, output) in zip(self.samples, self.outputs):
            digits_per_set = {}
            set_per_digit = {}

            # find 1,4,7,8 because they have the distinct number of digits
            for s in sample:
                if len(s) == 2:
                    print(s)
                    digits_per_set[''.join(sorted(s))] = 1
                    set_per_digit[1] = s
                elif len(s) == 4:
                    digits_per_set[''.join(sorted(s))] = 4
                    set_per_digit[4] = s
                elif len(s) == 3:
                    digits_per_set[''.join(sorted(s))] = 7
                    set_per_digit[7] = s
                elif len(s) == 7:
                    digits_per_set[''.join(sorted(s))] = 8
                    set_per_digit[8] = s

            # find 3.
            for s in sample:
                if len(s ^ set_per_digit[7]) == 2:
                    digits_per_set[''.join(sorted(s))] = 3
                    set_per_digit[3] = s
                    break
            # find 9
            for s in sample:
                if len(s ^ set_per_digit[3]) == 1:
                    digits_per_set[''.join(sorted(s))] = 9
                    set_per_digit[9] = s
                    break
            # find 0
            for s in sample:
                if len(s) == 6:
                    if len(s ^ set_per_digit[7]) == 3 and s not in [set_per_digit[9], set_per_digit[4]]:
                        digits_per_set[''.join(sorted(s))] = 0
                        set_per_digit[0] = s
                        break
            # find 6 and make sure it is not 0 or 9;
            for s in sample:
                if len(s) == 6 and s not in [set_per_digit[9], set_per_digit[0]]:
                    digits_per_set[''.join(sorted(s))] = 6
                    set_per_digit[6] = s
                    break
            # find 5 and 2
            for s in sample:
                if len(set_per_digit[9]-s) == 2 and s not in set_per_digit.values():
                    digits_per_set[''.join(sorted(s))] = 2
                    set_per_digit[2] = s
            for s in sample:
                if len(set_per_digit[9]-s) == 1 and s not in set_per_digit.values():
                    digits_per_set[''.join(sorted(s))] = 5
                    set_per_digit[5] = s
            out = int(
                ''.join([str(digits_per_set[''.join(sorted(s))]) for s in output]))
            full_sum += out

        return full_sum


#s = Solver()
#s.parse()
#print(s.part2())
#

# print(sum(sum(len(p) in [2, 3, 4, 7]for p in x.split()[11:])+1j*int(''.join('4725360918'[
#       sum(map(x[:60].count, r))//2 % 15 % 11]for r in x[60:].split()))for x in open(0)))



# Another alternative solution
#I used sets
#an intersection of 5 and 9 has a length of 4
#an intersection of 1 and 0 has a length of 2 (if you can exclude 9)
#then the only remaining six segment peice is 6
#
#then 1 and 3 has 2
#0 and 5 has len 5
#the only five segment left is two


def decode():
    with open("input.txt") as reader:
        nums = []
        outputs = []
        for line in reader:
            s, o = line.strip("\n").split(" | ")
            for i in s.split():
                nums.append(set(i))
            for j in o.split():
                outputs.append(set(j))

            _0 = []
            _1 = []
            _2 = []
            _3 = []
            _4 = []
            _5 = []
            _6 = []
            _7 = []
            _8 = []
            _9 = []

            # nums: list[str]
            nums = list(map(lambda x : x, sorted(nums, key=len)))

            _1, _7, _4 = nums[0:3]
            _8 = nums[-1]
            for item in filter(lambda x: len(x) == 6, nums):
                # the number of digits with length of 6 is 9 , 0 and 6
                # if _4 intersect item == len(4), it is a number 9
                if len(_4 & item) == 4:
                    _9 = item
                elif len(_1 & item) == 2:
                    _0 = item
                else:
                    _6 = item

            for item in filter(lambda x: len(x) == 5, nums):
                if len(_1 & item) == 2:
                    _3 = item
                elif len(_9 & item) == 5:
                    _5 = item
                else:
                    _2 = item
            return _0, _1, _2, _3, _4, _5, _6, _7, _8, _9

print(decode())
