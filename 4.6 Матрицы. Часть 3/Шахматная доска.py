# put your python code here
s = input().split() 
A = []
n, m = int(s[0]), int(s[1])
for i in range(n):                    #Создаю матрицу из нулей
    A.append([0]*m)
    
for i in range(n):                    #Создаю очередность точки и звездочки
    for j in range(m):
        if (i + j) % 2 == 0:
            A[i][j] = '.'
        else:
            A[i][j] = '*'

for r in range(n):                    #Вывод элементов без кавычек
    for c in range(m):
        print(A[r][c], end = ' ')
    print()
