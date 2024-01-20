s = {i for i in input().split()}
s_ = {i for i in input().split()}
print(*sorted(s | s_))
