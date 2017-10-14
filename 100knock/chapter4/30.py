import MeCab
import pickle

drct = "./out/neko.txt.mecab"

f = open(drct, "r")

line = f.readline()
analysis = []
sentence = []

while line:
    if "EOS" in line:
        analysis.append(sentence)
        sentence = []
    else:
        try:
            surface, all_features = line.split()
        except ValueError:
            all_fetures = line.split()
        feature = all_features.split(",")
        base = feature[6]
        pos = feature[0]
        pos1 = feature[1]
        sentence.append({"surface": surface, "base": base, "pos": pos, "pos1": pos1})
    line = f.readline()

f.close()

with open("./out/analysis_map.dump", "wb") as fout:
    pickle.dump(analysis, fout)
