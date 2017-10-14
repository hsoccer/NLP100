import pickle
import pandas as pd
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

df = pd.DataFrame(columns=["frequency"])

for i in range(10):
    word = words[i]
    count = count_map[word]
    freq = count / num_words
    df.loc[word] = freq

df.plot(kind="bar", width=0.8)
plt.show()
