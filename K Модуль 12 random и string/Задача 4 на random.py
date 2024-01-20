import random

lst = [random.randrange(1, 50) for _ in range(7)]
print(*sorted(lst))
