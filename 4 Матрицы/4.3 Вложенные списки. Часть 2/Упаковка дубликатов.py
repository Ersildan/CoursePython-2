res = []

for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)
