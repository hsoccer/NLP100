drct = "./out/UK.txt"
dout = "./out/noisy_category.txt"

f = open(drct, "r")
fout = open(dout, "w")
lines = f.readlines()

for line in lines:
    if "Category" in line:
        fout.write(line)

f.close()
fout.close()
