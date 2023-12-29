matrix = [list(map(int, input().split())) for i in range(int(input()))]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[j][i], end = ' ')
    print()
