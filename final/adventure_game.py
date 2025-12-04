#AB 1st Text Based Adventure Game
#import random

#DICTIONARIES
#Player ditionary
#player has perry's health, stealth, agility,strength, and basic attack
#Doof dictionary
#doof has Doofenshmirz's health, attack, and inator stats
#   }
#Norm dictionary
#norm has norm's health and basic attack

#Variables
#gadgets is a list of gadgets perry has attained
#visited rooms is a list of the rooms that were visited

#FUNCTIONS
#Room 1 funtion(Fletcher Yard)
#The goal of this funtion is to get money from the Fletchers and gain some stealth or strength
#For this function the parameters is the gadgets list, kwarg of perry's stats(health,stealth,strength), visited rooms list
#   first the computer needs to check the visited rooms list with the list checker funtion
#   Then the computer need to check if the gadget is in list with the list checker funtion
#   Then the computer has to check if the player has the correct stats based on what is necessary
#   Use conditionals about if the room has been visited, if you have money already, and if you have the correct stats to steal the money if you didn't already to get an outcome

#Room 2 funtion(Danvil Park)
#The goal of this funtion is to get the keycard for Doofenshmirz Evil Inc. and you have to fight norm for it unless you have the correct number of stats
#For this funtion the parameters are perry's stats, the gadget list, and the room visited list
#   First use the visited rooms funtion to check if the player has been there before
#   Then use the gadget checker funtion to check if the player already has the gadget
#   If they haven't gotten the object then they need to fight norm bot so I would call the combat funtion
#   Then the computer has to check if the player has the correct stats based on what is necessary
#   Use a seiries of conditionals to reach the outcome of the room and how they are going to interact with it

#Room 3 funtion(City Hall)
#The goal of this funtion is to gain a signal jammer and you need to warn Mayor Roger Doofenshmirz but to do that you need the platypus translator also you can gain some agility
#For this funtion the parameters are the gadget list and perry's stats
#   First check the gadget list to see if you have the signal jammer if so then you just exit the room
#   If you haven't then the computer uses the list checker again to check if the player has the platypus translator then you can warn the mayor and get the signal jammer other wise you have to leave
#   If you haven't already been there then you can gain an agility point

#Room 4 funtion(Subway Tunnels)
#This room is the only way to get to the final boss but you need to have a flashlight
#For this funtion the parameters are the gadget list
#   If the flashlight is on the gadget list(checked with the list checker funtion) then the player can enter other wise they can't

#Room 5 funtion(Slushy Burger)
#The goal of this room is to gain health from a burger but you need to have money
#Room 6 funtion(Waste Recycling Plant)
#Room 7 funtion(Water Tower)
#Room 8 funtion(Alleyway Hideout)
#Room 9 funtion(Doofenshmirz Evil Inc.)
#Room choice funtion
#Health change funtion
#Attack funtion
#Play again funiton

#MAIN LOOP
#while true
#   describe mission to player
#   tell them they are in the Fletchers backyard and they have to sneak away without being caught by the Fletchers
#   while true
