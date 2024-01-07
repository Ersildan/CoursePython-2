n = int(input())
t1 = t2 = t3 = 1
for _ in range(n):
    print(t1, end=' ')
    t1, t2, t3 = t2, t3, t1 + t2 + t3
