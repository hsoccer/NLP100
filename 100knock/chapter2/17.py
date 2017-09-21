f = open("hightemp.txt", "r")
lines = f.readlines()

res = []

for line in lines:
    words = line.split("\t")
    res.append(words[0])

print(set(res))

f.close()
