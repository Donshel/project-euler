a = 3
b = 5
c = 1000

n_a = ((c - 1) - (c - 1) % a) / a
sum_a = n_a * (1 + n_a) * a / 2

n_b = ((c - 1) - (c - 1) % b) / b
sum_b = n_b * (1 + n_b) * b / 2

n_ab = ((c - 1) - (c - 1) % (a * b)) / (a * b)
sum_ab = n_ab * (1 + n_ab) * (a * b) / 2

sum = sum_a + sum_b - sum_ab
