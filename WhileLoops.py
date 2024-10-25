### Part Two -- your code goes here. 
import random 
randomnumber = random.randint(1, 3) 

while True:
    guess = int(input("Guess a number between 1 and 100: ")) 

    if guess != randomnumber:
        continue

    else:
        print("You guessed the right number.")
        break



    
