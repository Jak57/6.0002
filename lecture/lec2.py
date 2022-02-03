# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 08:49:27 2021

@author: jakir
"""

# Book
# 13.1

# ==========
# Example: Fibonacci Sequence
# ==========

# def fib(n):
#     """
#     Assumes n is an int >= 0.
#     Returns fibonacci of n
#     """
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
    
# for i in range(121):
#     print("fib(" + str(i) + ") = " + str(fib(i)))



# Fast Fibonacci

# def fastFib(n, memo = {}):
#     """
#     Assumes n is an int >= 0, memo used only by recursive calls
#     Returns fibonacci of n
    
#     """
#     if (n == 0 or n == 1):
#         return 1
    
#     try:
#         return memo[n]
#     except KeyError:
#         result = fastFib(n-1, memo) + fastFib(n-2, memo)
#         memo[n] = result
#         return result


# for i in range(121):
#     print("fib(" + str(i) + ") = " + str(fastFib(i)))


#13.2
# ===========
# Example: 0/1 Knapsack using decision tree
# ===========

# import random

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
    

# def maxVal(toConsider, avail):
#     """
#     Assumes toConsider a list of items and avail a weight
#     Returns a tuple of the total value of the solution of
#     the 0/1 Knapsack problem and the items of the solution
#     """
    
#     if toConsider == [] or avail == 0:
#         result = (0, ())
        
#     elif toConsider[0].getWeight() > avail:
#         # Explore right branch only
#         result = maxVal(toConsider[1:], avail)
        
#     else:
#         nextItem = toConsider[0]
        
#         # Explore left branch
#         withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())
#         withVal += nextItem.getValue()
        
#         # Explore right branch
#         withoutVal,  withoutToTake = maxVal(toConsider[1:], avail)
        
#         # Choose better branch
#         if withVal > withoutVal:
#             result = (withVal, withToTake + (nextItem,))
#         else:
#             result = (withoutVal, withoutToTake)
        
#     return result


# def smallTest():
    
#     names = ["a", "b", "c", "d"]
#     values = [6, 7, 8, 9]
#     weights = [3, 3, 2, 5]
    
#     Items = []
#     for i in range(len(values)):
#         Items.append(Item(names[i], values[i], weights[i]))
    
#     val, taken = maxVal(Items, 5)
#     for item in taken:
#         print(item)
    
#     print("Total value of item taken is =", val)
        
        
# def buildManyItems(numItems, maxVal, maxWeight):
#     items = []
    
#     for i in range(numItems):
#         items.append(Item(str(i), random.randint(1, maxVal),\
#                           random.randint(1, maxWeight)))
    
#     return items


# def bigTest(numItems):

#     items = buildManyItems(numItems, 10, 10)
    
#     # val, taken = maxVal(items, 40)
#     memo = {}
#     val, taken = fastMaxVal(items, 40, memo)
    
#     print("Item taken")
#     for item in taken:
#         print(' ', item)
        
#     print("Total value of items taken =", val)


# def fastMaxVal(toConsider, avail, memo):
#     """
#     Assumes toConsider list of items, avail a weight, memo supplied by
#     recursive calls
    
#     Returns a tuple of the total value of the solution to the
#     0/1 knapsack problem and the items of that solution
#     """
    
#     if (len(toConsider), avail) in memo:
#         result = memo[(len(toConsider), avail)]
        
#     elif toConsider == [] or avail == 0:
#         result = (0, ())
        
#     elif toConsider[0].getWeight() > avail:
#         # Explore right branch only
#         result = fastMaxVal(toConsider[1:], avail, memo)
        
#     else:
        
#         nextItem = toConsider[0]
        
#         # Explore left branch
#         withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem.getWeight(), memo)
#         withVal += nextItem.getValue()
        
#         # Explore right branch
#         withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        
#         # Chose better branch
#         if withVal > withoutVal:
#             result = (withVal, withToTake + (nextItem, ))
#         else:
#             result = (withoutVal, withoutToTake)
            
#     memo[(len(toConsider), avail)] = result
#     return result


# bigTest(10)







