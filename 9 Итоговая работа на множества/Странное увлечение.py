a = set(input().split())
b = set(input().split())
print(*sorted(a & b, reverse = True, key=int) if len(a & b) > 0 else ('BAD DAY',))
