n = 8
matrix = [['.']*n for _ in range(n)]

xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])

for i in range(8):
    for j in range(8):
        matrix[x][y] = 'Q'
        if abs(x - i) == abs(y-j):
            matrix[i][j] = '*'
        elif x == i and x == i or y == j and y == j:
            matrix[i][j] = '*'
for r in range(n): 
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
