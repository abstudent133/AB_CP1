#AB 1st elif and logical operators notes

grade = 100

if grade > 100:
    print(f"You did extra credit ... you did {grade - 100}% extra credit!")
elif grade == 100:
    print("You have a perfect grade!")
else:
    print(f"TRY HARDER! You only have {grade}.")

username = "anna.b"
password = "1234"

user = input('Enter your username')
pword = input('Enter your password')

if not user or not pword:
    print('Please enter a valid input')
elif user == username and pword == password:
    print('Welcome Anna Bangerter')
elif user == username:
    print('Password incorrect')
else:
    print('Incorrect credentials')

 