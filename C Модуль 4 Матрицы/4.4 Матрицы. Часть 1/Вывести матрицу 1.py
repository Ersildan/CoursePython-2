n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
