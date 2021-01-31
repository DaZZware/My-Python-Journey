# Guess number game 2

import random

secret_number = 69

n = input('Guess the Secret Number between 1 and 100: ')
n = int(n) # input to digit to read by computer

while not (n == secret_number):
    # Not equel to secret number selected.
    if n > secret_number:
        print('Your guess is to high, try again. ')
    else:
        print('Your guerss is to low, try again. ')
    # Ask to guess again
    n = input('Take another guess between 1 and 100 ')
    n = int(n)
print('Great guess, you got it')

input()
