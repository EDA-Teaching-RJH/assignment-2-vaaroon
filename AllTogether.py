### Part Four -- your code goes here. 

import random 

random_number = [random.randint(1, 100) for i in range(1,11)]
print(random_number)


while True:
    even_number = random_number % 2
    
    if even_number == 0:
        random_number.pop()
        
    else:
        print(random_number)






