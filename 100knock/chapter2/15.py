import sys

f = open("hightemp.txt", "r")
lines = f.readlines()

N = int(sys.argv[1])
length = len(lines)

for i in [_ for _ in range(length-N, length)]:
    print(lines[i])
f.close()
