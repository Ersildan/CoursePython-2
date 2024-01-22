from fractions import Fraction as F

n = int(input())
x = 0
for i in range(1, n + 1):
    x += F(1, i**2)
print(x)
