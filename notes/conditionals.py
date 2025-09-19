#AB 1st Conditionals Notes
player_hp = 20
player_attack = 2
player_damage = 5
player_defense = 5

monster_hp = 15
monster_attack = 3
monster_damage = 10
monster_defense = 2

import random

hit_roll = random.randint(1,20) + player_attack
damage_roll = random.randint(1,8) + player_damage
if hit_roll == 20:
    print("You got a crit! That means you get to roll for damage twice!")
    damage_roll = random.randint(1,8) + player_damage
    print(f"You did {damage_roll-monster_defense} damage.")
    monster_hp -= (damage_roll-monster_defense)
elif hit_roll == 1:
    print("You rolle acritical faliure! Now the monster gets to attack you!")
    damage_roll = random.randint(1,12) + monster_damage
    player_hp -= (damage_roll - player_defense)
    print(f"the monster rolled {damage_roll}, you hp is now {player_hp}.")
elif hit_roll >= 12:
    print("You hit! Roll for damage!")
    damage_roll = random.randint(1,8) + player_damage
    if damage_roll > monster_defense:
        print(f"You did {damage_roll-monster_defense} damage.")
        monster_hp -= (damage_roll-monster_defense)
    else:
        print("You did no damage.")
else:
    print("You missed.")

print("Your turn is over")

if monster_hp > 0:
    attack_roll = random.randint(1,20) + monster_attack


 