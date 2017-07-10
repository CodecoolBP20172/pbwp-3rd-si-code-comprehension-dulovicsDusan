#This is a program what picks a random number between 1-20. The user has to guess it under six times.

import random #Import a built-in function.

guessesTaken = 0 #Assign this variable to 0.

print('Hello! What is your name?') #Display a message.(Ask for the user's name.)
myName = input() #Ask for user input.

number = random.randint(1, 20) #Assign a variable to a number between 1-20.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #Display a message + the user's name.

while guessesTaken < 6: #This loop runs until the variable reaches 6.(The player reaches the 6th round of the game.)
    print('Take a guess.') #Display a message.
    guess = input() #Ask for user input.
    guess = int(guess) #User input to integer.

    guessesTaken += 1 #This variable adds 1 to guessTaken if the condition is True

    if guess < number: #If user input is lower than the number variable
        print('Your guess is too low.') #Display a message.

    if guess > number: #If user input higher than the number variable
        print('Your guess is too high.') #Display a message.

    if guess == number: #If user input equals the number variable
        break #Stop the loop.

if guess == number: #If user input equals the number variable
    guessesTaken = str(guessesTaken) #guessTaken variable to string.
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') #Display a message + the user's name + guessTaken variable.

if guess != number: #If user input not equals the number variable
    number = str(number) #number variable to string.
    print('Nope. The number I was thinking of was ' + number) #Display a message + number variable.
