s = input()
with open(s, 'r', encoding='utf-8') as f:
    lst = list(map(str.rstrip, f.readlines()))
    print(*lst[-10:], sep='\n')
