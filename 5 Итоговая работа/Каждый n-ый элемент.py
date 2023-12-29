s = input().split()
a = []
num = int(input())
for i in range(num):
    a.append(s[i::num])
print(a)
