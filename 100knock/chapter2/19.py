f = open("hightemp.txt", "r")
lines = f.readlines()

words_lst = [line.split("\t") for line in lines]
dic = {}

for words in words_lst:
    if words[0] in dic:
        dic[words[0]] += 1
    else:
        dic[words[0]] = 1

sorted_words_lst = sorted(words_lst, key=lambda elem: -dic[elem[0]])

res = []

for lst in sorted_words_lst:
    res.append(lst[0])

for elem in res:
    if dic[elem] > 0:
        print(elem)
        dic[elem] = 0

f.close()
