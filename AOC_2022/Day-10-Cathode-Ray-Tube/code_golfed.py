R = C = 0
S = ""
X = 1


def T(): global R, C, S; C += 1; R += X*C * \
    ((W := C % 40) == 20); S += " #"[X <= W < X+3]+"\n"[W:]


for L in open(0):
    T()
    if'b' > L:
        T()
        X += int(L[4:])
print(S, R)
