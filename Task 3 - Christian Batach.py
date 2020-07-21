import random

name = input("Your name: ")

def play():
    dict = {
        "scissors" : "paper",
        "paper" : "rock",
        "rock" : "scissors" 
        }

    computer_random = random.choice(list(dict))
    computer_choice = dict[computer_random]

    user_choice = False
    while user_choice == False:
        user_choice = input("Rock, paper or scissors?: ").lower().strip()
        print(f"Your choice is: {user_choice}")
        print(f"The Computer's choice is: {computer_random}\n")
        if user_choice == computer_random:
            print("It's a tie!")
        elif user_choice == computer_choice:
            print("You lost!")
        elif user_choice != computer_choice:
            print("You won!")
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