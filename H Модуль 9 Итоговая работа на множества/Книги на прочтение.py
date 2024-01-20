m, n = int(input()), int(input())
lst = set()
for _ in range(m):
    s = input()
    lst.add(s)
for _ in range(n):
    s = input()
    if s in lst:
        print('YES')
    else:
        print('NO')
