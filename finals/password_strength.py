#AB 1st password strength test

#password is ask user for password
password = input("What is your password: ")
#length is get length of password
length = len(password)
#length point = 0
len_point = 0
#lower point = 0
low_point = 0
#upper point = 0
upp_point = 0
#special point = 0
spe_point = 0
#number point = 0
num_point = 0
#total points = length point + lower point + upper point + number point + special point
total = len_point + low_point + upp_point + spe_point + num_point
#special = (!@#$%^&*()_+-=[]{}|;:,.<>?)
special = "(!@#$%^&*()_+-=[]{}|;:,.<>?)"

#if length is >= 8 then
if length >= 8:
    #add 1 to the points
    len_point += 1

#for password
for char in password:
    #if character is lower is true
    if char.islower:
        #add 1 point to the  lower points
        low_point += 1
        #break code
        break
#for password
for char in password:
    #if charachter is upper is true
    if char.isupper:
        #add 1 to  upper points
        upp_point += 1
        #break code
        break
#for password
for char in password:
    #if character is number is true
    if char.isnumeric:
        #add 1 to number points
        num_point += 1
        #break code
        break
#for password
for char in password:
    #if character has special
    if char in special:
        #add 1 to special points
        spe_point += 1
        #break code
        break

# show the total points
print(f"Your password is {total}/5")
#if total points is 5
if total == 5:
    #show this is a very strong password
    print("This password is a very strong.")
#or else total points is 4
elif total == 4:
    #show this is a very strong password
    print("This is a strong password.")
#or else total points is 3
elif total == 3:
    #show this is a mid password
    print("This is a mid password.")
#or else total points is 2
elif total == 2:
    #show this is a weak password
    print("This is a weak password.")
#or else totla points is 1
elif total == 1:
    #show this is a very weak password
    print("This is a very weak password.")
#or else total points is 0
    #show this is th worst password ever
#if 
#if length point is 0
    #show this password is too short
#if lower point is 0
    #show this password doesn't have a lowercase letter
#if upper point is 0
    #show this password doesn't have an uppercase letter
#if number point is 0
    #show this password doesn't have a number
#if special point is 0
    #show this password doesn't have a special character


        
