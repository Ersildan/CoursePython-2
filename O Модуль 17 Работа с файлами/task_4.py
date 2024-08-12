name_file = open('numbers.txt', 'r')
print(sum(list(map(int, name_file.readlines()))))
name_file.close()

