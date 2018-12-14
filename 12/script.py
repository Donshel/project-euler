from functools import reduce
from operator import mul
from functions.myMath import decomp, comp

d = 500

n = 2
while True:
    triangle = decomp(n * (n + 1) / 2)[1:]

    e = [f[1] + 1 for f in triangle]
    g = reduce(mul, e)
    if g > d:
        break

    n += 1

triangle = comp(triangle)
