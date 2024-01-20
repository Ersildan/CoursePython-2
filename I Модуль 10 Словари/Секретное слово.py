s = input()
d = {}
d_ = {}
for _ in s:
    d[_] = d.get(_, 0) + 1
for _ in range(int(input())):
    k, v = input().split(':')
    d_.setdefault(int(v), []).append(k)
for i in s:
    for k, v in d.items():
        if k == i:
            print(*d_[v], end='')
print()
