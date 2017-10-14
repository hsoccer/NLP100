import re
import pickle

drct = "./out/UK.txt"
dout = "./out/basic_info.dump"

f = open(drct, "r")
fout = open(dout, "wb")

text = f.read()
lines = re.split("\n(\||\})", text)

dic = {}

for line in lines:
    expr = re.search("(.*?)\s=\s(.*?)$", line, re.S)
    if expr is not None:
        dic[expr.group(1)] = expr.group(2)

pickle.dump(dic, fout)

f.close()
fout.close()
