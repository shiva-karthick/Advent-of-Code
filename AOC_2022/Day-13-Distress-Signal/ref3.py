raw = open(0).read()


class Packet:
    def __init__(self, data):
        self.items = data

    def __lt__(self, other):
        return compare(self.items, other.items) == 1


def compare(x, y):
    t_x, t_y = type(x), type(y)
    if t_x == t_y == int:
        if x < y:
            return 1
        elif x == y:
            return 0
        else:
            return -1
    if not t_x == t_y == list:
        if t_x == int:
            x = [x]
        else:
            y = [y]
    for i_x, i_y in zip(x, y):
        result = compare(i_x, i_y)
        if result:
            return result
    return compare(len(x), len(y))


data = []
data2 = [div1 := Packet([[2]]), div2 := Packet([[6]])]
for p in raw.split('\n\n'):
    a, b = p.split('\n')
    data.append((Packet(eval(a)), Packet(eval(b))))
    data2.extend((Packet(eval(a)), Packet(eval(b))))

t = 0
for i, (a, b) in enumerate(data):
    if compare(a.items, b.items) == 1:
        t += i + 1
print(t)

data2.sort()
print((data2.index(div1) + 1) * (data2.index(div2) + 1))
