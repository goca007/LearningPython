for num in range(2, 21):
    for i in range (2, num):
        if num % i == 0:
            # print(num, "is not a prime number")
            break
        
    else:
        print(num, "is a prime number")