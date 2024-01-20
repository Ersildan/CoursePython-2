n = int(input())
matrixA = [['.'] * n for _ in range(n)]
for i in range(n):
        for j in range(n):
            if i == j:
                matrixA[i][j] = '*'
            elif i == n//2:
                matrixA[i][j] = '*'
            elif j == n//2:
                matrixA[i][j] = '*'
            elif j == n - i - 1:
                matrixA[i][j] = '*'
for r in range(n):
    for c in range(n):
        print(str(matrixA[r][c]).ljust(1), end=' ')
    print()
