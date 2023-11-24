matrix = [list(map(int, input().split())) for i in range(int(input()))]
A = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (i >= j and i <= len(matrix) - 1 - j) or (i <= j and i >= len(matrix) - 1 - j):
            A.append(matrix[i][j])
print(max(A))
