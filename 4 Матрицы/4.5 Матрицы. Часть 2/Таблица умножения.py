m, n = int(input()), int(input())
A = [[str(i * j).ljust(3) for i in range(n)] for j in range(m)]
[print(*i) for i in A]
