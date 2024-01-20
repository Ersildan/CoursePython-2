from math import factorial

n = int(input())
lst = []
for i in range(n + 1):
    lst.append(int((factorial(n))/(factorial(i) * factorial(n - i))))
print(lst)
