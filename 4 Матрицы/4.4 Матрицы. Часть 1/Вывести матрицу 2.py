n = int(input()) # n - количество строк 
m = int(input()) # m - столбцов в матрице

L = [ [0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        L[i][j] = input()       
for row in L:
    for elem in row:
        print(elem, end = ' ')
    print()
print()
for i in range(m):
    for j in range(n):
        print(L[j][i], end = ' ')
    print()
