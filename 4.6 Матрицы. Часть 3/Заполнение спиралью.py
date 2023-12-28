n, m = [int(i) for i in input().split()]
A = [[0] * m for _ in range(n)]
i = 1 # счетчик
x = 0
y = -1
d_row = 0 # -1 0 1 - движение по рядам
d_column = 1 # -1 0 1 - движение по столбцам

while i <= n*m:
    if 0 <= x + d_row < n and 0 <= y + d_column < m and A[x + d_row ][y + d_column] == 0:
        x += d_row
        y += d_column
        A[x][y] = i
        i += 1
    else:
        if d_column == 1:
            d_column = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_column = -1
        elif d_column == -1:
            d_column = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_column = 1
#вывод матрицы

for r in A:
  for c in r:
    print(c, end = ' ')
  print()
