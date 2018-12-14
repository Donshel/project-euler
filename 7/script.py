from functions.myMath import isPrime

n = 10001

i = 2
p = 5

while True:
    if isPrime(p):
        i += 1
        if i == n:
            break
    p += 2
