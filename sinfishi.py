import json
###1-shart

with open("ustoz.json") as ptr:
    data=json.load(ptr)

for i in data["branches"]:
    print(i["name"])   



        