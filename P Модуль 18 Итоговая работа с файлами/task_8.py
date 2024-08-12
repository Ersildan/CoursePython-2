with open(input(), 'r', encoding='utf-8') as f:
    s = f.readlines()
    flag = True
    for i in range(len(s)):
        if s[i][:4] == 'def ' and s[i-1][0] != '#':
            print(s[i][4:s[i].find('(')])
            flag = False
    if flag:
        print('Best Programming Team')