import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

drct = "./out/analysis_map.dump"

with open(drct, "rb") as f:
    analysis_map = pickle.load(f)

count_map = {}
num_words = 0

for sentence in analysis_map:
    for mapping in sentence:
        num_words += 1
        try:
            count_map[mapping["surface"]] += 1
        except KeyError:
            count_map[mapping["surface"]] = 1

words = list(count_map.keys())
words.sort(key=lambda key: -count_map[key])

freq = []

for word in words:
    count = count_map[word]
    freq.append(count / num_words)

x = list(range(1, 1+len(words)))
y = freq

plt.xscale("log")
plt.yscale("log")

plt.scatter(x, y)

plt.show()
