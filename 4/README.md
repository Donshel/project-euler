# Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## Mathematics

If <img src="https://latex.codecogs.com/svg.latex?f"> is a factor of the natural <img src="https://latex.codecogs.com/svg.latex?n">, <img src="https://latex.codecogs.com/svg.latex?f"> is smaller or equal than the square root of <img src="https://latex.codecogs.com/svg.latex?n">.

<!-- \forall\,f\in\mathbb{N}\setminus\{n\}:\frac{n}{f}\in\mathbb{N},\,f\leq\sqrt{n} -->
<img src="https://latex.codecogs.com/svg.latex?%5Cforall%5C%2Cf%5Cin%5Cmathbb%7BN%7D%5Csetminus%5C%7Bn%5C%7D%3A%5Cfrac%7Bn%7D%7Bf%7D%5Cin%5Cmathbb%7BN%7D%2C%5C%2Cf%5Cleq%5Csqrt%7Bn%7D">

## Python implementation

Define

```python
deg = 3
min = pow(10, deg - 1)
max = pow(10, deg) - 1
```

While `m` is a `deg` digit integer

```python
m = max
while m > min:
```

Compute the palindrome which has `m` as first digits

```python
    n = int(str(m) + str(m)[::-1])
```

While `f` is a possible factor of `n`

```python
    f = min
    while pow(f, 2) <= n:
```

If `f` is a factor of `n` and `n / f` is a `deg` digit integer, stop

```python
        if n % f == 0 and n / f < max:
            break
```

Else, increment `f`

```python
        f += 1
```

If `n` is the solution, stop

```python
    if n % f == 0:
        break
```

Decrement `m`

```python
    m -= 1
```

## Answer

<!-- n=906609=913\times993 -->
<img src="https://latex.codecogs.com/svg.latex?n%3D906609%3D913%5Ctimes993">
