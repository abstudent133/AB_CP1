#AB 1st Combat Program using Activity Diagram

import random

dice_1 = random.randint(1,20)
dice_2 = random.randint(1,8)
coin = random.randint(1,2)
turn = "none"

health = 0
defense = 0
damage = 0
attack = 0

monster_health = 30
monster_defense = 12
monster_damage = 0
monster_attack = dice_1 + 3

def player(attack, monster_defense):
        monster_damage = attack - monster_defense
        monster_health -= monster_damage
        return monster_health

def monster(monster_attack, defense):
        damage = monster_attack - defense
        health -= damage
        return health

print("This is a combat game. You are a fighter who has to defeat a monster. But first, you must choose what fighter you will be.")
print("You must choose between a Wizard(1), a Knight(2), and a Rouge(3).")
fighter = input("Please enter the number of the fighter you want to be: ")
print("Great. Here are your stats:")
if fighter == 1:
        health = 30
        defense = 15
        attack = dice_1 + 3
        print("Health = 30")
        print("Defense = 15")
        print("Attack = D20 + 3")
elif fighter == 2:
        health = 30
        defense = 13
        attack = dice_1 + 4
        print("Health = 30")
        print("Defense = 13")
        print("Attack = D20 + 4")
elif fighter == 3:
        health = 25
        defense = 14
        attack = dice_1 + 6
        print("Health = 25")
        print("Defense = 14")
        print("Attack = D20 + 6")
else:
        print("Sorry. That was an invalid answer.")

print("You are being attacked by a Dark Gnome!")
if coin == 1:
        print("You go first!")
        turn = "player"
else:
        print("The monster goes first.")
        turn = "monster"
        
        
if turn == "player":
        print("These are your combat options:")
        print("1.Do attack")
        print("2.Double attack but take damage")
        print("3.Get 9 health")
        print("4.Run away(you might not get away)")
        action = input("Put the number of the action  you would like to complete: ")
        if action == 1:
                player(attack, monster_defense)
                if attack > monster_defense:
                        print("You hit!")
                        print(f"This is the monster's health now: {monster_health}")
                elif attack <= monster_defense:
                        print("You missed.")
        elif action == 2:
                player(attack*2, monster_defense)
                if attack > monster_defense:
                        print("You hit!")
                        print(f"This is the monster's health now: {monster_health}")
                        print(f"This is your health now: {health - 3}")
                elif attack <= monster_defense:
                        print("You missed.")
                        print(f"This ")

                
    

