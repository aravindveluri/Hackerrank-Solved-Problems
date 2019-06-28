from itertools import permutations
from math import factorial
def solve(n, m):
    return factorial(m+n-1)/(factorial(m-1) * factorial(n))
print solve(4, 3)