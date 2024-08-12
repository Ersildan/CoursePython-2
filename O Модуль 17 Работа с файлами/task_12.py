with open('file.txt') as t:
    count_letters = 0
    count_words = 0
    count_lines = 0
    text = list(map(str.strip, t.readlines()))
    for line in text:
        count_lines += 1
        count_words += len(line.split())
        for i in line:
            if i.isalpha() == True:
                count_letters += 1
print('Input file contains:')
print(f'{count_letters} letters')
print(f'{count_words} words')
print(f'{count_lines} lines')