def decomp(n):
    if n < 1:
        return []

    d = [[1, 1], [2, 0]]

    while n > 1:
        while n % d[-1][0] == 0:
            n /= d[-1][0]
            d[-1][1] += 1
        if n != 1:
            if d[-1][1] != 0:
                d += [[d[-1][0], 0]]
            d[-1][0] += 1

    return d

def comp(d):
    n = 1
    for f in d:
        n *= pow(f[0], f[1])

    return n

def lcm(a, b):
    from functions.myArray import merge

    a, b = decomp(a), decomp(b)
    c = merge(max, 0, a, b)

    return comp(c)