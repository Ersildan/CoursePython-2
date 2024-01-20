a = [int(i) for i in input().split()]
b = {int(i) for i in input().split()}
if list(sorted(b)) == sorted(a):
    print("YES")
else:
    print('NO')
