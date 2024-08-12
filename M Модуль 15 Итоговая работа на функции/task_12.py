# put your python code here
n = int(input())
lst = []
for _ in range(n):
    s = input()
    lst.append(s)
new_lst = sorted(lst)
print(*sorted(new_lst, key=(lambda word: sum([ord(i) - ord('A') for i in word.upper()]))), sep= "\n")

