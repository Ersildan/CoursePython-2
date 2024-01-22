from fractions import Fraction as F

print(*sorted(set(F(j, i) for i in range(1, int(input()) + 1) for j in range(1, i))), sep='\n')
