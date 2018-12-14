from functools import reduce
from functions.myMath import lcm

m = range(1, 20)

prod = reduce(lcm, m)
