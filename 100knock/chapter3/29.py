import re
import requests

drct = "./out/without_mediawiki.txt"

f = open(drct, "r")

def search_json(json_file):
    json_dict = {}
    for k, v in json_file.items():
        if isinstance(v, list):
            for e in v:
                json_dict.update(search_json(e))
        elif isinstance(v, dict):
            json_dict.update(search_json(v))
        else:
            json_dict[k] = v
    return json_dict

dic = {}
lines = f.readlines()

for line in lines:
    temp_line = re.search("^(.*?):(.*)", line)
    if temp_line is not None:
        key = temp_line.group(1)
        value = temp_line.group(2)
        dic[key] = value

url = 'https://ja.wikipedia.org/w/api.php'
payload = {
    'action': 'query',
    'titles': 'File:{}'.format(dic['国旗画像']),
    'prop': 'imageinfo',
    'iiprop': 'url',
    'format': 'json'
}

json_file = requests.get(url, params=payload)
json_dict = search_json(json_file.json())
print(json_dict["url"])

f.close()
