# Power digit sum

2<sup>15</sup> = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2<sup>1000</sup>?

## Python

Define

```python
b, n = 2, 1000
```

Computes `b` to the `n`<sup>th</sup>

```python
p = pow(b, n)
```

Computes the `sum` of the digits

```python
sum = sum([int(i) for i in str(p)])
```

### Answer

```python
sum = 1366
```
