def func_apply(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def add3(x):
    return x + 3

def mul7(x):
    return x * 7
