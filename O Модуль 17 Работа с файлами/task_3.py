name_file = open(input(), 'r')
print(list(map(str.strip, name_file.readlines()))[-2])
name_file.close()

