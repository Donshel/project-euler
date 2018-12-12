f0 = 0
f1 = 1
fmax = 4000000

sum = 0;

while f1 <= fmax:
    if f1 % 2 == 0:
        sum += f1
    f0, f1 = f1, f0 + f1
