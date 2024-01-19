import random
lst = ['Орел', 'Решка']
n = int(input())    # количество попыток
for i in range(n):
    print(lst[random.randint(0, 1)])
