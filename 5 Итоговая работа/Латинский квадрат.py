n = int(input())
a, flag1, flag2 = [], True, True
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
matrixB = [list(i) for i in zip(*matrixA)]

for i in range(1, n + 1):
    a.append(i)
for i in matrixA:
    if sorted(i) != a:
        flag1 = False
for i in matrixB:
    if sorted(i) != a:
        flag2 = False
if flag1 and flag2 == True:
    print('YES')
else:
    print('NO')
