# Guess the number game

secret_number = 87
n = input('Guess the Secret Number between 1 and 100 ')
n = int(n) # converts input to interger
if n == secret_number:
    print('You have got it!')
else:
    # if not equel check higher or lower
    if n > secret_number:
        print('Your guess was too high')
    else:
        print('Your guess was too low')
print('Thanks for playing')

input()
