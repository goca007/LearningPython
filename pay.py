hrs = input("Enter your hours: ")
hrs = float(hrs)
regular_rate = input("Enter your hourly rate: ")
reg_rate = float(regular_rate)
higher_rate = reg_rate * 1.5


if hrs <= 40:
    pay = hrs * reg_rate
    print("Your gross pay is", pay)
    
else:
    pay = ((hrs - 40) * higher_rate) + (40 * reg_rate)
    print("Your gross pay is", pay)