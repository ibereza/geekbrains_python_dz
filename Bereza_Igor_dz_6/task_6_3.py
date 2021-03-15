import sys
import json

with open("users.csv", "r", encoding="UTF-8") as f:
    users = f.read().splitlines()

with open("hobby.csv", "r", encoding="UTF-8") as f:
    hobby = f.read().splitlines()

if len(hobby) > len(users):
    sys.exit(1)

users_dict = {}
for i, el in enumerate(users):
    if i < len(hobby):
        users_dict[el.replace(",", " ")] = hobby[i].replace(",", ", ")
    else:
        users_dict[el.replace(",", " ")] = None

with open("users_dictionary.json", "w", encoding="UTF-8") as f:
    json.dump(users_dict, f, ensure_ascii=False)
