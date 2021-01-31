# Functions that return information
# Define a function that fins the average of a list
# import sys

def average(myList):
    total = sum(myList) # use the function sum in python list
    average = total / len(myList) # len gives number of items
    return average

#using the function
scores = [7, 23, 56, 89]
averageScore = average(scores)
print('The Average of the scores is', averageScore)

input('press enter to close')