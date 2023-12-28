n, m = [int(i) for i in input().split()]
A = [[0] * m for _ in range(n)]
a  = 1
for x in range(n*m):
    for i in range(n):
        for j in range(m):
            if i + j == x:
                A[i][j] = a
                a += 1
for r in range(n):
    for c in range(m):
        print(str(A[r][c]).ljust(3), end=' ')
    print()
