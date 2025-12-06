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
# Checks for special items or higher stats that could affect damage.
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
