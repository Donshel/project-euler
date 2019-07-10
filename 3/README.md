# Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

## Mathematics

Any natural <img src="https://latex.codecogs.com/svg.latex?n"> greater than 1 can be written as the product of <img src="https://latex.codecogs.com/svg.latex?k"> powers of prime numbers.

<p align="center">
    <!-- n=\prod_i^k{f_i}^{e_i} -->
    <img src="https://latex.codecogs.com/svg.latex?n%3D%5Cprod_i%5Ek%7Bf_i%7D%5E%7Be_i%7D">
</p>

With <img src="https://latex.codecogs.com/svg.latex?f_i"> the prime factors and <img src="https://latex.codecogs.com/svg.latex?e_i"> their non-zero power.

Therefore, if <img src="https://latex.codecogs.com/svg.latex?f_i%3Ef_%7Bi-1%7D">, the largest prime factor of <img src="https://latex.codecogs.com/svg.latex?n"> is

<p align="center">
    <img src="https://latex.codecogs.com/svg.latex?f_k%3D%5Cfrac%7Bn%7D%7B%7Bf_k%7D%5E%7Be_k-1%7D%5Cprod_i%5E%7Bk-1%7D%7Bf_i%7D%5E%7Be_i%7D%7D">
</p>

## Python implementation

Define

```python
n = 600851475143
```

While `n` differs from `f`

```python
f = 2
while n != f:
```

If `f` divides `n`, do so

```python
    if n % f == 0:
        n /= f
```

Else, increment `f`

```python
    else :
        f += 1
```

### Answer

```python
f = 6857
```
