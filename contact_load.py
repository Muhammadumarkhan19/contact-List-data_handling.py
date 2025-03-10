import json

with open("contacts.json", "r") as file:
    data = json.load(file) 

print(data)
print(data["ali"]["Phone"]) 
print(data["umar"]["Email"])  
