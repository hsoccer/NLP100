f = open("hightemp.txt", "r")
lines = f.readlines()

words_lst = [line.split("\t") for line in lines]
sorted_words_lst = sorted(words_lst, key=lambda elem: -float(elem[2]))

f.close()

fout = open("sorted_hightemp_18.txt", "w")
for lst in sorted_words_lst:
    fout.write("\t".join(lst))

fout.close()
