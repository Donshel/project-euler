with open('67/resources/txt/p067_triangle.txt', 'r') as f:
    triangle = [[int(i) for i in line.split(' ')] for line in f.read().splitlines()]

while len(triangle) > 1:
    i, l = 0, len(triangle[-2])
    while i < l:
        triangle[-2][i] += max(triangle[-1][i], triangle[-1][i + 1])
        i += 1
    triangle = triangle[:-1]

sum = triangle[0][0]
