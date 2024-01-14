n = int(input())
lst1 = set()
lst2 = []
for i in range(n):
    s = input()
    lst1.add(s)
    lst2.append(s)
s_ = input()
lst1.add(s_)
lst2.append(s_)
print('REPEAT' if len(lst1) != len(lst2) else 'OK')

'''Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов,
 особенно Тимур, однако к концу игры ввиду своего возраста забывают, какие города уже называли.'''