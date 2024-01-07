# put your python code here
n = int(input())
a, a2 = [],[]
for _ in range(n):
    s = input().split()
    a.append(tuple(s))

for row in a:
    for elem in row:
        print(elem, end =' ')
    print()

for i in range(len(a)):
    if (int(a[i][1])) >= 4:
        a2.append(a[i])
print()
for row in a2:
    for elem in row:
        print(elem, end =' ')
    print()
