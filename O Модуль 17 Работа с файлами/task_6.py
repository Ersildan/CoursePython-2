file = open('prices.txt')
total = 0
for line in file:
    s = line.split('\t')
    total += int(s[1]) * int(s[2])
print(total)
file.close()
