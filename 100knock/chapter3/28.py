import re

drct = "./out/without_link.txt"
dout = "./out/without_mediawiki.txt"

f = open(drct, "r")
fout = open(dout, "w")

#すでに強調と内部リンクは除去してある

lines = f.readlines()

for line in lines:
    line = re.sub("\<.*?\>", "", line) #コメント
    line = re.sub("\[.*?\]", "", line) #外部リンク
    fout.write(line)

f.close()
fout.close()
