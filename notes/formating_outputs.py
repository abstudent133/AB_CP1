#AB 1st Formating Outputs notes

name = "Jake"
age = 21
money = 25.06
percent = .74

print("Hello {}, you are {}. That is so old! You have ${:.2f} you must be rich. Random percent is {:%}.".format(name, age, money, percent))

print(f"Hello {name}, you are {age:,}. That is so old! You have ${money:.2f} you must be rich! Random percent is {percent:%}.")