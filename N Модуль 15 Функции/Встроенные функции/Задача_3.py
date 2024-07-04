abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))
lst = []
for i in zip(abscissas, ordinates, applicates):
    lst.append(sum(list(map(lambda x: x**2, list(i)))) <= 4)
print(all(lst))