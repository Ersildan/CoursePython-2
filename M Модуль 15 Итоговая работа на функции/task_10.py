def arithmetic_operation(operation):
    d = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x/y}
    return d[operation]

