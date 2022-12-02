from collections import defaultdict as dicc


def solve():
    with open('input.txt') as f:
        d, i = f.read().split('\n\n')
    res = dicc(int)
    for x in d.split('\n'):
        x = x.split(',')
        res[int(x[0]), int(x[1])] = 1
    inst = i.split('\n')
    for k in inst:
        if k != "":
            ins, c = k[11:].split('=')
        for i in res.copy():
            if ins.endswith('y'):
                if i[1] > int(c):
                    res[i[0], i[1] - 2*(i[1]-int(c))] = 1
                    del res[i[0], i[1]]
            if ins.endswith('x'):
                if i[0] > int(c):
                    res[i[0]-2*(i[0]-int(c)), i[1]] = 1
                    del res[i[0], i[1]]
    _ = max(res.keys(), key=lambda x: x[0])

    print('\n'.join(''.join('█' if res[j, i] else ' ' for j in range(
        _[0]+1)) for i in range(_[1]+1)))


solve()
