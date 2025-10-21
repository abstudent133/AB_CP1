#AB 1st function notes
#set variables first then define functions

def add(x,y):
    #print(f"{x} + {y} = {x+y}")
    return x+y#this replaces

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]

    return initials

#add(5,5)#this when called
total = add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")
x = 0
while x < add(3,9):
    print("duck")
    x+=1
print("Goose!")
add(3,9)