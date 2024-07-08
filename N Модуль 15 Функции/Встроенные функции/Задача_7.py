n = int(input())
lst_ = []
for _ in range(n):
    s = int(input())
    lst = []
    for _ in range(s):
        s_ = input()
        lst.append(s_[-1])
    lst_.append(lst)
print(['NO','YES'][all(map(lambda x: '5' in x, lst_))])