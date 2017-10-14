import pickle

drct = "./out/analysis_map.dump"

with open(drct, "rb") as f:
    analysis_map = pickle.load(f)

for sentence in analysis_map:
    for mapping in sentence:
        if mapping["pos"] == "動詞":
            print(mapping["surface"])
