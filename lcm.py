import math
def lcm(list):
    lcm = list[0]
    for i in range(1,len(list)):
        lcm = lcm * list[i] // math.gcd(lcm, list[i])
    return lcm
l = list(range(2,21))
print(lcm(l))



