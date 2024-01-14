s = input().split() 
A, total = [], 0
n, m = int(s[0]), int(s[1])
for i in range(n):
    A.append([0]*m)
    
for i in range(n):
    for j in range(m):
        A[i][j] = total + 1
        total += 1

for r in range(n):
    for c in range(m):
        print(str(A[r][c]).ljust(3), end = ' ')
    print()
