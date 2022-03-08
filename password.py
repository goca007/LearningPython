import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password =''.join(random.choices(characters, k=12))        
print("Your password is ", password)

user_choice = input("Would you like a new password? Y/N ")
user_choice = user_choice.lower()

if user_choice == "y":
    count = 0
    while count < 10:
        user_choice = input("Another password? Y/N ")
        user_choice = user_choice.lower()
        count += 1  
        print(password)
        if count == 10:
            user_choice = input("This is your last chance! Y/N ")
            user_choice = user_choice.lower()
            count += 1  
            print(password)
        if count > 10:
            break
            
else:
    print("OK")














    

    
                                
