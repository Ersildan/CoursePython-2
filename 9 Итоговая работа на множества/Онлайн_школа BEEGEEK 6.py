m = int(input())
print(*sorted(set.intersection(*({input() for _ in range(int(input()))} for _ in range(m)))), sep="\n")
