with open('numbers.txt') as numb:
    languages = list(map(str.strip, numb.readlines()))
    for line in languages:
        print(sum([int(i) for i in line.split()]))

