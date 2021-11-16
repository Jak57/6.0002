###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Jakir Hasan
# Collaborators: N/A
# Time: 3 Hours

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    # pass
    
    # Opening file
    with open(filename, "r") as file:
        cows = {}
        
        for line in file:
            
            # Stripping new line
            line = line.rstrip("\n")
            word_list = line.split(",")
            name = word_list[0]
            
            weight = int(word_list[1])
            # Creating dictionary of key: name and value: weight
            cows[name] = weight
            
    return cows
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # pass
    
    # Sorting dictionary according to weights
    cows_sorted = dict(sorted(cows.items(), key = lambda item: item[1], reverse = True))
    taken = {}
    
    # Initially taken cow is false
    for name in cows_sorted:
        taken[name] = False
    
    trips = []
    cows_transported = 0
    
    # Picking greedily the cow which has large weight
    while True:
        trip = []
        total_weight = 0
        
        for name in cows_sorted:
            weight = cows_sorted[name]
            if not taken[name] and weight + total_weight <= limit:
                
                total_weight += weight
                trip.append(name)
                
                cows_transported += 1
                taken[name] = True
        
        trips.append(trip)
        if cows_transported == len(cows):
            break

    return trips
    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # pass
    
    # Trying all possible partitions and
    # picking the best trip
    
    for trips in get_partitions(cows):
        optimal_trip = True
        
        for trip in trips:
            total_weight = 0
            
            for name in trip:
                weight = cows[name]
                total_weight += weight
                
            if (total_weight > limit):
                optimal_trip = False
                break
        
        if optimal_trip:
            return trips
    
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    # pass

    cows = load_cows("ps1_cow_data.txt")

    # Measuring time of greedy approach
    start = time.time()
    trips = greedy_cow_transport(cows)
    end = time.time()
    
    print("Number of trips needed using greedy approach is", len(trips))
    print("Time needed to run greedy approach in seconds is", end-start)
    
    print("\n--------\n")
    
    # Measuring time of brute force approach
    start = time.time()
    trips = brute_force_cow_transport(cows)
    end = time.time()
    
    print("Number of trips needed using brute force approach is", len(trips))
    print("Time needed to run brute force approach in seconds is", end-start)
    

if __name__ == '__main__':
    compare_cow_transport_algorithms()
