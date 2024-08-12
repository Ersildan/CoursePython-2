with open("goats.txt") as txt, open("answer.txt", "w") as file:
    s = txt.readlines()
    s = s[s.index("GOATS\n") + 1:]
    for i in sorted(set(s)):
        if s.count(i) / len(s) > 0.07:
            file.write(i)
