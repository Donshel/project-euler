import numpy as np

deg = 3
min = pow(10, deg - 1)
max = pow(10, deg) - 1

m = max
while m > min:
    n = int(str(m) + str(m)[::-1])
    f = min
    while pow(f, 2) <= n:
        if n % f == 0 and n / f < max:
            break
        f += 1
    if n % f == 0:
        break
    m -= 1
