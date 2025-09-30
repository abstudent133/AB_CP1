#AB 1st Shopping List Manager

print("This is a shopping list program that allows you to add to(1),remove from(2), or show(3) your shopping list. If you would like to exit the site please enter 4.")
shopping_list = []
while True:
    choice = int(input("Please input the number next to the action you want to complete(1, 2, 3, or 4): "))
    if not choice == 1 and not choice == 2 and not choice == 3 and not choice == 4:
        print("Sorry incorrect input try again")
    elif choice == 1:
        shopping_list.append(input("Please input you item:"))
        print("This is your shopping list now:")
        print(shopping_list)
    elif choice == 2:
        print(shopping_list)
        remove = input("Please input the item you would like to remove")
        print("This is your shopping list now:")
        print(shopping_list)
    elif choice == 3:
        print("This is your current shopping list:")
        print(shopping_list)
    elif choice == 4:
        break
