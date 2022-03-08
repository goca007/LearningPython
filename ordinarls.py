s = input("Type a number from 1 to infinity:")
if s.endswith("1"):
  print (s+"st")
elif s.endswith ("2"):
   print (s+"nd")
elif s.endswith ("3"):
  print (s+"rd")
else: 
    print (s+"th")

#Cesar code 

import random
code = random.randint(1,10)
print ("This is your encryption key")
print (code)

s = input("Type your secret message here:")
out = ""
for c in s: 
  o = ord (c)
  o = o + code 
  c = chr (o)
  out = out + c
print ("This is your encoded message:")
print (out)

# ordinal to cardinal 

s = input("Type a number from 1 to infinity:")
if s.endswith("1"):
  print (s+"st")
elif s.endswith ("2"):
   print (s+"nd")
elif s.endswith ("3"):
  print (s+"rd")
else: 
    print (s+"th")

#Cesar code 

import random
code = random.randint(1,10)
print ("This is your encryption key")
print (code)

s = input("Type your secret message here:")
s = s.upper ()
#print(s.upper())

out = ""
for c in s: 
  o = ord (c)
  if o > 64 and o < 91: 
    o = o + code 
    if o > 91: 
      o = o - 26
    c = chr (o)
  out = out + c
print ("This is your encoded message:")
print (out)

#Making it harder to crack 

#for harder in out: 
#  tryharder = ord (out)
  

#Decoding the Cesar code 

decode = input ("Type your encoded message here:")
decode = decode.upper ()

nouveau = ""
for haha in decode: 
  hihi = ord (haha)
  if hihi > 64 and hihi < 91: 
    hihi = hihi - code
    if code < 64:
      code = code + 26
    haha = chr (hihi)
  nouveau = nouveau + haha
print ("This is your decoded message:")
print (nouveau)


#  <  >  <  > ABCDEFGHIJKLMNOPQRSTUVWXYZ

#Cesar code 

import random
code = random.randint(1,10)
print ("This is your encryption key")
print (code)

s = input("Type your secret message here:")
s = s.upper ()
#print(s.upper())

out = ""
for c in s: 
  o = ord (c)
  if o > 64 and o < 91: 
    o = o + code 
    if o > 90: 
      o = o - 26
    c = chr (o)
  out = out + c
print ("This is your encoded message:")
print (out)



#  <  >  <  >

##############################
# TURN BACK NOW!
# The code below is spoiler
# for the Introduction to
# Python  course at City Lit!
##############################






import random
import time

possible = ["cat", "clock", "banana", "car", "pencil", "bear", "policeman", "bus", "guitar", "alligator", "playing card", "pizza", "chair", "candle", "snowflake", "parrot", "trousers", "hairbrush", "shed"]
print()
print()
num = 5
items = random.sample(possible, num)
print(items)
time.sleep(5)
for i in range(20):
  print()
solution = random.choice(items)
items.remove(solution)
random.shuffle(items)
print(items)
ans = input("What's missing? ")
if ans.lower() == solution:
  print("Well done!")
else:
  print("Nope, it was", solution)