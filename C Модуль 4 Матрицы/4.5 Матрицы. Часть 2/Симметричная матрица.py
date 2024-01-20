n = int(input())
A, total = [], 0
for _ in range(n):
    temp = [int(num) for num in input().split()]
    A.append(temp)

for i in range(n):
    for j in range(n):
        if A[i][j] == A[j][i]:
            total += 1
if total == n * n:
    print ('YES')
else:
    print('NO')
