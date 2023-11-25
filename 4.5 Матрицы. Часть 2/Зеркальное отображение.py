n = int(input())
A = [[int(num) for num in input().split()] for temp in range(n)]

A2 = A.reverse()

for r in range(n):
    for c in range(n):
        print(A[r][c], sep='\n', end=' ')
    print()

