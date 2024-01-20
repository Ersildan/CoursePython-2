d = {'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'}
lst = ','.join(input()).split(',')

print(*[d[i]for i in lst], end='', sep='')
