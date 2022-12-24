from pprint import pprint

data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

dict_ = {}

for line in lines:
    words = line.split()
    name = words[0][:-1]
    expr = line.split(':')[1]
    dict_[name] = expr.split()


def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
        # If string is not a valid `float`,
        # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True


while True:

    if len(dict_.get('root')) == 1:
        print((dict_.get('root')[0]))
        break

    for pointer_name in dict_.keys():
        # substitute numbers
        if len(dict_[pointer_name]) == 1:  # choose a number
            # loop entire dictionary to substitute the chosen number
            for name in dict_.keys():
                if name == pointer_name:
                    continue
                else:
                    if len(dict_[name]) == 3:
                        if dict_[name][0] == pointer_name:
                            dict_[name].pop(0)
                            dict_[name].insert(0, dict_[pointer_name][0])
                        elif dict_[name][2] == pointer_name:
                            dict_[name].pop(2)
                            dict_[name].insert(2, dict_[pointer_name][0])
                        # new if statement
                    if len(dict_[name]) == 3 and is_number(dict_[name][0]) and is_number(dict_[name][2]):
                        if len(dict_[name]) == 3 and dict_[name][1] == "+":
                            dict_[name] = [
                                str(float(dict_[name][0]) + float(dict_[name][2]))]
                        if len(dict_[name]) == 3 and dict_[name][1] == "*":
                            dict_[name] = [
                                str(float(dict_[name][0]) * float(dict_[name][2]))]
                        if len(dict_[name]) == 3 and dict_[name][1] == "/":
                            dict_[name] = [
                                str(float(dict_[name][0]) / float(dict_[name][2]))]

                        if len(dict_[name]) == 3 and dict_[name][1] == "-":
                            dict_[name] = [
                                str(float(dict_[name][0]) - float(dict_[name][2]))]


def f(name, h):
    words = dict_[name]
    if name == 'humn' and h >= 0:
        return h

    try:
        return int(words[0])
    except:
        assert len(words) == 3
        e1 = f(words[0], h)
        e2 = f(words[2], h)
        if words[1] == '+':
            return e1+e2
        elif words[1] == '*':
            return e1*e2
        elif words[1] == '-':
            return e1-e2
        elif words[1] == '/':
            return e1/e2
        else:
            assert False, expr


for line in lines:
    words = line.split()
    name = words[0][:-1]
    expr = line.split(':')[1]
    dict_[name] = expr.split()

print(int(f('root', -1)))

p1 = dict_['root'][0]
p2 = dict_['root'][2]

if f(p2, 0) != f(p2, 1):
    p1, p2 = p2, p1
assert f(p1, 0) != f(p1, 1)
assert f(p2, 0) == f(p2, 1)
target = f(p2, 0)

lo = 0
hi = int(1e20)
while lo < hi:
    mid = (lo+hi)//2
    score = target - f(p1, mid)
    if score < 0:
        lo = mid
    elif score == 0:
        print(mid)
        break
    else:
        hi = mid
