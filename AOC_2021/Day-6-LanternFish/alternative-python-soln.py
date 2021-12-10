*a, i = map(eval(input()).count, range(10))

while i < 255:
    a[(i+7) % 9] += a[i % 9]
    i += 1
print(sum(a))
