import random
user_action = input("Enter a choice(rock, paper, scissors): ")
user_action = user_action.lower() 
choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice)
#print(user_action, computer_choice)

if user_action == computer_choice:
    print("It's a tie!")
elif user_action == "rock":
    if computer_choice == "scissors":
        print("You win! Rock crushes scissors.") 
    else:
        print("You lose. Paper covers rock.") 
elif user_action == "paper":
    if computer_choice == "rock":
        print("You win! Paper covers rock.")
    else:
        print("You lose. Scissors cuts paper.")
elif user_action == "scissors":
    if computer_choice == "paper":
        print("You win! Scissors cuts paper.")
    else:
        print("You lose. Rock crushes scissors.")