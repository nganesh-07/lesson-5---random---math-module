import random

while True:
    user = input("Enter ur action for rock, paper, scissors here:")
    possible_actions = ["rock", "paper", "scissors"]
    computer = random.choice(possible_actions)
    print("You chose", user, "while the computer chose", computer)

    if user == computer:
        print("Draw.")
    elif user == "rock":
        if computer == "scissors":
            print("Rock over scissors, you win.")
        else:
            print("Paper beats rock, you lost.")
    elif user == "paper":
        if computer == "rock":
            print("Paper beats rock, you won.")
        else:
            print("Your paper lost to scissors.")
    elif user == "scissors":
        if computer == "rock":
            print("Your scissors r done for, you lost.")
        else:
            print("Scissors over paper, you won.")
    print("Good game.")