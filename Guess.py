
import random

n = random.randrange(1,10)

guess = int(input("Enter any number: "))
while n!= guess: # means if n is not equal to the input guess
    # if guess is smaller than n
    if guess < n:
        print("Too low") 
         # to again ask for the user input   
        guess = int(input("Enter number again: "))
    

    elif guess > n:
        print("Too high!")
        # to again ask for the user input
        guess = int(input("Enter number again: "))

        
    # if guess gets equals to n terminate the while loop
    else:
        break
print("you guessed it right!!")