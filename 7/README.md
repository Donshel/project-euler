# 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

## Python implementation

Define

```python
n = 10001
```

Initialize

```python
i = 2
p = 5
```

Until stop

```python
while True:
```

If `p` is prime, increment `i`

```python
    if isPrime(p):
        i += 1
```

If `p` is the `n`<sup>th</sup> prime number, stop

```python
        if i == n:
            break
```

Increment `p`

```python
    p += 1
```

## Answer

<!-- p=104743 -->
<img src="https://latex.codecogs.com/svg.latex?p%3D104743">
