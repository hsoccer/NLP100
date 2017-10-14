import json

drct = "./out/jawiki-country.json"
dout = ".out/UK.txt"

f = open(drct, "r")
fout = open(dout, "w")

lines = f1.readlines()

for line in lines:
    data = json.loads(line)
    if data["title"] == "イギリス":
        fout.write(data["text"])
        break

f.close()
fout.close()
