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

def maxReduce(op, n, A):
    from numpy import array
    from functools import reduce

    maxR, temp = 0, 0

    A = array(A)

    if len(A.shape) > 1:
        for B in A:
            temp = maxReduce(op, n, B)
            maxR = max(temp, maxR)
    else:
        i = n - 1
        while i < A.shape[0]:
            if temp == 0:
                temp = reduce(op, A[i - n + 1:i + 1])
            else:
                temp = A[i] * temp / A[i - n]
                if temp == 0:
                    i += n
                    continue
                maxR = max(temp, maxR)
            i += 1

    return maxR
