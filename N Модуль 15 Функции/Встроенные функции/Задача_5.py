a, b = int(input()), int(input())
lst = [i for i in range(a, b + 1) if '0' not in str(i)]
new_lst = [i for i in lst if all(i % int(x) == 0 for x in str(i))]
print(*new_lst)