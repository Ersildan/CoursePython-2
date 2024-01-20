# Создам пустой словарь
my_dict = {}

# Создаём 1й цикл для строк, разбивая на ключи и значения, затем обновляем словарь my_dict
for _ in range(int(input())):
    k, v = input().split(': ')
    res = dict(zip([k.lower()], [v]))
    my_dict.update(res)

# Создаеём 2й цикл для строк, в которых ищем ключи для словаря my_dict
for _ in range(int(input())):
    key = input()
    print(my_dict.setdefault(key.lower(), 'Не найдено'))
