n = int(input())

for i in range(n):
    with open(input(), 'r') as r:
        with open('output.txt', 'a') as f:
            print(r.read(), file=f, end='')
