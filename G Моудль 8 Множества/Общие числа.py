s1 = {int(i) for i in input().split()}
s2 = {int(i) for i in input().split()}
print(*sorted(s1 & s2))
