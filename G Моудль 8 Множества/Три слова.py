word_1, word_2, word_3 = map(str, input().split())
w, w1, w2 = [], [], []
for i in range(len(word_1)):
    w.append(word_1[i])
    w1.append(word_2[i])
    w2.append(word_3[i])
print(['NO', 'YES'][sorted(w) == sorted(w1) and sorted(w2) == sorted(w1) and sorted(w) == sorted(w2)])
