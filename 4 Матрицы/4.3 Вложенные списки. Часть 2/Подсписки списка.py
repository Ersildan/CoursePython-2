L, D =  [[]], []
s = input().split()
shift = len(s)

for i in range(shift):
    for j in range(shift):
        D = s[j : i + j + 1]
        if len(D) == i + 1:
            L.append(D)
print(L)
