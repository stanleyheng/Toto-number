import random #packages/libraries/modules

print ("Press Enter to Generate your 7 lucky TOTO number")
input() 

n = random.sample(range(1,49), 7) # Make n 7 random number between 1 and 49
sn = sorted(n) 
print (sn ,"good luck!")