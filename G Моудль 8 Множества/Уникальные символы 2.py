n = int(input())
symbols = set()

for _ in range(n):
    for c in input().lower():
        symbols.add(c)

print(len(symbols))