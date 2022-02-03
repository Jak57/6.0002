# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:43:35 2021

@author: jakir
"""

# Book: Chapter - 15

# 15.1: Roll Die

# import random

# def rollDie():
#     """
#     Returns a random int between 1 and 6
#     """
    
#     return random.choice([1, 2, 3, 4, 5, 6])


# def rollN(n):
#     """
#     Assumes n is an int
#     Rolls the die n times
#     """
    
#     result = ""
#     for i in range(n):
#         result = result + str(rollDie())
        
#     print(result)


# rollN(10)


# Example: Simulation of Die rolling

# def runSim(goal, numTrials, txt):
    
#     total = 0
#     for i in range(numTrials):
#         result = ""
#         for j in range(len(goal)):
#             result = result + str(rollDie())
        
#         if result == goal:
#             total += 1
    
#     print("Actual probability of", txt, "=", round(1/6**(len(goal)), 8))
#     estProbability = round(total/numTrials, 8)
#     print("Estimated probability of", txt, "=", estProbability)


# runSim("11111", 1000000, "11111")
    

# Example: Birthday problem -> same date

import random
import math

def sameDate(numPeople, numSame):
    possibleDates = range(366)
    birthdays = [0]*366
    
    for p in range(numPeople):
        birthday = random.choice(possibleDates)
        birthdays[birthday] += 1
    
    return max(birthdays) >= numSame


def birthdayProblem(numPeople, numSame, numTrials):
    numHits = 0
    
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1
    
    return numHits/numTrials


for numPeople in [10, 20, 40, 100]:
    print("For", numPeople, "est. probability of a shared birthday is", \
           birthdayProblem(numPeople, 2, 1000))
    
    numerator = math.factorial(366)
    denom = (366**numPeople) * math.factorial(366 - numPeople)
    print("Actual probability is", 1 - numerator/denom)
    print("\n---------\n")

