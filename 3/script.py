n = 600851475143

f = 2
while n != f:
    if n % f == 0:
        n /= f
    else :
        f += 1
