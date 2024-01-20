import random

length = int(input())
alf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alf = ",".join(alf).split(',')
for _ in range(length):
    print(random.choice(alf), end='')
