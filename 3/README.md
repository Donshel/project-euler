# Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

## Mathematics

Any natural <img src="https://latex.codecogs.com/svg.latex?n"> greater than 1 can be written as the product of <img src="https://latex.codecogs.com/svg.latex?k"> powers of prime numbers.

<!-- n=\prod_i^k{f_i}^{e_i}\quad\forall\;e_i\in\mathbb{N}\;\text{and}\;f_i\in\mathbb{N}\setminus\{1\}:\left(\nexists\;x\in\mathbb{N}\setminus\{1,f_i\}:\frac{f_i}{x}\in\mathbb{N}\right) -->
<img src="https://latex.codecogs.com/svg.latex?n%3D%5Cprod_i%5Ek%7Bf_i%7D%5E%7Be_i%7D%5Cquad%5Cforall%5C%3Be_i%5Cin%5Cmathbb%7BN%7D%5C%3B%5Ctext%7Band%7D%5C%3Bf_i%5Cin%5Cmathbb%7BN%7D%5Csetminus%5C%7B1%5C%7D%3A%5Cleft%28%5Cnexists%5C%3Bx%5Cin%5Cmathbb%7BN%7D%5Csetminus%5C%7B1%2Cf_i%5C%7D%3A%5Cfrac%7Bf_i%7D%7Bx%7D%5Cin%5Cmathbb%7BN%7D%5Cright%29">

Therefore, if <img src="https://latex.codecogs.com/svg.latex?f_i%3Ef_%7Bi-1%7D">, the largest prime factor of <img src="https://latex.codecogs.com/svg.latex?n"> is

<!-- f_k=\frac{n}{{f_k}^{e_k-1}\prod_i^{k-1}{f_i}^{e_i}} -->
<img src="https://latex.codecogs.com/svg.latex?f_k%3D%5Cfrac%7Bn%7D%7B%7Bf_k%7D%5E%7Be_k-1%7D%5Cprod_i%5E%7Bk-1%7D%7Bf_i%7D%5E%7Be_i%7D%7D">

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

## Answer

<!-- f=6857 -->
<img src="https://latex.codecogs.com/svg.latex?f%3D6857">
