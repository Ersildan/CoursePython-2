from fractions import Fraction as F
from math import *

n = int(input())
x = 0
for i in range(1, n + 1):
    x += F(1, factorial(i))
print(x)
