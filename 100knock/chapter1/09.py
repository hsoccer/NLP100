import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split(" ")
shuffle = s[1: -1]
random.shuffle(shuffle)
res = [s[0]] + shuffle + [s[-1]]
print(" ".join(res))
