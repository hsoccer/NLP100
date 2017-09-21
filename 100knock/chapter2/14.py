import sys

f = open("hightemp.txt", "r")
lines = f.readlines()

for i in range(int(sys.argv[1])):
    print(lines[i])
f.close()
