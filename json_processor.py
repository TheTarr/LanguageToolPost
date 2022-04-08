import json

path = 'json/short.json'
n = 1117

f = open(path, encoding='utf-8')
for i in range(n):
    line = f.readline()
    d = json.loads(line)
    print(d["text"])