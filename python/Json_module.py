import json
data ='{"var1":"Sudarshan","var2":88}'
print(data)

parsed = json.loads(data)
print(parsed)

data2 = {
    "name":"Sudarshan",
    "languages":['java','python','javascript'],
    "games":['Cricket',200],
    "isbad": False
}
jscomp = json.dumps(data2)
print(jscomp)