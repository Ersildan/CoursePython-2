names = {}
rights= {'W': 'write', 'R': 'read', 'X': 'execute'}

for _ in range(int(input())):
    s = input().split()
    names[s[0]] = [rights[i] for i in s[1:]]

for _ in range(int(input())):
    comm, n = input().split()
    print('OK' if comm in names[n] else 'Access denied')
