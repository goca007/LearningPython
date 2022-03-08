"""
x = int(input("Enter a number: "))
def triangular_num(x):
    #print(sum(range(x+1)))
    #print((x ** 2 + x) // 2)
    print(x * (x + 1) // 2)
triangular_num(x)
"""

import math
x = int(input("Enter a number: "))
print(int(math.fsum(range(x+1))))

