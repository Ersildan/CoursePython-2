words = [word.lower().strip('.,;:-?!') for word in input().split()]

print(len(set(words)))
