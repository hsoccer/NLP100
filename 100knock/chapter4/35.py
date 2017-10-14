import pickle

drct = "./out/analysis_map.dump"

with open(drct, "rb") as f:
    analysis_map = pickle.load(f)

for sentence in analysis_map:
    it = iter(sentence)
    linked_words = ""
    isLink = False
    while True:
        try:
            word = next(it)
        except StopIteration:
            if linked_words != "" and isLink:
                print(linked_words)
            break
        if word["pos"] != "名詞":
            if linked_words != "" and isLink:
                print(linked_words)
            linked_words = ""
            isLink = False
        else:
            if linked_words != "":
                isLink = True
            linked_words += word["surface"]
