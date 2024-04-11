def print_products(*kek, start=0):
    lst = [i for i in kek if type(i) is str and i != '']
    n = len(lst)
    if n != 0:
        for i in range(n):
            print(f'{start+1}) {lst[i]}')
            start += 1
    else:
        print('Нет продуктов')
