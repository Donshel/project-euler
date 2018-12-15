# Special Pythagorean triplet

<!-- a<b<c -->
A Pythagorean triplet is a set of three natural numbers, <img src="https://latex.codecogs.com/svg.latex?a%3Cb%3Cc">, for which,

<p align="center">
    <!-- a^2+b^2=c^2 -->
    <img src="https://latex.codecogs.com/svg.latex?a%5E2%2Bb%5E2%3Dc%5E2">
</p>

<!-- 3^2+4^2=9+16=25=5^2 -->
For example, <img src="https://latex.codecogs.com/svg.latex?3%5E2%2B4%5E2%3D9%2B16%3D25%3D5%5E2">.

<!-- a+b+c=1000 -->
There exists exactly one Pythagorean triplet for which <img src="https://latex.codecogs.com/svg.latex?a%2Bb%2Bc%3D1000">.  
Find the product <img src="https://latex.codecogs.com/svg.latex?abc">.

## Mathematics

Let be <img src="https://latex.codecogs.com/svg.latex?a">, <img src="https://latex.codecogs.com/svg.latex?b"> and <img src="https://latex.codecogs.com/svg.latex?c"> three naturals such that <img src="https://latex.codecogs.com/svg.latex?a%3Cb%3Cc"> and <img src="https://latex.codecogs.com/svg.latex?a%2Bb%2Bc%3Dn">.

Therefore,

<p align="center">
    <!-- c>\frac{n}{3}+1 -->
    <img src="https://latex.codecogs.com/svg.latex?c%3E%5Cfrac%7Bn%7D%7B3%7D%2B1"> and
    <!-- b>\frac{c}{2}+1 -->
    <img src="https://latex.codecogs.com/svg.latex?b%3E%5Cfrac%7Bc%7D%7B2%7D%2B1">
</p>

## Python implementation

Define

```python
n = 1000;
```

While `c` is acceptable

```python
c = np.ceil(n / 3) + 1;
while c < n:
```

While `b` is acceptable

```python
    b = np.ceil(c / 2) + 1
    while b < c:
```

If `a` verify the Pythagorean triplet condition, stop

```python
        a = n - b - c
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            break
```

Increment `b`

```python
        b += 1
```

If the algorithm has found a solution, stop

```python
    if b != c:
        break
```

Increment `c`

```python
    c += 1
```

Compute the product `a * b * c`

```python
prod = a * b * c
```

### Answer

```python
prod = 31875000
```
