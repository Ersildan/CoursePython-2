m, n = int(input()), int(input())
a = {input() for _ in range(m)}
b = {input() for _ in range(n)}
if len(a ^ b) == 0:
    print('NO')
else:
    print(len(a ^ b))
