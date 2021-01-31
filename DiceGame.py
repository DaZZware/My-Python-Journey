# Dice Game
import random
import time

def rollDice(n):
    dice = [] # Start empty
    # Adding range of number 1-6 to list
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

def findWinner(cdiceList, udiceList):
    computerTotal = sum(cdiceList)
    userTotal = sum(udiceList)
    print("Computer total:",computerTotal)
    print("User Total:", userTotal)
    if userTotal > computerTotal:
        print("User Wins")
    elif computerTotal > userTotal:
        print("Computer Wins")
    else:
        print("It's a Tie!!")
    
def rollAgain(choices, diceList):
    print("Roll Again....")
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i] == 'r':
            diceList[i] = random.randint(1,6)
    time.sleep(3)

def computerStrategy1(n):
    #Create computer choices: roll everything.
    print("Computer is thinking......")
    time.sleep(3)
    choices = '' # start with an empty list
    for i in range(n):
        choices = choices + 'r'
    return choices

def computerStrategy2(n):
    # roll everything under again
    print('Computer is thinking.....')
    time.sleep(3)
    choices = ''
    for i in range(n):
        if computerRolls[i] < 5:
            choices = choices + 'r'
        else:
            choices = choices + '-'
    return choices
    
# First Step in game - starting game
numberDice = input('Enter the total of Dice to be used: ')
numberDice = int(numberDice)
ready = input('Ready to Roll? Hit any Key to continue.. ')
# User Rolling
userRolls = rollDice(numberDice)
print('User first roll: ', userRolls)
# hold or roll
userChoices = input("Enter - to hold or r to roll again: ") # use - and r to each corisponding dice
#check choices
while len(userChoices) != numberDice:
    print("You must enter", numberDice,"choices")
    userChoices = input("Enter - to hold or r to roll again: ")
rollAgain(userChoices, userRolls)
print('Player new roll: ', userRolls)

# Computer turn
print('Computers turn ')
computerRolls = rollDice(numberDice)
print('Computers first roll: ', computerRolls)
# Decide on what choice 
computerChoices = computerStrategy2(numberDice)
print('Computer choice: ', computerChoices)
# computer rolls again
rollAgain(computerChoices, computerRolls)
print('Computer new Roll: ', computerRolls)
findWinner(computerRolls,userRolls)


input('Press Enter to exit')