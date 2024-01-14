d = {}
for _ in range(int(input())):
    s = input().split()
    k = s[0]
    v = s[1:]
    res = dict(zip([k],[v]))
    d.update(res)

for _ in range(int(input())):
    s = input()
    for key, value in d.items():
        if s in value:
            print(key)
