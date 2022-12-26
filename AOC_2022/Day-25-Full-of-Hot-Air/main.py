def f(s):               # SNAFU to decimal
    if s:               # if s is not empty
        *a, b = s       # remove last char
        return f(a)*5 + '=-012'.find(b)-2
    else:
        return 0      # base case


def g(d):               # decimal to SNAFU
    if d:               # if d is not zero
        a, b = divmod(d+2, 5)
        return g(a) + '=-012'[b]
    else:
        return ''     # base case


print(g(sum(map(f, open('data.txt').read().split()))))
