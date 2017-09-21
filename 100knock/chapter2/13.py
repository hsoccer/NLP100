f = open("merge.txt", "w")
f1 = open("col1.txt", "r")
f2 = open("col2.txt", "r")

lines1 = f1.readlines()
lines2 = f2.readlines()

for line1, line2 in zip(lines1, lines2):
    f.write(line1[:-1] + "\t" + line2)

f.close()
f1.close()
f2.close()
