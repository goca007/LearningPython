import random
import time

list = ["key", "fridge", "belt", "laptop", "comb", "house", "dog", "book", "coin", "bulb"]
print(list)
time.sleep(10)

x = 0
while x < 10:
    print("\n")
    x += 1

list.pop(random.randrange(len(list)))
random.shuffle(list)
print(list)
question = input("One item is missing. Which one? ")
