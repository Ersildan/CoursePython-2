def mean(*args):
    lst = [i for i in args if type(i) is float or type(i) is int]
    if len(lst) == 0:
        return float(sum(lst))
    else:
        return sum(lst)/len(lst)
