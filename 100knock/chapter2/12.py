f = open("hightemp.txt")
f1 = open("col1.txt", "w")
f2 = open("col2.txt", "w")

lines = f.readlines()
for line in lines:
    words = line.split("\t")
    f1.write(words[0] + "\n")
    f2.write(words[1] + "\n")

f.close()
f1.close()
f2.close()
