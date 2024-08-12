with open('input.txt', 'r') as f_1:
    with open('output.txt', 'w') as f_2:
        lst = list(map(str.strip, f_1.readlines()))
        for line in lst:
            f_2.write(f'{str(lst.index(line) + 1)}) {line}' + '\n')

