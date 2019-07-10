from functools import reduce
from operator import mul, add
from functions.myMath import decomp

def d(n):
    f =  decomp(n)[1:]
    t = [(pow(i[0], i[1] + 1) - 1) / (i[0] - 1) for i in f]

    return int(reduce(mul, t) - n)

n = 10000

amicable = set()
unfriendly = set()

a = 2
while a < n:
    if a not in amicable and a not in unfriendly:
        b = d(a)
        if d(b) == a and b != a:
            amicable |= {a, b}
        else:
            if b > a:
                unfriendly |= {b}

    a += 1

sum = reduce(add, amicable)
