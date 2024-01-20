m = int(input())
n = int(input())
s = set()
for i in range(n + m):
    s_ = input()
    if s_ in s:
        s.discard(s_)
    else:
        s.add(s_)
print([len(s), 'NO'][len(s) == 0])
