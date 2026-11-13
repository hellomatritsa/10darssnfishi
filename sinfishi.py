import json
###1-shart

with open("ustoz.json") as ptr:
    data=json.load(ptr)

for i in data["branches"]:
    print(i["name"])   

###2-shart

# with open("ustoz.json") as ptr:
#     data=json.load(ptr)

# for i in data["branches"]:
#     for x in i["teachers"]:
#         if x["subject"] == "Python":
#             print(f"{x["name"]} {i["name"]} {x["experience"]}")

###3-shart

# with open("ustoz.json") as ptr:
#     data=json.load(ptr)

# dct={}
    
# for i in data["branches"]:
#     if i["name"] not in dct:
#         dct[i["name"]]=len(i["students"])
#     else:
#         dct[i["name"]]+=len(i["students"])

# print(dct)

##4-shart

# with open("ustoz.json") as ptr:
#     data=json.load(ptr)

# max_payment = 0
# max_student = {}
# branch_name = ""

# for i in data["branches"]:
#     for x in i["students"]:
#         if x["payment"] > max_payment:
#             max_student = x["name"]
#             max_payment = x["payment"]
#             branch_name = i["name"]

# print("Talaba:", max_student)
# print("Filial:", branch_name)
# print("Payment:", max_payment)

##5-masala

# with open("ustoz.json") as ptr:
#     data=json.load(ptr)

# dct={}

# for i in data["branches"]:
#     for x in i["students"]:
#         if i["name"] not in dct:
#             dct[i["name"]] = 0
#         dct[i["name"]] += x["payment"]

# print(dct)

###6-masala

# with open("ustoz.json") as ptr:
#     data=json.load(ptr)


# for i in data["branches"]:
#     for x in i["teachers"]:
#         if x["experience"] > 5:
#             print(x["name"])

##7-masala

# with open("ustoz.json") as ptr:
#     data=json.load(ptr)

# new=()

# for i in data["branches"]:
#     faqat_python= True

#     for x in i["students"]:
#          if x["course"] != "Python":
#              faqat_python=False
#              break
#     if faqat_python and i["students"]:
#         print(i["name"])
             
            
         

    

    
            



