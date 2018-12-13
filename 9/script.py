import numpy as np

n = 1000;

c = np.ceil(n / 3) + 1;
while c < n:
    b = np.ceil(c / 2) + 1
    while b < c:
        a = n - b - c
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            break
        b += 1
    if b != c:
        break
    c += 1
    
prod = a*b*c
