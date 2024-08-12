def concat(*args, sep=' '):
    return f"{sep}".join(list(map(str, args)))
