import pickle

drct = "./out/analysis_map.dump"

with open(drct, "rb") as f:
    analysis_map = pickle.load(f)

for sentence in analysis_map:
    for i in range(len(sentence)-2):
        if sentence[i]["pos"] == "名詞" and sentence[i+1]["surface"] == "の" and sentence[i+2]["pos"] == "名詞":
            print(sentence[i]["surface"] + sentence[i+1]["surface"] + sentence[i+2]["surface"])
