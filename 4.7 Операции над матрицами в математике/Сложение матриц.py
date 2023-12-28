n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrixB = [[int(i) for i in input().split()] for _ in range(n)]
matrixC = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

for row in matrixC:
    print(*row)
