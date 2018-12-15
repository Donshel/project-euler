# Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

## Python implementation

Define

```python
n = 2000000
p = 5
```

Initialize the sum for the two first primes

```python
sum = np.int(2 + 3)
```

Until the number `n` is reached

```python
while p < n:
```

If `p` is prime, add it to the sum

```python
    if isPrime(p):
        sum += p
```

Increment `p`

```python
    p += 2
```

### Answer

```python
sum = 142913828922
```
