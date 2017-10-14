import re

drct = "./out/without_emphasis.txt"
dout = "./out/without_link.txt"

f = open(drct, "r")
fout = open(dout, "w")

lines = f.readlines()

for line in lines:
    without_link = re.sub("\[{2}([^\|\]]+?\|)*(.+?)\]{2}", "\\2", line)
    fout.write(without_link)

f.close()
fout.close()
