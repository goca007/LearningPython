#Fibonacci suite 

Fibonacci=[0,1]
#final=[Fibonacci-1]
#penultimate=[Fibonacci-2]
#next=[final+penultimate]

for Counter in range (1,100):
  Fibonacci.append(Fibonacci[Counter] + Fibonacci[Counter-1])
print (Fibonacci)



#  <  >  <  > ABCDEFGHIJKLMNOPQRSTUVWXYZ