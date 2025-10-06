#AB 1st rock paper scissors
import random

print('This is a game or rock paper scissors.')
while True:
    choice = input("Rock Paper or Scissors(If you are done put quit): ").strip().capitalize()
    computer = random.randint(1,3)
    #1 is rock 2 is paper 3 is scissors
    if choice == "Rock" and computer == 1:
        print("You put rock.")
        print("The computer put rock.")
        print("Oh, we both chose rock!")
        continue
    elif choice == "Rock" and computer == 2:
        print("You put rock.")
        print("I put paper.")
        print("You lost.")
        continue
    elif choice == "Rock" and computer == 3:
        print("You put rock.")
        print("I put scissors.")
        print("YOU WON!")
        continue
    elif choice == "Paper" and computer == 1:
        print("You put paper")
        print("I put rock.")
        print("YOU WON!")
        continue
    elif choice == "Paper" and computer == 2:
        print("You put paper.")
        print("I put paper.")
        print("Oh, we both chose paper!")
        continue
    elif choice == "Paper" and computer == 3:
        print("You chose paper.")
        print("I chose scissors")
        print("You lost.")
        continue
    elif choice == "Scissors" and computer == 1:
        print("You chose scissors.")
        print("I chose rock.")
        print("You lost.")
        continue
    elif choice == "Scissors" and computer == 2:
        print("You chose scissors.")
        print("I chose paper.")
        print("YOU WON!")
        continue
    elif choice == "Scissors" and computer == 3:
        print("You chose scissors.")
        print("I chose scissors.")
        print("Oh, we both chose scissors!")
        continue
    elif choice == "quit":
        print("Thanks for playing. Goodbye.")
        break
    else:
        print("Sorry, that was an invalid choice. Try again.")
