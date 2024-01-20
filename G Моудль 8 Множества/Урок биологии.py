x = set(range(11))
one = {int(_) for _ in input().split()}
two = {int(_) for _ in input().split()}
tree = {int(_) for _ in input().split()}
print(*sorted(x - one - two - tree))
