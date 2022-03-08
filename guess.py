import random
n = random.randint(1,5)
print(n)
guess = input("Guess a number between 1 and 5: ")  

try:
    guess = int(guess)

    if n == guess:
        print("Yes! You've guessed right!")
    else:
        print("Better luck next time.")
except:
    print("Please enter numeric input.")
    guess = int(input("Try again. Guess a number between 1 and 5: "))
    
    if n == guess:
        print("Hooray! You've guessed right!")
    else:
        print("Oh, dear.")  




