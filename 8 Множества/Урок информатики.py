uch1 = {int(_) for _ in input().split()}
uch2 = {int(_) for _ in input().split()}
uch3 = {int(_) for _ in input().split()}
print(*sorted(uch1 & uch2 - uch3)[::-1])
