import pickle

drct = "./out/analysis_map.dump"

with open(drct, "rb") as f:
    analysis_map = pickle.load(f)

count_map = {}

for sentence in analysis_map:
    for mapping in sentence:
        try:
            count_map[mapping["surface"]] += 1
        except KeyError:
            count_map[mapping["surface"]] = 1

words = list(count_map.keys())
words.sort(key=lambda key: -count_map[key])

for word in words:
    print(word)
