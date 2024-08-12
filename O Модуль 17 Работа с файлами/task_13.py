import random
with open('first_names.txt', 'r') as file_1:
    with open('last_names.txt', 'r') as file_2:
        first_n = list(map(str.strip, file_1.readlines()))
        last_n = list(map(str.strip, file_2.readlines()))
        print(f'{random.choice(first_n)} {random.choice(last_n)}')
        print(f'{random.choice(first_n)} {random.choice(last_n)}')
        print(f'{random.choice(first_n)} {random.choice(last_n)}')

