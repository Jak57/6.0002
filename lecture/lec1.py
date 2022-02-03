# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 07:42:54 2021

@author: jakir
"""

# Book
# 12.1.1

# ============
# Example: Greedy Algorithm - 0/1 Knapsack
# ============

# class Item(object):
    
#     def __init__(self, name, value, weight):
#         """
#         name (str): Name of the item
#         value (int): Value of the item
#         weight (int): Weight of the item

#         """
#         self.name = name
#         self.value = value
#         self.weight = weight
        
#     def getName(self):
#         return self.name
    
#     def getValue(self):
#         return self.value
    
#     def getWeight(self):
#         return self.weight
    
#     def __str__(self):
#         result = "<" + self.name + ", " + str(self.value) + ", " + str(self.weight) + ">"
#         return result
    
    
# def value(item):
#     """
#     item (Item)
#     """
#     return item.getValue()


# def weightInverse(item):
#     return 1.0/item.getWeight()


# def density(item):
#     return item.getValue()/item.getWeight()


# def greedy(items, maxWeight, keyFunction):
#     """
#     Assumes items a list (of type Item), maxWeight >= 0, 
#     keyFunction maps elements of items to numbers.

#     """
#     itemsCopy = sorted(items, key=keyFunction, reverse=True)
#     result = []
#     totalValue, totalWeight = 0.0, 0.0
    
#     for i in range(len(itemsCopy)):
        
#         if (totalWeight + itemsCopy[i].getWeight() <= maxWeight):
            
#             result.append(itemsCopy[i])
#             totalWeight += itemsCopy[i].getWeight()
#             totalValue += itemsCopy[i].getValue()
            
#     return (result, totalValue)


# def buildItems():
#     """
#     Returns list of items

#     """
#     names = ["clock", "painting", "radio", "vase", "book", "computer"]
#     values = [175, 90, 20, 50, 10, 200]
#     weights = [10, 9, 4, 2, 1, 20]
#     Items = []
    
#     for i in range(len(names)):
#         Items.append(Item(names[i], values[i], weights[i]))
        
#     return Items


# def testGreedy(items, maxWeight, keyFunction):
#     """
#     Shows the result

#     """
#     taken, value =greedy(items, maxWeight, keyFunction)
#     print("Total value of items taken is", value)
    
#     for item in taken:
#         print(" ", item)


# def testGreedys(maxWeight = 20):
#     """
#     Shows result for different kind of approach
#     of solving 0/1 knapsack

#     """
#     items = buildItems()
#     print("Use greedy by value to fill knapsack of size", maxWeight)
#     testGreedy(items, maxWeight, value)
    
#     print("\nUse greedy by weight to fill knapsack of size", maxWeight)
#     testGreedy(items, maxWeight, weightInverse)
    
#     print("\nUse greedy by density to fill knapsack of size", maxWeight)
#     testGreedy(items, maxWeight, density)
    
    
# testGreedys()


# # 12.1.2

# def chooseBest(powerSet, maxWeight, getVal, getWeight):
#     """
#     powerSet (list): All possible set of items
#     maxWeight (int): Maximum capacity of knapsack
    
#     Returns the best value and set of items which ensures 
#     best value

#     """
#     bestVal = 0.0
#     bestSet = None
    
#     for items in powerSet:
#         itemsVal = 0.0
#         itemsWeight = 0.0
        
#         for item in items:
#             itemsVal += getVal(item)
#             itemsWeight += getWeight(item)
        
#         if itemsWeight <= maxWeight and itemsVal > bestVal:
#             bestVal = itemsVal
#             bestSet = items
        
#     return (bestSet, bestVal)


# def testBest(maxWeight = 20):
#     """
#     Print the optimal solution
#     """
#     items = buildItems()
#     powerSet = getPowerset(items)
#     taken, val = chooseBest(powerSet, maxWeight, Item.getValue, Item.getWeight)
    
#     print("\n\nOptimal solution:")
#     print("-------------------")
#     print("Total value of items taken is", val)
#     for item in taken:
#         print(" ", item)


# def getBinaryRep(n, numDigits):
#     """
#     Assumes n and numDigits are non-negative ints.
#     Returns a string of length numDigits that is a 
#     binary representation of n

#     """
#     result = ""
#     while n > 0:
#         result = str(n%2) + result
#         n = n//2
    
#     if len(result) > numDigits:
#         raise ValueError("not enough digits")
    
#     for i in range(numDigits - len(result)):
#         result = "0" + result
        
#     return result


# def getPowerset(L):
#     """
#     Assumes L is a list.
#     Returns a list of lists that contains all 
#     possible combinations of elements of L. 

#     """
#     powerset = []
#     for i in range(0, 2**len(L)):
#         binStr = getBinaryRep(i, len(L))
#         subset = []
        
#         for j in range(len(L)):
#             if binStr[j] == "1":
#                 subset.append(L[j])
#         powerset.append(subset)
        
#     return powerset


# testBest()
    

# Slide

# ============
# Example: Knapsack
# ============

class Food(object):
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.value / self.calories
    
    def __str__(self):
        return self.name + ": <" + str(self.value) + ", " + str(self.calories) + ">"


def buildMenu(names, values, calories):
    """
    names, values, calories are lists of same length.
    names is a list of strings
    values and calories are lists of numbers
    
    Returns list of food
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
        
    return menu


def greedy(items, maxCost, keyFunction):
    """
    Assumes items a list, maxCost >= 0
    keyFunction maps elements of items to number
    """
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsCopy)):
        if totalCost + itemsCopy[i].getCost() <= maxCost:
            
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    
    return (result, totalValue)


def testGreedy(items, constraint, keyFunction):
    taken, value = greedy(items, constraint, keyFunction)
    print("Total value of items taken =", value)
    
    for item in taken:
        print(" ", item)
        
        
def testGreedys(foods, maxUnits):
    print("Use greedy by value to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)
    
    print("\nUse greedy by cost to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    
    print("\nUse greedy by density to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.density)


names = ["wine", "beer", "pizza", "burger", "fries", \
         "cola", "apple", "donut", "cake"]
    
values = [89, 90, 95, 100, 90, 89, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]

foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
print("\n----------\n")
testGreedys(foods, 1000)

    
    







