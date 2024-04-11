strings = list(map(int, input().split()))
number = int(input())
lst_degree = [_ for _ in range(len(strings))][::-1]

print(sum(list(map(lambda x, y: x * number ** y, strings, lst_degree))))
