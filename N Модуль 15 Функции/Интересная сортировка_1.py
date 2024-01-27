def bumer(s):
    count = 0
    for i in range(len(s)):
        count += int(s[i])
    return count

s = input().split()

print(*sorted(s,key=bumer))
