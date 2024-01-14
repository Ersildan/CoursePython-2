n = int(input())
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for _ in range(n):
    s = {int(i) for i in input()}
    a.intersection_update(s)
print(*sorted(a))
