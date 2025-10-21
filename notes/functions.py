#AB 1st function notes
#set variables first then define functions

player_health = 100
monster_health = 100
def damage(amount, turn):
    if turn == "player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount
monster_health, player_health = damage(10, "player")
print(f"Monster Healthe: {monster_health}")
print(f"Player Health: {player_health}")

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
print(initials("Anna Bangerter"))
print(f"a = {ord("a")}")
print(f"98 = {chr(98)}")