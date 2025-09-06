#AB 1st Idiot Proof

username = input("What is your username?")
phone_num = input('What is your phone number?')
gpa = float(input('What is your gpa?'))

first_name, last_name = username.split('.')
full_name = (first_name + " " + last_name).title()
print(full_name)

phone_num_1 = phone_num[:3]
phone_num_2 = phone_num[3:6]
phone_num_3 = phone_num[6:]

print(phone_num_1 + " " + phone_num_2 + " " + phone_num_3)

gpa = round(gpa,1)
print(gpa)




