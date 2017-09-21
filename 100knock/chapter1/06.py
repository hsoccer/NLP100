def n_gram(seq, n):
    res = []
    for i in range(len(seq)):
        try:
            ngram = seq[i: i+n]
            res.append(ngram)
        except IndexError:
            break
    return res

x = set(n_gram("paraparaparadise", 2))
y = set(n_gram("paragraph", 2))

print(x | y)
print(x & y)
print(x - y)

print("se" in x)
print("se" in y)
