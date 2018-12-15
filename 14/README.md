# Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)  
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

<p align="center">
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
</p>

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

**NOTE:** Once the chain starts the terms are allowed to go above one million.

## Python implementation

Define

```python
n = 1000000
```

Initialize the longest sequence `seqList` and `seqSet`, an ordered vector of its elements

```python
seqList = [1]
seqSet = set(seqList)
```

While `i` hasn't reached `n`

```python
i = 2
while i < n:
```

Initialize `temp`

```python
    temp = [i]
```

While the last element of `temp` is not already in the longest sequence, compute the next one

```python
    while temp[-1] not in seqSet:
        if temp[-1] % 2 == 0:
            temp += [int(temp[-1] / 2)]
        else:
            temp += [int(3 * temp[-1] + 1)]
```

If the sequence up to the last element of `temp` is longer in `temp` than in `seqList`, replace it

```python
    l = seqList.index(temp[-1]) + 1
    if (len(temp) > l):
        seqList = temp + seqList[l:]
```

Update `seqSet`

```python
        seqSet = set(seqList)
```

Increment `i`

```python
    i += 1
```

### Answer

```python
n = 837799
```
