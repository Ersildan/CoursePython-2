with open('data.txt') as f:
    languages = list(map(str.strip, f.readlines()))[::-1]
    for line in languages:
        print(line)