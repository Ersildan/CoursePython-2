# put your python code here
n = int(input())
lst = []
for _ in range(n):
    lst.append([int(i) for i in input().split('.')])
new_lst = sorted(lst)
for i in new_lst:
    print(*i,sep='.')
