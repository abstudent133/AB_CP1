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
#For this function the parameters is the gadgets list, kwarg of perry's stats(health,stealth,strength), visited rooms list
#   first the computer needs to check the visited rooms list
#   if room 1 was on that list
#       if money was on the gadgets list or perry's stealth is 0
#           return there is nothing for you in this room choose another
#       else money was not on the gadgets list and perry's health is 1 or greater
#           choice is the choice to steal the money(1) or go to another room(2)
#           if choice is 1
#               append gadgets list with money
#               return gadgets list and a message saying you have the money
#           else choice is 2
#               return message about going to another room
#   if money was found on
#Room 2 funtion(Danvil Park)
#Room 3 funtion(City Hall)
#Room 4 funtion(Subway Tunnels)
#Room 5 funtion(Slushy Burger)
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
