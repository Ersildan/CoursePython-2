n = int(input()) 
A = []
for _ in range(n):
    A.append([0]*n)
    
for i in range(n):
    for j in range(n):
        if (i < j and i < n - 1 - j) or (i > j and i < n - 1 -j):
            A[i][j] = 0
        elif (i > j and i > n- 1 - j) or (i < j and i > n - 1 - j):
            A[i][j] = 0
        elif i == j:
            A[i][j] = 1
        else:
            A[i][j] = 1

for r in range(n):
    for c in range(n):
        print(A[r][c], end = ' ')
    print()
  
