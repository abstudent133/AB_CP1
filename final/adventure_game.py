# AB Text-Based Adventure Game Pseudocode

# Create a dictionary for Perry with his starting health, attack, strength, agility, and stealth.
# Create a dictionary for Doofenshmirtz with health, attack, and inator stats.
# Create a dictionary for Norm with health, attack, and strength.
# Create an empty list to store Perry’s collected gadgets.
# Create an empty list to record rooms that have been visited.
# Create variables to track defeated enemies, collected items, and disabled machines.
# Define a list of the nine Tri-State Area locations Perry can travel to.

# FUNCTIONS
# Function: check_item_in_list
# Checks if a specific gadget or item is in Perry’s inventory.
# Returns true if the item is already collected, false if not.

# Function: update_stats
# Modifies Perry’s stealth, strength, or agility depending on the room or item effects.
# Includes checks to prevent stats from going below zero.
# Returns updated stats.

# Function: update_health
# Increases or decreases Perry’s health.
# Checks if health drops below zero or exceeds maximum.
# Returns updated health.

# Function: combat
# Handles a fight between Perry and an enemy (Norm or Doof).
# Loop until either Perry or the enemy reaches zero health.
# Apply damage based on attacks and stats.
# Return who won the fight and updated health.

# Function: pick_up_item
# Adds an item to Perry’s gadgets list if not already collected.
# Applies any stat bonuses from the item.
# Returns updated inventory and stats.

# Function: room_choice
# Checks which rooms Perry can travel to next.
# Prevents travel to locked or inaccessible rooms.
# Returns the selected room.

# Function: play_again
# Asks the player if they want to restart the mission after win or loss.
# If yes, resets stats, inventory, and visited rooms.
# If no, ends the game.

# ROOM FUNCTIONS
# Room 1 Function: Flynn-Fletcher Backyard
# Checks if the room has been visited.
# If visited, only option is to leave.
# If not visited, Perry can choose to sneak or run.
# If Perry sneaks and stealth is high enough, this leads to gaining money and +1 stealth.
# If Perry runs, random chance may cause him to get caught.
# If caught, losing health and the room visit is recorded as completed.
# Otherwise, successful exit, stats updated, room marked visited.

# Room 2 Function: Danville Park
# Checks if the room has been visited.
# If Perry already has the keycard, only option is to leave.
# If Perry has high enough stats, this leads to stealing the card without fighting.
# Otherwise, combat with Norm occurs (combat function called).
# After fight, if Perry wins, this causes the keycard to be added to gadgets list.
# Room marked as visited.

# Room 3 Function: City Hall
# Checks if the room has been visited.
# If signal jammer already collected, this leads to being able to exit the room.
# If Perry has the platypus translator, this leads to warning Mayor and receiving the signal jammer.
# If not, Perry must leave without the jammer.
# On first visit, Perry gains +1 agility.
# Room marked visited.

# Room 4 Function: Subway Tunnels
# If Perry has flashlight, room is accessible.
# If flashlight missing, this causes him to be blocked.
# If accessible, player can choose to travel to Alleyway Hideout or Doofenshmirtz Evil Inc.
# Room can be revisited multiple times.

# Room 5 Function: Slushy Burger
# Checks if room has been visited.
# If Perry has money, this leads to eating burger and gaining health.
# If Perry tries to steal flashlight, must have stealth level 1.
# If stealth too low, this causes failing and losing health.
# If stealth sufficient, this leads to adding flashlight to gadgets.
# Room marked as visited after first interaction.

# Room 6 Function: Waste Recycling Plant
# Checks if room has been visited.
# If Perry has strength level 1 or higher, this leads to getting ID.
# If strength too low, this causes not being able to get ID yet.
# ID added to gadgets list if collected.
# Room marked as visited.

# Room 7 Function: Water Tower
# Checks if room has been visited.
# If signal jammer collected AND agility level 1+, this leads to disabling booster.
# If not, this causes inability to disable booster yet.
# Room marked as visited.

# Room 8 Function: Alleyway Hideout
# If Perry has ID from Waste Recycling Plant, this leads to being able to enter.
# If no ID, this causes him to be blocked from entering.
# If translator not yet collected, this leads to adding platypus translator to gadgets list.
# Room marked as visited.

# Room 9 Function: Doofenshmirtz Evil Inc.
# Perry must have at least level 1 in strength, agility, and stealth to fight Doof.
# If any stat is missing, this causes inability to fight → return failure.
# If all stats present, this leads to triggering final combat function.
# If Room 7 booster disabled, this leads to Doof being weaker, making battle easier.
# Return battle result and updated stats.

# MAIN LOOP
# Start mission statement: explain Perry’s goal to stop Doofenshmirtz.
# Place Perry in Room 1 and call Room 1 function.
# While Perry has not reached Room 9 and health > 0:
#     Call room_choice to select next room.
#     Call the chosen room’s function.
#     Check if room was visited before and handle appropriately.
#     Update Perry’s stats, health, gadgets, and visited rooms based on room outcomes.
#     If combat occurs, this leads to calling combat function and updating health/stats.
#     Check after each loop: if Perry’s health ≤ 0, this causes mission to fail → break loop.
# Once Room 9 completed:
#     If Perry won final battle, this leads to mission success.
#     If Perry lost, this causes mission failure.
# After mission ends, call play_again function to reset or exit.
import random

perry = {
    "health":30,
    "attack":5,
    "strengh":0,
    "agility":0,
    "stealth":0
}
doof = {
    "health":40,
    "attack":10,
    "inator":{
        "health":20
    }
}
norm = {
    "health":25,
    "attack":5
}
gadgets = []
visited = []
defeated = []
tri_state_area = ["Fletcher Backyard","Danville Park","City Hall","Subway Tunnels","Slushy Burger","Waste Recycling Plant","Water Tower","Alleyway Hideout","Doofenshmirz Evil Inc."]

def check_list(item,*arg):
    if item in arg:
        return True
    else:
        return False

def update_stats(name,change,**kwarg):
    if name in kwarg.keys():
        name = name + change
        if name >= 0:
            pass
        else:
            name = 0
        return name
    else:
        return "The item you want to change isn't in the dictionary."

def update_health(health,change):
    health = health + change
    if health > 45:
        health = 45
    elif health < 0:
        health = 0
    return health

def combat(p_health,enemy_health,attack,enemy_attack):
    winner = ""
    turn = "perry"
    while p_health > 0 and enemy_health > 0:
        if turn == "perry":
            enemy_health -= attack
        elif turn == "enemy":
            p_health -= enemy_attack
    if p_health <= 0:
        winner = "enemy"
    elif enemy_health <= 0:
        winner = "perry" 
    return winner

def pick_up_item(item,attack,*gadget):
    if item in gadget:
        in_list = True
        return in_list
    else:
        gadget.append(item)
        attack += 1
        return gadget and attack

def room_choice(*gadget):
    if 'flashlight' in gadget:
        choice = input(f"You have a choice of any of the nine rooms including {tri_state_area}. What is your choice: ")
        choice = choice.lower().strip()
    else:
        choice = input("You have a choice of 7 of the nine rooms including the Fletcher Yard, Danville, City Hall, Slushy Burger, Waste Recycling Plant, Water Tower, Alleyway Hideout. What is your choice: ")
        choice = choice.lower().strip()
    return choice

def play_again():
    choice = input("Would you like to play again? If yes put 1, if no put 2. Input here: ")
    if choice == "1":
        play = True
    else:
        play = False
    return play

def room_1(strength,*gadget,**visited):
#result = [health,stealth,strength,attack]
    result = [0,0,0,0,0,0]
    if "room 1" in visited.keys() and 'money' in gadget:
        return "You have already been in this room. You have to leave."
    else:
        choice = input("You have the choice to get the money from the Fletchers. This item may be used in a later room. If you choose to take the money you can either run and get it and gain a strength point and 1 to your attack but there is a 50 percent chance that you get caught unless you already have a strength point or you could sneak and gain a stealth point. If you would like to just leave this room input 1. If you would like to use stealth to get the money input 2 and if you would like to run for the money input 3. Please input your choice here: ")
        if choice == "1":
            return result
        elif choice == "2":
            result[1] += 1
            result[4] = 1
            result[5] = 1
            return result
        elif choice == "3" and strength >= 1:
            result[2] += 1
            result[3] += 1
            result[5] = 1
            return result
        elif choice == "3" and strength < 1:
            dice = random.randint(1,2)
            if dice == 1:
                result[2] += 1
                result[3] += 1
                result[4] = 1
                result[5] = 1
                return result
            else:
                result[0] -= 45
                return result
# Room 2 Function: Danville Park
# Checks if the room has been visited.
# If Perry already has the keycard, only option is to leave.
# If Perry has high enough stats, this leads to stealing the card without fighting.
# Otherwise, combat with Norm occurs (combat function called).
# After fight, if Perry wins, this causes the keycard to be added to gadgets list.
# Room marked as visited.
def room_2(stealth,*gadget,**visited): 
#result = [health,gadget] 
    result = [0]
    if 'room 2' in visited.keys() and 'keycard' in gadget:
        return "You've already been here. You have to leave."   
    else:
        choice = input("You are in Danville Park. The goal is to get the keycard from Norm bot so you can enter Doofenshmirz Evil Inc. You can either sneak and steal it if you have at least 1 stealth point or you are going to have to fight Norm for it. Would you like to try and sneak past or would you like to fight directly. If the first input 1. If the second input 2. Input here:")
        if choice == '1' and stealth >= 1:



            
