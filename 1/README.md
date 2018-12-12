# Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Mathematics

Let be <img src="https://latex.codecogs.com/svg.latex?a">, <img src="https://latex.codecogs.com/svg.latex?b"> and <img src="https://latex.codecogs.com/svg.latex?c">, three strictly positive integers with <img src="https://latex.codecogs.com/svg.latex?c"> the greatest.

The sum of the multiples of <img src="https://latex.codecogs.com/svg.latex?a"> **or** <img src="https://latex.codecogs.com/svg.latex?b"> up to <img src="https://latex.codecogs.com/svg.latex?c"> is equal to the sum of the sum of <img src="https://latex.codecogs.com/svg.latex?a"> multiples and <img src="https://latex.codecogs.com/svg.latex?b"> multiples minus the sum of <img src="https://latex.codecogs.com/svg.latex?a"> **and** <img src="https://latex.codecogs.com/svg.latex?b"> multiples.

<!-- \sum=\sum_{i=1}^{n_a}ia+\sum_{i=1}^{n_b}ib-\sum_{i=1}^{n_{ab}}iab -->
<img src="https://latex.codecogs.com/svg.latex?%5Csum%3D%5Csum_%7Bi%3D1%7D%5E%7Bn_a%7Dia%2B%5Csum_%7Bi%3D1%7D%5E%7Bn_b%7Dib-%5Csum_%7Bi%3D1%7D%5E%7Bn_%7Bab%7D%7Diab">

With <img src="https://latex.codecogs.com/svg.latex?n_x"> the number of multiples of <img src="https://latex.codecogs.com/svg.latex?x"> between <img src="https://latex.codecogs.com/svg.latex?x"> and <img src="https://latex.codecogs.com/svg.latex?c-1">.

<!-- n_x=\frac{(c-1)-(c-1)\;\text{mod}\;x}{x} -->
<img src="https://latex.codecogs.com/svg.latex?n_x%3D%5Cfrac%7B%28c-1%29-%28c-1%29%5C%3B%5Ctext%7Bmod%7D%5C%3Bx%7D%7Bx%7D">

But we know that

<!-- \sum_{i=1}^{n}i=\frac{n(1+n)}{2} -->
<img src="https://latex.codecogs.com/svg.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7Di%3D%5Cfrac%7Bn%281%2Bn%29%7D%7B2%7D">

Therefore,

<!-- \sum_{i=1}^{n_x}ix=a\frac{n_x(1+n_x)}{2} -->
<img src="https://latex.codecogs.com/svg.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn_x%7Dix%3Da%5Cfrac%7Bn_x%281%2Bn_x%29%7D%7B2%7D">

Finally,

<!-- \sum=a\frac{n_a(1+n_a)}{2}+b\frac{n_b(1+n_b)}{2}-ab\frac{n_{ab}(1+n_ab)}{2} -->
<img src="https://latex.codecogs.com/svg.latex?%5Csum%3Da%5Cfrac%7Bn_a%281%2Bn_a%29%7D%7B2%7D%2Bb%5Cfrac%7Bn_b%281%2Bn_b%29%7D%7B2%7D-ab%5Cfrac%7Bn_%7Bab%7D%281%2Bn_ab%29%7D%7B2%7D">

## Python implementation

Define

```python
a = 3
b = 4
c = 1000
```

For `x` being successively `a`, `b` and `ab`

```python
n_x = ((c - 1) - (c - 1) % x) / x
sum_x = n_x * (1 + n_x) * x / 2
```

Then

```python
sum = sum_a + sum_b - sum_ab
```

## Answer

<!-- \sum=233168 -->
<img src="https://latex.codecogs.com/svg.latex?%5Csum%3D233168">
