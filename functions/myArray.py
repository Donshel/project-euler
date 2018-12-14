def merge(op, n, a, b):
    def take(x):
        return x[n]

    a, b = sorted(list(a), key=take), sorted(list(b), key=take)
    c = sorted(a + b, key=take)

    m = min([a[-1][n], b[-1][n]])

    i = 0
    while c[i][n] <= m:
        if c[i][n] == c[i + 1][n]:
            j = 0
            while c[i][j:]:
                if j != n:
                    c[i][j] = op(c[i][j], c[i + 1][j])
                j += 1
            c = c[:i + 1] + c[i + 2:]
        if c[i + 1:]:
            i += 1
        else:
            break

    return c
