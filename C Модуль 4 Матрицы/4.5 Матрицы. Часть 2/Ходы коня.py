n = 8
matrix = [['.'] * n for _ in range(n)]    # создаем квадратную матрицу размером 8×8

xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])

for i in range(8):
    for j in range(8):
        matrix[x][y] = 'N'
        INX = (x - i) * (y - j)
        if INX == 2 or INX == -2:
            matrix[i][j] = '*'
            
for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
