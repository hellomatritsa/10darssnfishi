import json
###1-shart

# with open("ustoz.json") as ptr:
#     data=json.load(ptr)

# for i in data["branches"]:
#     print(i["name"])   


###2-shart

with open("ustoz.json") as ptr:
    data=json.load(ptr)

for i in data["branches"]:
    for x in i["teachers"]:
        if x["subject"] == "Python":
            print(f"{x["name"]} {i["name"]} {x["experience"]}")

    
        