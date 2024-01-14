matrix = [list(map(int, input().split())) for i in range(int(input()))]
A = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i >= j or i == j:
            A.append(matrix[i][j])
print(max(A))
