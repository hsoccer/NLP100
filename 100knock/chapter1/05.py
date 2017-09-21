def n_gram(seq, n):
    res = []
    for i in range(len(seq)):
        try:
            ngram = seq[i: i+n]
            res.append(ngram)
        except IndexError:
            break
    return res

s = "I am an NLPer"
print(n_gram(s, 2))
print(n_gram(s.split(" "), 2))
