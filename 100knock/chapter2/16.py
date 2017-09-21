import sys

N = int(sys.argv[1])

f = open("hightemp.txt", "r")
lines = f.readlines()

length = len(lines)

num = length // N
remainder = length % N

less = N - remainder
more = remainder

start = 0

for i in range(N):
    fout = open("fout{}".format(i), "w")
    if i <= more - 1:
        for j in range(start, start+num+1):
            fout.write(lines[j])
        start += num + 1
    else:
        for j in range(start, start+num):
            fout.write(lines[j])
        start += num
    fout.close()

f.close()
