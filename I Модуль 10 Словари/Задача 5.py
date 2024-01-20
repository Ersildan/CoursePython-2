result = {}
lst = [int(i) for i in range(1,16)]
lst_ = [int(i**2) for i in range(1,16)]
result = dict(zip(lst, lst_))
