n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(m)]
matrixC = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for q in range(m):
            matrixC[i][j] += matrixA[i][q] * matrixB[q][j]

for row in matrixC:
    print(*row)
