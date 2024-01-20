data = 'Python для продвинутых!'
data_tuple = tuple(data)
print(data_tuple)

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
lst = list(poet_data)
lst[2] = 'Москва'
poet_data = tuple(lst)

print(poet_data)

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
lst, lst2 = [],[]
for i in range(len(numbers)):
    lst.append((sum(numbers[i]))/len(numbers[i]))
print(lst)

