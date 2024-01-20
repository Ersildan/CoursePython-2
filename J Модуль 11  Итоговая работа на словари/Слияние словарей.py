def merge(values):
    result = {}
    for i in values:
        for j in i:
            result.setdefault(j, set()).add(i[j])
    return result
