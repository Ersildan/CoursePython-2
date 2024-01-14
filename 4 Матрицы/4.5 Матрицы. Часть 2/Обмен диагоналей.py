n = int(input())
A = []
for _ in range(n):
    temp = [int(num) for num in input().split()]
    A.append(temp)

for i in range(len(A)):
    for j in range(len(A)):
        if i > j and i == n - 1 - j:
            A[i][j], A[j][j] = A[j][j], A[i][j]
            
        if i < j and j == n - 1 - i:
            A[i][j], A[j][j] = A[j][j], A[i][j]
            

for r in range(n):
    for c in range(n):
        print(A[r][c], sep='\n', end=' ')
    print()
  
