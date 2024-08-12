with open('lines.txt') as numb:
    s = list(map(str.strip, numb.readlines()))
    lst = []
    for line in s:
        lst.append(len(line))
    maximus = max(lst)
    for line in s:
        if len(line) == maximus:
            print(line)
