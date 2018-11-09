## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016

import random


#Pick a number
number = int(input("What should the answer be? "))
if number == -1:
    number = random.randint(1,100)

#Guess numbers and get response
for i in range(5):
    guess = int(input("Guess a number: "))
    if i != 4:
        if guess == number:
            print("You win!")
            break
        elif guess > number :
            print("The number is lower than that.")
        elif guess < number:
            print("The number is higher than that.")
    elif i == 4:
        if guess == number:
            print("You win!")
        elif guess != number:
            print("You lose; the number was " + str(number) + ".")