#AB 1st List Notes 

sibs = ["Anna", "Kailyn", "Lauren", "Danielle", "Jason", "Nicole", "James"]
import random
print(random.choice(sibs, weights=(10,10,10,10,10,10,10), k=7))#this gives a weight to how likely something is to get chosen
print(sibs[6])
print(f"The list is {len(sibs)} people long")
print(sibs)
sibs[0] = "Marie"
sibs[6:-1] = ["Pratt","Ashera"]
sibs.pop()
sibs.pop(3)
#sibs.remove("Kailyn")
#sibs.append("Kailyn")
#sibs.insert(2, "Kailyn")
sibs.extend(["Bella", "Maisy"])
print(sibs)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]
        ]

print(board)

fruit = ("Apple","Orange","Banana")#Tuple ordered, not changeable

veggies = ("Spinach", "Kale", "Broccoli")#set unordered changeable