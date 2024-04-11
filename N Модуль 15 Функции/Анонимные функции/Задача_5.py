t = lambda a: True if a.replace('-', '').replace('.', '', 1).isdigit() and a.count('.') < 2 and float(a) >= 0 else False
