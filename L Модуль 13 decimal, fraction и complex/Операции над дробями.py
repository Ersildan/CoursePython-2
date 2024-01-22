from fractions import Fraction as F

a, b = input(), input()
print(f'{a} + {b} = {F(F(a) + F(b))}')
print(f'{a} - {b} = {F(F(a) - F(b))}')
print(f'{a} * {b} = {F(F(a) * F(b))}')
print(f'{a} / {b} = {F(F(a) / F(b))}')
