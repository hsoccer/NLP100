import re

drct = "./out/noisy_category.txt"
dout = "./out/pure_category.txt"

f = open(drct, "r")
fout = open(dout, "w")

lines = f.readlines()

for line in lines:
    category = re.search("^\[\[Category:(.*?)(\|.*)?\]\]$", line)
    if category is not None:
        fout.write(category.group(1) + "\n")

f.close()
fout.close()
