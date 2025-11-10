#AB 1st Dictionaries notes
person = {
    #key:value
    "name": "Xavier",
    "age": 22,
    "job": "Maverick",
    "siblings": ["Alex","Katie","Andrew","Vienna","Tia","Treyson","Jake"]
}
person_two = {
    "name": "Jake",
    "age": 21,
    "job": "NEET",
    "siblings": ["Alex","Katie","Andrew","Vienna","Tia","Treyson","Xavier"]
}
print(person["name"])
print(person.keys())
for key in person.keys():
    if key == "sibling":
        for name in key:
            print(f"{person['name']} has siblings named {name}")
    else:
        print(f"{key} is {person[key]}")

print(person_two.values())
person_two["age"] -= 1
print(person_two.items())
person_two["age"] -= 1
person_two["SO"] = "Carry"
print(person_two.items())