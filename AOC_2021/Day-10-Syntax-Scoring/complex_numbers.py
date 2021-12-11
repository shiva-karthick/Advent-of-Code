def solve(datafile="input.txt"):
    DELIMS = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
        "(": -3,
        "[": -57,
        "{": -1197,
        "<": -25137,
    }
    RDELIMS = {-3: 1, -57: 2, -1197: 3, -25137: 4}

    def check(line):
        stack = []
        for _ in line:
            d = DELIMS[_]
            if d < 0:
                stack.insert(0, d)
            else:
                if d + stack.pop(0):
                    return complex(0, d)

        return complex(int("".join([str(RDELIMS[v]) for v in stack]), 5), 0)

    ls = [_ for _ in (check(_.strip()) for _ in open(resolve(datafile))) if _]
    ss = sorted([_.real for _ in ls if _.real])

    return (int(sum(_.imag for _ in ls)), int(ss[len(ss) >> 1]))
