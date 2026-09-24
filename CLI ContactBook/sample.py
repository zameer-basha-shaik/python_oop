import json

with open("CLI ContactBook/contacts.json", mode= "r") as f:
    data = json.load( f)

data["Shanmuk"] = {"name": "Shanmuk", "Email": "", "Phone": "1234567780"}

with open("CLI ContactBook/contacts.json", mode = 'w') as f:
    json.dump(data, f, indent=2)

