import re
with open(input()) as inp:
    with open('forbidden_words.txt') as fw:
        lst = fw.read().split()
        text = inp.read()
for i in lst:
    text = re.sub(i,'*' * len(i),text, flags=re.IGNORECASE)
print(text)