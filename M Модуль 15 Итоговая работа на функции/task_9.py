def add3(x):
    return x + 3


def mul7(x):
    return x * 7

def compose(f, g):
    return lambda x: f(g(x))
