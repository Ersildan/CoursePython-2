with open('population.txt', 'r') as pip:
    lst = list(map(str.strip, pip.readlines()))
    my_dict = dict()
    for line in lst:
        k, v = line.split('\t')
        my_dict.update(dict(zip([k],[v])))
for k, v in my_dict.items():
    if k[0] == 'G' and int(v) > 500000:
        print(f'{k}')
