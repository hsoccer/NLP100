import pickle
import re

drct = "./out/basic_info.dump"
dout = "./out/without_emphasis.txt"

f = open(drct, "rb")
dic = pickle.load(f)

fout = open(dout, "w")

for key, value in dic.items():
    name = re.search("^(.*?)\'{1,3}(.*?)\'{1,3}(.*?)$", value)
    if name is None:
        fout.write(key + ":" + value + "\n")
    else:
        fout.write(key + ":" + name.group(1) + name.group(2) + name.group(3) + "\n")

f.close()
fout.close()
