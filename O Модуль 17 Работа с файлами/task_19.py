with open('class_scores.txt', 'r') as f_1:
    with open('new_scores.txt', 'w') as f_2:
        lst = list(map(str.strip, f_1.readlines()))
        for line in lst:
            s = line.split()
            s1 = s[0]
            s2 = str(int(s[1])+5)
            if int(s2) > 100:
                s2 = str(100)
            f_2.write(f'{s1} {s2}' + "\n")
