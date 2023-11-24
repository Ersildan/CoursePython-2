n, A, total = int(input()), [], 0
for _ in range(n):
    a = [int(i) for i in input().split()]
    A.append(a)

for i in range(n):
    for j in range(n):
        if i == j:
            total += A[i][j]
print(total)
