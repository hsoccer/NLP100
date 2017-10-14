import re

drct = "./out/UK.txt"
dout = "./out/media_file.txt"

f = open(drct, "r")
fout = open(dout, "w")

lines = f.readlines()

for line in lines:
    media_file = re.search("(ファイル|file):(.*?)\|.*?$", line, re.IGNORECASE)
    if media_file is not None:
        fout.write(media_file.group(2) + "\n")

f.close()
fout.close()
