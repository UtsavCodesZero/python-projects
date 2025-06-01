# PROJECT 1: SNAKE, WATER, GUN GAME

import random

print("SNAKE WATER GUN GAME")
print("Let's begin!")

user_input = input("Enter your chocie (Snake, Water or Gun): ").capitalize()
options = ["Snake", "Water", "Gun"]
computer_choice = random.choice(options)

if user_input in options:
    print(f"You chose {user_input}.")
    print(f"Computer chose {computer_choice}.")

    if (user_input == computer_choice):
        print("It's a tie.")

    elif (user_input == "Snake" and computer_choice == "Water") or \
         (user_input == "Water" and computer_choice == "Gun") or \
         (user_input == "Gun" and computer_choice == "Snake"):
        print("You win!")

    else:
        print("You lose!")

else:
    print("Enter valid input (Snake, Water or Gun).")