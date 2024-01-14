s = input() + input()
lst = []
set_s = set(s)
for i in range(0, 10):
    lst.append(str(i))

if lst == sorted(set_s):
    print('YES')
else:
    print('NO')

'''На вход программе подаются две строки, состоящие из цифр. 
Необходимо определить, верно ли, что в записи этих двух строк 
используются все десять цифр?'''