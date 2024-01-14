my_dict = {}
for _ in range(int(input())):
    k, v = input().split()
    res = dict(zip([k], [v]))
    my_dict.update(res)

A = input()
if A in list(my_dict.keys()):
    print(list(my_dict.values())[list(my_dict.keys()).index(A)])
elif A in list(my_dict.values()):
    print(list(my_dict.keys())[list(my_dict.values()).index(A)])

# print(list(my_dict.keys())[list(my_dict.values()).index(A)])