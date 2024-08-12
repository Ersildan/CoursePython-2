import random
with open('random.txt', 'w') as f:
    for _ in range(25):
        print(random.randint(111,777), file=f , sep ='\n')