n = int(input())
A = []
for _ in range(n):
    temp = [int(num) for num in input().split()]
    A.append(temp)

A2 = A.reverse()

for r in range(n):
    for c in range(n):
        print(A[c][r], sep='\n', end=' ')
    print()
