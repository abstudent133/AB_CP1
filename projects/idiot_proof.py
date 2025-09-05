#AB 1st Idiot Proof

username = input("What is your username?")
phone_num = input('What is your phone number(add a space bettween the first three numbers, next three numbers, and the last four numbers)?')
gpa = float(input('What is your gpa?'))

first_name, last_name = username.split('.')
full_name = (first_name + " " + last_name).title()

gpa = round(gpa,1)




