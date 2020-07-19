import random

name = input("Your name: ")

def play():
    game_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(game_choices)

    user_choice = False
    while user_choice == False:
        user_choice = input("Rock, paper or scissors?: ").lower().strip()
        print(f"Your choice is: {user_choice}")
        print(f"The Computer's choice is: {computer_choice}\n")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You won!")
            else: #else would mean the computer's choice is scissors
                print("You lost!")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("You won!")
            else: #else would mean the computer's choice is rock
                print("You lost!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You won!")
            else: #else would mean the computer's choice is paper
                print("You lost!")
        else:
            print("Invalid choice. Please enter a valid option\n") #in case user types something not listed in game_choices

while True:
    play_again = input(f"\nDo you want to play rock, paper or scissors? (yes/no)\n")
    if play_again == 'yes': #user selects yes so game restarts
        print()
        play()
    elif play_again == 'no': #user selects no so game ends
        break
    else:
        print("invalid choice") #in case user types something other than yer or no
