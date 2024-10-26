### Part Four -- your code goes here. 

import random 
import math 

random_number = ([random.randint(1, 100) for i in range(1,11)])
print(random_number)


i = 0 
while i < (random_number):
    if random_number % 2 == 0:
        random_number.pop  # Remove the even number
    else:
        i += 1

print (random_number)
