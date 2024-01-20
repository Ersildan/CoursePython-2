poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
lst = list(poet_data)
lst[2] = 'Москва'
poet_data = tuple(lst)

print(poet_data)
