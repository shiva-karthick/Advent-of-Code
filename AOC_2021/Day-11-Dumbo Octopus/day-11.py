# Part 1
print((u := lambda i, c, e: 1if(i in e or c[i] < 10)else(e.add(i) or [c.__setitem__(i+d, c[i+d]+1) or u(i+d, c, e)for d in (-11, -10, -9, -1, 1, 9, 10, 11)if 0 <= i+d < 100 and -2 < i % 10-(i+d) % 10 < 2])) and (g := lambda c: (
    e := set()) or [u(i, c, e)for i in range(100)] and [c.__setitem__(i, 1+(i not in e and c[i]))for i in range(100)] and len(e)) and (c := [int(i)+1 for l in open("input.txt").read().splitlines()for i in l]) and sum(g(c)for _ in range(100)))

# Part 2
print((u := lambda i, c, e: 1if(i in e or c[i] < 10)else(e.add(i) or [c.__setitem__(i+d, c[i+d]+1) or u(i+d, c, e)for d in (-11, -10, -9, -1, 1, 9, 10, 11)if 0 <= i+d < 100 and -2 < i % 10-(i+d) % 10 < 2])) and (g := lambda c: (e := set()) or [
      u(i, c, e)for i in range(100)] and [c.__setitem__(i, 1+(i not in e and c[i]))for i in range(100)] and len(e)) and (s := lambda c, n: n if g(c) == 100 else s(c, n+1)) and (c := [int(i)+1 for l in open("input.txt").read().splitlines()for i in l]) and s(c, 1))
