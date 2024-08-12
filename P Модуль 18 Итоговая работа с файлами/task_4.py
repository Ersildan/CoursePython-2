with open('words.txt', 'r', encoding='utf-8') as f:
    lst = list(map(str.rstrip, f.readlines()))
    for line in lst:
        new_lst = line.split()
        max_word = ' '
        LOL = []
        for i in new_lst:
            if len(i) >= len(max_word):
                max_word = i
                LOL.append(max_word)

print(*list(filter(lambda x: len(x) >= len(max_word), LOL)), sep='\n')
