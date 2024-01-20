def chunked(n):
    res = []
    for i in range(0,len(s),n):
        res.append(s[i:i+n])
    return res


s = input().split()
n = int(input())
print(chunked(n))
