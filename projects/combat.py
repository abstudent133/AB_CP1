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

def player(attack, monster_defense):
        global monster_health
        monster_damage = attack - monster_defense
        if monster_damage > 0:
                monster_health -= monster_damage
        else:
                monster_damage = 0  
        return monster_health

def monster(current_attack):
        global health
        damage = current_attack - defense
        if damage > 0:
                health -= damage
        else:
                damage = 0  
        return health


print("This is a combat game. You are a fighter who has to defeat a monster. But first, you must choose what fighter you will be.")
print("You must choose between a Wizard(1), a Knight(2), and a Rouge(3).")
fighter = int(input("Please enter the number of the fighter you want to be: "))
print("Great. Here are your stats:")
if fighter == 1:
        health = 30
        defense = 15
        attack = random.randint(1,20) + 3
        print("Health = 30")
        print("Defense = 15")
        print("Attack = D20 + 3")
elif fighter == 2:
        health = 30
        defense = 13
        attack = random.randint(1,20) + 4
        print("Health = 30")
        print("Defense = 13")
        print("Attack = D20 + 4")
elif fighter == 3:
        health = 25
        defense = 14
        attack = random.randint(1,20) + 6
        print("Health = 25")
        print("Defense = 14")
        print("Attack = D20 + 6")
else:
        print("Sorry. That was an invalid answer.")

print("You are being attacked by a Dark Gnome!")
if coin == 1:
        print("You go first!")
        turn = "player"
elif coin == 2:
        print("The monster goes first.")
        turn = "monster"
        
while health > 0 and monster_health > 0:  
        if turn == "player":
                print("These are your combat options:")
                print("1.Do attack")
                print("2.Double attack but take damage")
                print("3.Get 9 health")
                print("4.Run away(you might not get away)")
                action = int(input("Put the number of the action  you would like to complete: "))
                if action == 1:
                        player(attack, monster_defense)
                        if attack > monster_defense:
                                print("You hit!")
                                print(f"This is the monster's health now: {monster_health}")
                                turn = "monster"
                        elif attack <= monster_defense:
                                print("You missed.")
                                turn = "monster"
                elif action == 2:
                        player(attack*2, monster_defense)
                        if attack > monster_defense:
                                health -= 15
                                print("You hit!")
                                print(f"This is the monster's health now: {monster_health}")
                                print(f"This is your health now: {health}")
                                turn = "monster"
                        elif attack <= monster_defense:
                                health -= 15
                                print("You missed.")
                                print(f"This is your health now: {health}")
                                turn = "monster"
                elif action == 3:
                        health += 9
                        print(f"This is your health now: {health}")
                        turn = "monster"
                elif action == 4:
                        print("You run. Did you get away?")
                        choice = random.randint(1,2)
                        if choice == 1:
                                print("You got away!")
                                print("Game over. You win!")
                                break
                        elif choice == 2:
                                print("You got caught.")
                                print("Sorry game over. You lose.")
                                break
        elif turn == "monster":
                print("The monster has attacked.")
                current_attack = random.randint(1,20) + 3
                monster(current_attack)
                print(f"This is your health now: {health}")
                turn = "player"               

        if health <= 0 or monster_health <= 0:
                if health <= 0:
                        print("You lose.")
                        break
                elif monster_health <= 0:
                        print("You win!")
                        break

        

        


