import re

with open('nums.txt') as numb:
    my_list = [re.findall(r'\d+', line) for line in numb.readlines()]
    total = 0
    for line in my_list:
        total += sum(list(map(int,line)))
print(total)
