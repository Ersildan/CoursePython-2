n, lst = int(input()), []
for i in range(n):
    s = input()
    s = s.lower()
    lst.append(len(set(s)))
print(*lst, sep='\n')
