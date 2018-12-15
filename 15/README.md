# Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

<p align="center">
    <img src="resources/gif/p015.gif">
</p>

How many such routes are there through a 20×20 grid?

## Mathematics

For a <img src="https://latex.codecogs.com/svg.latex?m"> by <img src="https://latex.codecogs.com/svg.latex?p"> grid, we have <img src="https://latex.codecogs.com/svg.latex?n">, the number of routes, with

<p align="center">
    <!-- n=\frac{(m+p)!}{m!\,p!} -->
    <img src="https://latex.codecogs.com/svg.latex?n%3D%5Cfrac%7B%28m%2Bp%29%21%7D%7Bm%21%5C%2Cp%21%7D">
</p>

## Python

Define

```python
m, p = 20, 20
```

Computes `n`

```python
n = factorial(m + p) / (factorial(m) * factorial(p))
```

### Answer

```python
n = 137846528820
```
