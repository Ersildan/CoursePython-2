with open('grades.txt') as f:
    print(sum(1 for i in f.readlines() if all([int(j) >= 65 for j in i.split(' ')[1:]])))