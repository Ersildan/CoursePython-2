def bumer(s_):
    count = 0
    for i in range(len(s_)):
        count += int(s_[i])
    return count

s = sorted([int(_) for _ in input().split()])
s_ = [str(i) for i in s]

print(*sorted(s_, key=bumer))
