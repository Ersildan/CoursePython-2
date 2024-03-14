def greet(name, args):
    names = f'Hello, {name}', *args
    return " and ".join(names) + '!'
