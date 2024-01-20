import random

lst = [1, 2, 3, 4, 5, 6]
for _ in range(1, int(input()) + 1):
    print(random.choice(lst))
