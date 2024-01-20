n = int(input())
flag = 'YES'
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
matrixA.reverse()
for i in range(n):
    for j in range(n):
        if matrixA[i][j] == matrixA[j][i]:
            flag = 'YES'
            continue
        else:
            flag = 'NO'
            break
print(flag)
