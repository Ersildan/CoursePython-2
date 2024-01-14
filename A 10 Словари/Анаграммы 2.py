import re

s = re.sub(r'[.,;:-?-!]', '', input().lower())
s_ = re.sub(r'[.,;:-?-!]', '', input().lower())
s = s.replace(' ', "")
s_ = s_.replace(' ', "")

d = {}

for c in s:
    d[c] = d.get(c, 0) + 1
for c in s_:
    d[c] = d.get(c, 0) - 1

print(('NO', 'YES')[set(d.values()) == {0}])
