# Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

<p align="center">
    <b>3</b> <br>
    <b>7</b> 4 <br>
    2 <b>4</b> 6 <br>
    8 5 <b>9</b> 3
</p>

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in [triangle.txt](resources/txt/p067_triangle.txt), a 15K text file containing a triangle with one-hundred rows.

**NOTE:** This is a much more difficult version of [Problem 18](../18). It is not possible to try every route to solve this problem, as there are 2<sup>99</sup> altogether! If you could check one trillion (10<sup>12</sup>) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

## Python implementation

Load

```python
with open('67/resources/txt/p067_triangle.txt', 'r') as f:
    triangle = [[int(i) for i in line.split(' ')] for line in f.read().splitlines()]
```

While `triangle` as more than one element

```python
while len(triangle) > 1:
```

For each term of the penultimate line

```python
    i, l = 0, len(triangle[-2])
    while i < l:
```

Choose the direction which is preferable between left (`i`) and right (`i + 1`)

```python
        triangle[-2][i] += max(triangle[-1][i], triangle[-1][i + 1])
```

Increment `i`


```python
        i += 1
```

Delete the last line

```python
    triangle = triangle[:-1]
```

The last element of `triangle` is the maximum total

```python
sum = triangle[0][0]
```

### Answer

```python
sum = 7273
```
