import re

drc = "hightemp.txt"
f = open(drc, "r")
text = f.read()
text = text.replace("\t", " ", len(text))
print(text)
f.close()
