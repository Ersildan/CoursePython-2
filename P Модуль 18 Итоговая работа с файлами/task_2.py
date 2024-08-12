with open('ledger.txt') as inp:
    print('${}'.format(sum(map(lambda x: int(x[1::]), inp))))