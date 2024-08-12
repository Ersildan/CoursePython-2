file = open('nums.txt')
s = file.read().split()
print(sum(map(int, s)))
file.close()
