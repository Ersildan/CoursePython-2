matrix = [list(map(int, input().split())) for i in range(int(input()))]
A, n = [] , len(matrix)
for i in range(n):
    for j in range(len(matrix)):
        if (i >= j and i >= n - 1 - j) or (i <= j and i >= n - 1 - j):
            A.append(matrix[i][j])
print(max(A))
