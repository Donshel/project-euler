# Amicable numbers

Let *d(n)* be defined as the sum of proper divisors of *n* (numbers less than *n* which divide evenly into *n*).  
If *d(a) = b* and *d(b) = a*, where *a* is different of *b*, then *a* and *b* are an amicable pair and each of *a* and *b* are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore *d*(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so *d*(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

## Mathematics

Any natural <img src="https://latex.codecogs.com/svg.latex?n"> greater than 1 can be written as the product of <img src="https://latex.codecogs.com/svg.latex?k"> powers of prime numbers.

<p align="center">
    <!-- n=\prod_i^k{f_i}^{e_i} -->
    <img src="https://latex.codecogs.com/svg.latex?n%3D%5Cprod_i%5Ek%7Bf_i%7D%5E%7Be_i%7D">
</p>

With <img src="https://latex.codecogs.com/svg.latex?f_i"> the prime factors and <img src="https://latex.codecogs.com/svg.latex?e_i"> their non-zero power.

Therefore, the sum of proper divisors of <img src="https://latex.codecogs.com/svg.latex?n">, <img src="https://latex.codecogs.com/svg.latex?d%28n%29"> is determined by

<p align="center">
    <img src="https://latex.codecogs.com/svg.latex?d%28n%29%3D%5Cleft%5B%5Cprod_i%5E%7Bk%7D%5Cfrac%7B%7Bf_i%7D%5E%7Be_i%2B1%7D-1%7D%7Bf_i-1%7D%5Cright%5D-n">
</p>

## Python implementation

Define

```python
def d(n):
    f =  decomp(n)[1:]
    t = [(pow(i[0], i[1] + 1) - 1) / (i[0] - 1) for i in f]

    return int(reduce(mul, t) - n)

n = 10000
```

Initialize

```python
amicable = set()
unfriendly = set()
```

Until `a` has reached `n`

```python
a = 2
while a < n:
```

If `a` hasn't already been checked

```python
    if a not in amicable and a not in unfriendly:
```

If `a` is amicable, add `a` and `d(a)` to the `amicable` set

```python
        b = d(a)
        if d(b) == a and b != a:
            amicable |= {a, b}
        else:
            if b > a:
                unfriendly |= {b}
```

Increment `a`

```python
    a += 1
```

Compute the sum of amicables

```python
    sum = reduce(add, amicable)
```

### Answer

```python
sum = 31626
```
