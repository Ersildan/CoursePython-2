with open('logfile.txt') as fin, open('output.txt', 'w') as fout:
    for line in fin:
        b, e = [int(h)*60 + int(m) for t in line.split(', ')[1:] for h, m in [t.split(':')]]
        if e - b >= 60:
            fout.write(line.split(', ')[0] + '\n')