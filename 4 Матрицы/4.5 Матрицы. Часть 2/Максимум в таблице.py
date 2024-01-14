n, m = int(input()), int(input())
max_num = -1000
A = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    A.append(temp)
    
for i in range(n):
    for j in range(m):
        if int(A[i][j]) >= max_num:
            max_num = int(A[i][j])

for i in range(n):
    if max_num in A[i]:
        print(i, A[i].index(max_num))
        break
