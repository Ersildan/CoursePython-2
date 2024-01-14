uch1 = {int(_) for _ in input().split()}
uch2 = {int(_) for _ in input().split()}
uch3 = {int(_) for _ in input().split()}
print(*(sorted((uch3-uch2-uch1)))[::-1])
