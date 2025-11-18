#AB *args and *kwargs notes


"""def hello(name="Anna",age=14):
    return f"hello {name}! You are {age}"

print(hello())
print(hello("Xaveir"))
print(hello("Vienna"))
print(hello(age=37))"""

def hello(*names,**kwargs):
    print(type(names))

    for n in names:
        print(f"Hello {n} {kwargs['last_name']}!")
    
hello("Anna","Kailyn","Lauren","Danielle","Jason",last_name = "Bangerter",dad = "James",mom = "Nicole")


def full_names(age,**names):
    if 'middle' in names.keys():
        return f"{names['first']} {names['middle']} {names['last']} is {age}"
    else:
        return f"{names['first']} {names['last']} is {age}"
    
print(full_names(age="???",first="Koro",last='Sensei'))
print(full_names(age="So old",first="Albus",middle="Brian",last="Dumbuldore"))


def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum+= f"{story['name']} is the main character of this story."
    if "place" in story.keys():
        sum+= f"The story takes place in {story['place']}."
    if "conflict" in story.keys():
        sum+= f"The problem is {story['conflict']}."
    return sum

print(summary(name = "Luke Skywalker",place = "Galaxy far far away"))
print(summary(name = "Harry Potter",conflict = "Evil wizard wants to kill him."))
