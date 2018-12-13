from functions.myMath import isPrime

n = 2000000
p = 5

sum = int(2 + 3)
while p < n:
    if isPrime(p):
        sum += p
    p += 2
