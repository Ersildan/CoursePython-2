n, m = int(input()), int(input())
A = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    A.append(temp)
    
x = [int(i) for i in input().split()]
a1, a2 = x[0], x[1]

for i in range(n):
    A[i][a1], A[i][a2] = A[i][a2], A[i][a1]
for r in range(n):
    for c in range(m):
        print(A[r][c], sep='\n', end=' ')
    print()
