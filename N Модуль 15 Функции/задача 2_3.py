def count_args(*args):
    return len(args)


def sq_sum(*args):
    lst = [i**2 for i in args]
    return sum(lst)
