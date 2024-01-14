matrix = [list(map(int, input().split())) for i in range(int(input()))]
a1, a2, a3, a4 = [],[],[],[]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i > j and i < len(matrix) - 1 - j:
            a1.append(matrix[i][j])
        if i < j and i > len(matrix) - 1 - j:
            a3.append(matrix[i][j])
        if i < j and i < len(matrix) - 1 - j:
            a2.append(matrix[i][j])
        if i > j and i > len(matrix) - 1 - j:
            a4.append(matrix[i][j])
print('Верхняя четверть:', sum(a2))
print('Правая четверть:', sum(a3))
print('Нижняя четверть:', sum(a4))
print('Левая четверть:', sum(a1))
