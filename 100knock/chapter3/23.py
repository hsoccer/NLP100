import re

drct = "./out/UK.txt"
dout = "./out/section.txt"

f = open(drct, "r")
fout = open(dout, "w")

lines = f.readlines()

for line in lines:
    section = re.search("^=+\s*(.*?)\s*=+$", line)
    if section is not None:
        count = str(line.count("=") // 2 - 1)
        name = section.group(1)
        fout.write(name + " " + count + "\n")

f.close()
fout.close()
