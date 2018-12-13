# Sum square difference

The sum of the squares of the first ten natural numbers is,

<!-- 1^2+2^2+\dots+10^2=385 -->
<img src="https://latex.codecogs.com/svg.latex?1%5E2%2B2%5E2%2B%5Cdots%2B10%5E2%3D385">

The square of the sum of the first ten natural numbers is,

<!-- (1+2+\dots+10)^2=3025 -->
<img src="https://latex.codecogs.com/svg.latex?%281%2B2%2B%5Cdots%2B10%29%5E2%3D3025">

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Mathematics

We have

<!-- \sum_{i=1}^{n}i=\frac{n(n+1)}{2} -->
<img src="https://latex.codecogs.com/svg.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7Di%3D%5Cfrac%7Bn%28n%2B1%29%7D%7B2%7D">

and

<!-- \sum_{i=1}^{n}i^2=\frac{n(n+1)(2n+1)}{6} -->
<img src="https://latex.codecogs.com/svg.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7Di%5E2%3D%5Cfrac%7Bn%28n%2B1%29%282n%2B1%29%7D%7B6%7D">

## Python implementation

Define

```python
n = 100
```

Compute `sum_of_squares`, `square_of_sum` and `diff`

```python
sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
square_of_sum = pow(n * (n + 1) / 2, 2)
diff = square_of_sums - sum_of_squares
```

## Answer

<!-- \sum_{i=1}^{100}i-\sum_{i=1}^{100}i^2=25164150 -->
<img src="https://latex.codecogs.com/svg.latex?%5Csum_%7Bi%3D1%7D%5E%7B100%7Di-%5Csum_%7Bi%3D1%7D%5E%7B100%7Di%5E2%3D25164150">
