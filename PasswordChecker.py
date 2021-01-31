# Password Checker

import time
password = 'Python39'

userGuess = input('Can you guess my password? \nType your first guess: ')
while not userGuess == password:
    print('This is incorrect, only clue I will give is as follows. \nThere is one Uppercase letter, two numbers and 5 lowercase letters. May or May not be in this particular order.')
    time.sleep(2)
    userGuess = input('Enter your Guess again: ')
    if userGuess == password:
        print()
        time.sleep(4)
        print('Success: You have correctly guessed my password.')
        input('Press Enter for a Surprise!!')

input()
