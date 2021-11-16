###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Jakir Hasan
# Collaborators: N/A
# Time: 2 Hours
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    # pass
    
    # Initializing first row of table with
    # large values
    for i in range(target_weight + 1):
        memo[(0, i)] = 1000000000
    
    # Initializing first column with 0
    for i in range(len(egg_weights) + 1):
        memo[(i, 0)] = 0

    for i in range(1, len(egg_weights) + 1):
        
        for j in range(1, target_weight + 1):
            # weight of an egg
            weight = egg_weights[i-1]
            
            if (weight <= j):
                # If weight of an egg is less than j, then pick the minimum
                # of upper cell or the cell present left weight distance before 
                # plus one
                memo[(i, j)] = min(memo[(i-1, j)],\
                                   memo[(i, j-weight)] + 1)
            else:
                # If weight is greater, then pick the upper cell
                memo[i, j] = memo[i-1, j]
    
    # Total number of different sized eggs
    total = len(egg_weights)
    
    # Minimum no. of eggs needed to transport
    total_eggs_needed = memo[(total, target_weight)]

    return total_eggs_needed
    

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
