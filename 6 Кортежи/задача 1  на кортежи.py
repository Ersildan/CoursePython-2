tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
lst = []
for i in range(len(tuples)):
  if len(tuples[i]) != 0:
    a = list(tuples[i])
    a[-1] = 100
    tuples[i] = tuple(a)
    lst.append(tuples[i])
print(lst)
