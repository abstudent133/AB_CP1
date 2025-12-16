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


def reset_game():
    perry = {
        "health": 30,
        "attack": 5,
        "strength": 0,
        "agility": 0,
        "stealth": 0
    }
    gadgets = []
    visited = set()
    return perry, gadgets, visited



def combat(player_health, strength, attack, enemy):
    if enemy == "norm":
        enemy_health, enemy_attack = 25, 5
    elif enemy == "doof":
        enemy_health, enemy_attack = 40, 10
    elif enemy == "weakened doof":
        enemy_health, enemy_attack = 30, 7

    while player_health > 0 and enemy_health > 0:
        choice = input("""Cobat Choices:
                       1. Normal Attack
                       2. Double attack(you lose 7 health)
                       Input the number here: """)
        if choice == "1":
            enemy_health -= attack + strength
        elif choice == "2":
            enemy_health -= attack*2 + strength
            player_health -= 7
            
        if enemy_health <= 0:
            return player_health, "player"
        player_health -= enemy_attack
        

    return player_health, "enemy"


def health_change(perry, change):
    perry["health"] += change
    perry["health"] = max(0, min(45, perry["health"]))


def pick_up_item(item, gadgets):
    if item not in gadgets:
        gadgets.append(item)


def room_1(perry,gadgets, visited):
    # [health, stealth, strength, money]
    result = [0, 0, 0, 0]

    if "room1" in visited and "money" in gadgets:
        return result

    choice = input("1 Leave | 2 Sneak for money | 3 Run for money: ")

    if choice == "2":
        result[1] = 1
        result[3] = 1
    elif choice == "3":
        if perry["strength"] > 0 or random.randint(1, 2) == 1:
            result[2] = 1
            result[3] = 1
        else:
            result[0] = -5

    visited.add("room1")
    return result


def room_2(perry, gadgets, visited):
    # [health_change, keycard]
    result = [0, 0]

    if "room2" in visited and "keycard" in gadgets:
        return result

    choice = input("1 Sneak | 2 Fight Norm: ")

    if choice == "1" and perry["stealth"] > 0:
        result[1] = 1
    else:
        new_health, winner = combat(
            perry["health"], perry["strength"], perry["attack"], "norm"
        )
        result[0] = new_health - perry["health"]
        if winner == "player":
            result[1] = 1

    visited.add("room2")
    return result


def room_3(gadgets, visited):
    # [agility, jammer]
    if "room3" in visited and "signal jammer" in gadgets:
        return [0, 0]
    elif "room3" in visited:
        if "translator" in gadgets:
            return [1, 1]
        return [0, 0]
    else:
        visited.add("room3")
        if "translator" in gadgets:
            return [1, 1]
        return [0, 0]
    
def room_4(gadgets, visited):
    # [access]
    if "room4" in visited:
        return [0]

    if "flashlight" in gadgets:
        visited.add("room4")
        return [1]
    return [0]


def room_5(perry, gadgets, visited):
    # [health, flashlight, spent_money]
    result = [0, 0, False]

    if "room5" in visited and "flashlight" in gadgets:
        return result

    choice = input("1 Eat | 2 Steal flashlight: ")

    if choice == "1" and "money" in gadgets:
        result[0] = 15
        result[2] = True
    elif choice == "2" and perry["stealth"] > 0:
        result[1] = 1

    visited.add("room5")
    return result


def room_6(perry, gadgets, visited):
    # [hideout id]
    if "room6" in visited and "hideout id" in gadgets:
        return [0]

    visited.add("room6")
    return [1] if perry["strength"] > 0 else [0]


def room_7(perry, gadgets, visited):
    # [inator weakened]
    if "room7" in visited and "signal jammer" not in gadgets:
        return [0]

    visited.add("room7")
    return [1] if "signal jammer" in gadgets and perry["agility"] > 0 else [0]


def room_8(gadgets, visited):
    # [translator]
    if "room8" in visited and "translator" in gadgets:
        return [0]

    visited.add("room8")
    return [1] if "hideout id" in gadgets else [0]


def room_9(perry, gadgets):
    # [health_change, victory]
    if "evil inc access" not in gadgets:
        print("You can't reach Evil Inc yet. Find tunnel access.")
        return [0, 0]

    enemy = "weakened doof" if "inator weakened" in gadgets else "doof"
    new_health, winner = combat(
        perry["health"], perry["strength"], perry["attack"], enemy
    )

    return [new_health - perry["health"], 1 if winner == "player" else 0]



print("""
MISSION BRIEFING:
Dr. Doofenshmirtz is attempting to control every pet in the Tri-State Area.
You are Agent P — Perry the Platypus.
Explore locations, gather gadgets, improve your stats,
and stop Doof before it's too late.
""")

while True:
    perry, gadgets, visited = reset_game()

    while True:
        print("STATUS")
        print(perry)
        print("Gadgets:", gadgets)
        print("""
        1. Fletcher Yard
        2. Danville Park
        3. City Hall
        4. Subway Tunnels
        5. Slushy Burger
        6. Waste Recycling Plant
        7. Water Tower
        8. Alleyway Hideout
        9. Doofenshmirz Evil Inc.""")

        choice = input("Choose a room (1-9): ")

        if choice == "1":
            print("""ROOM 1 — Fletcher Yard.
                    The goal of this room is to get money that may be used in a later room. You can either use 
                  steath or strength to get this money or you can leave.""")
            r = room_1(perry, gadgets, visited)
            health_change(perry, r[0])
            perry["stealth"] += r[1]
            perry["strength"] += r[2]
            if r[3]: pick_up_item("money", gadgets)

        elif choice == "2":
            print("""ROOM 2 — Danville Park
                  In this room you have to get the key card from Norm Bot. You can try to steal it if you have at least one 
                  stealth point or you can fight Norm bot.""")
            r = room_2(perry, gadgets, visited)
            health_change(perry, r[0])
            if r[1]: pick_up_item("keycard", gadgets)

        elif choice == "3":
            print("""ROOM 3 — City Hall
                  In this room you have to get the signal jammer form the mayor to use later but you need the platypus
                  translator.""")
            r = room_3(gadgets, visited)
            perry["agility"] += r[0]
            if r[1]: pick_up_item("signal jammer", gadgets)

        elif choice == "4":
            print("""ROOM 4 — Subway Tunnels
                  This is the only way to get to Doofenshmirz Evil Inc. but to enter you need a flashlight.""")
            r = room_4(gadgets, visited)
            if r[0]: pick_up_item("evil inc access", gadgets)

        elif choice == "5":
            print("""ROOM 5 — Slushy Burger
                  In this room you can buy a burger to gain your health back or you could steal a flashlight.""")
            r = room_5(perry, gadgets, visited)
            health_change(perry, r[0])
            if r[2] and "money" in gadgets:
                gadgets.remove("money")
            if r[1]: pick_up_item("flashlight", gadgets)

        elif choice == "6":
            print("""ROOM 6 — Recycling Plant
                  In this room you need to get the hideout ID to open the door to your hideout because you lost it here 
                  yesterday when you fought Doofenshmirz.""")
            r = room_6(perry, gadgets, visited)
            if r[0]: pick_up_item("hideout id", gadgets)

        elif choice == "7":
            print("""ROOM 7 — Water Tower
                  The singal enhancer for Doof's inator is on top of this tower. You need to scale it, if you have at 
                  least 1 agility point, to weaken the intaor.""")
            r = room_7(perry, gadgets, visited)
            if r[0]: pick_up_item("inator weakened", gadgets)

        elif choice == "8":
            print("""ROOM 8 — Alleyway Hideout
                  For this room you need the ID and here is where you can get the platypus translator to talk to the
                  mayor.""")
            r = room_8(gadgets, visited)
            if r[0]: pick_up_item("translator", gadgets)

        elif choice == "9":
            print("""ROOM 9 — Doofenshmirtz Evil Inc.
                  This is the final boss. Good luck.""")
            r = room_9(perry, gadgets)
            health_change(perry, r[0])
            if r[1]:
                print("MISSION SUCCESS! The Tri-State Area is safe.")
                break

        else:
            print("Invalid choice.")

        if perry["health"] <= 0:
            print("MISSION FAILED. Perry has fallen.")
            break

    replay = input("Play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing!")
        break