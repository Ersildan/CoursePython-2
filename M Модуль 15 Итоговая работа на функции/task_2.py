def pretty_print(data, side='-', delimiter='|'):
    lol = len(f' {delimiter} '.join(map(str, data)))
    return print(f' {side * (lol+2)} ', f"{delimiter} {f' {delimiter} '.join(map(str, data))} {delimiter}", f' {side * (lol+2)} ', sep='\n')


