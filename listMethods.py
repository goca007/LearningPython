# using this list, 
#basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
#basket.pop(0)
#print(basket)

# 2. Remove "Blueberries" from the list.
#basket.pop(3)
#print(basket)

# 3. Put "Kiwi" at the end of the list.
#basket.append("Kiwi")
#print(basket)

# 4. Add "Apples" at the beginning of the list
#basket.insert(0, "Apples")
#print(basket)

# 5. Count how many apples in the basket
#x = basket.count("Apples")
#print(x)

# 6. empty the basket
#basket.clear()
#print(basket)

#print(basket)

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.extend(new_friend)

print(sorted(friends))