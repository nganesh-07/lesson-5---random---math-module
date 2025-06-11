import random
true = True
number = str(random.randint(0, 10))

print("Guess what number I'm thinking of between 0 and 10. Keep guessing until you get it right and the game ends.")

while true:
    guess = input("Enter your guess here:")
    if number == guess:
        print("You got it.")
        break
    else:
        print("Try again...")