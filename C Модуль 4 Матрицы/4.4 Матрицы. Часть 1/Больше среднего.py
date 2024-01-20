matrix = [list(map(int, input().split())) for i in range(int(input()))]
for i in matrix:
    count = 0
    for j in i:
        if j > (sum(i)/len(i)):
            count += 1
    print(count)
