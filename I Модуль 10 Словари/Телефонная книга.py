d = {}
for _ in range(int(input())):
    number, name = input().split()
    d.setdefault(name,[]).append(number)
for _ in range(int(input())):
    print(*d.get(input().title(), ['абонент не найден']))