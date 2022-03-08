
import random
num = random.randint(1,10)
print(num)
count = 4
score = 0
guess = int(input("Guess a number between 1 and 10: "))
if guess == num:
    score += 1
else:
    score -= 1

while guess != num and count > 0:
     guess = int(input("Take another guess: "))
     count -= 1 
     if guess != num:
         score -= 1
     else:
        score += 1

print("Your score is:", score)


"""
import random
num = random.randint(1,10)
#print(num)
count = 5
score = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != num:
        score -= 1
        count -= 1

    if guess == num:
        score += 1
        break

    elif count == 0:
        break 
    
print("Your score is:", score)

"""









    
