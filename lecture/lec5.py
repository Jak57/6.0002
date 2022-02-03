# # -*- coding: utf-8 -*-
# """
# Created on Thu Jan 20 14:29:32 2022

# @author: jakir
# """
# ################
# # Code from Book
# ################

# import random
# import pylab
# random.seed(0)

# class Location(object):
#     def __init__(self, x, y):
#         """
#         x and y are numbers

#         """
#         self.x, self.y = x, y
        
#     def move(self, deltaX, deltaY):
#         """
#         deltaX and deltaY are numbers

#         """
#         return Location(self.x + deltaX, self.y + deltaY)
    
#     def getX(self):
#         return self.x
    
#     def getY(self):
#         return self.y
    
#     def distFrom(self, other):
#         ox, oy = other.x, other.y
#         xDist, yDist = self.x - ox, self.y - oy
#         return (xDist**2 + yDist**2)**0.5
    
#     def __str__(self):
#         return "<" + str(self.x) + ", " + str(self.y) + ">"
    
    
# class Field(object):
#     def __init__(self):
#         self.drunks = {}
    
#     def addDrunk(self, drunk, loc):
#         if drunk in self.drunks:
#             raise ValueError("Duplicate drunk")
#         else:
#             # drunk is immutable, so we can use is as key in
#             # dictionary
#             self.drunks[drunk] = loc
            
#     def moveDrunk(self, drunk):
#         if drunk not in self.drunks:
#             raise ValueError("Drunk not in field")
            
#         xDist, yDist = drunk.takeStep()
#         currentLocation = self.drunks[drunk]
        
#         # use move method of Location to get
#         # new location
#         self.drunks[drunk] = currentLocation.move(xDist, yDist)
    
#     def getLoc(self, drunk):
#         if drunk not in self.drunks:
#             raise ValueError("Drunk not in field")
            
#         return self.drunks[drunk]


# class Drunk(object):
#     def __init__(self, name = None):
#         """
#         Assumes name is a str

#         """
#         self.name = name
        
#     def __str__(self):
#         if self.name != None:
#             return self.name
#         return "Anonymous"
    
    
# class UsualDrunk(Drunk):
#     def takeStep(self):
#         stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         return random.choice(stepChoices)


# def walk(f, d, numSteps):
#     """
#     Assumes: f a Field, d a drunk in f and numSteps is an int >= 0.
#     Moves d numSteps times; returns the distance between the final location 
#     and the location at the start of the walk.

#     """
#     start = f.getLoc(d)
#     for s in range(numSteps):
#         f.moveDrunk(d)
#     return start.distFrom(f.getLoc(d))


# def simWalks(numSteps, numTrials, dClass):
#     """
#     Assumes numSteps an int >= 0, numTrials an int > 0, 
#     dClass a subclass of Drunk
    
#     Simulates numTrials walk of numSteps steps each. 
#     Returns the list of the final distances for each trial.

#     """
#     Homer = dClass()
#     origin = Location(0, 0)
#     distances = []
    
#     for t in range(numTrials):
#         f = Field()
#         f.addDrunk(Homer, origin)
#         distances.append(round(walk(f, Homer, numSteps), 1))
#     return distances


# def drunkTest(walkLengths, numTrials, dClass):
#     """
#     Assumes walkLengths a sequence of ints >= 0, numTrials an
#     int > 0, dClass a subclass of Drunk
    
#     For each number of steps in walkLengths, runs simWalks 
#     with numTrials walks and prints results
#     """
    
#     for numSteps in walkLengths:
#         distances = simWalks(numSteps, numTrials, dClass)
#         print(dClass.__name__, "random walk of", numSteps, "steps")
#         print(" Mean =", round(sum(distances) / len(distances), 4))
#         print(" Max =", max(distances), "Min =", min(distances))
    

# # drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
# # drunkTest((0, 1), 100, UsualDrunk)
    
# class ColdDrunk(Drunk):
#     def takeStep(self):
#         stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
#         return random.choice(stepChoices)


# class EWDrunk(Drunk):
#     def takeStep(self):
#         stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
#         return random.choice(stepChoices)


# def simAll(drunkKinds, walkLengths, numTrials):
#     for dClass in drunkKinds:
#         drunkTest(walkLengths, numTrials, dClass)
#         print("\n---------------\n")
    

# # simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)
    

# class StyleIterator(object):
#     def __init__(self, styles):
#         self.index = 0
#         self.styles = styles
        
#     def nextStyle(self):
#         result = self.styles[self.index]
#         if self.index == len(self.styles) - 1:
#             self.index = 0
#         else:
#             self.index += 1
        
#         return result
    
    
# def simDrunk(numTrials, dClass, walkLengths):
#     meanDistances = []
#     for numSteps in walkLengths:
#         print("Starting simulation of", numSteps, "steps")
#         trials = simWalks(numSteps, numTrials, dClass)
        
#         mean = sum(trials) / len(trials)
#         meanDistances.append(mean)
        
#     return meanDistances


# def simAll1(drunkKinds, walkLengths, numTrials):
#     styleChoice = StyleIterator(("m-", "r:", "k-."))
    
#     for dClass in drunkKinds:
#         curStyle = styleChoice.nextStyle()
#         print("Starting simulation of", dClass.__name__)
#         means = simDrunk(numTrials, dClass, walkLengths)
#         pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
        
#         pylab.title("Mean distance from origin (" + str(numTrials) + ") trials")
#         pylab.xlabel("Number of Steps")
#         pylab.ylabel("Distance from Origin")
        
#         pylab.legend(loc = "best")
#         pylab.semilogx()
#         pylab.semilogy()
    
# # simAll1((UsualDrunk, ColdDrunk, EWDrunk), (10, 100, 1000, 10000, 100000), 100)      

# def getFinalLocs(numSteps, numTrials, dClass):
#     locs = []
#     d = dClass()
    
#     for t in range(numTrials):
#         f = Field()
#         f.addDrunk(d, Location(0, 0))
        
#         for s in range(numSteps):
#             f.moveDrunk(d)
#         locs.append(f.getLoc(d))
        
#     return locs


# def plotLocs(drunkKinds, numSteps, numTrials):
#     styleChoice = StyleIterator(("k+", "r^", "mo"))
#     for dClass in drunkKinds:
#         locs = getFinalLocs(numSteps, numTrials, dClass)
#         xVals, yVals = [], []
        
#         for loc in locs:
#             xVals.append(loc.getX())
#             yVals.append(loc.getY())
        
#         meanX = sum(xVals) / len(xVals)
#         meanY = sum(yVals) / len(yVals)
#         curStyle = styleChoice.nextStyle()
#         pylab.plot(xVals, yVals, curStyle, label = \
#                    dClass.__name__ + " mean loc. = <" + str(meanX) + ", " + \
#                        str(meanY) + ">")
    
#     pylab.title("Location at end of walks (" + str(numSteps) + " steps)")
#     pylab.xlabel("Steps East/West of Origin")
#     pylab.ylabel("Steps North/South of Origin")
#     pylab.legend(loc = "lower left")

# # plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)

# def traceWalk(drunkKinds, numSteps):
#     styleChoice = StyleIterator(("k+", "r^", "mo"))
#     # f = Field()
#     # For odd field
#     f = OddField(1000, 100, 200)
    
#     for dClass in drunkKinds:
#         d = dClass()
#         f.addDrunk(d, Location(0, 0))
#         locs = []
        
#         for s in range(numSteps):
#             f.moveDrunk(d)
#             locs.append(f.getLoc(d))
        
#         xVals, yVals = [], []
#         for loc in locs:
#             xVals.append(loc.getX())
#             yVals.append(loc.getY())
        
#         curStyle = styleChoice.nextStyle()
#         pylab.plot(xVals, yVals, curStyle, label = dClass.__name__)
    
#     pylab.title("Spots Visited on Walk (" + str(numSteps) + " steps)")
#     pylab.xlabel("Steps East/West of Origin")
#     pylab.ylabel("Steps North/South of Origin")
#     pylab.legend(loc = "best")
    
# # traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 200)

# class OddField(Field):
#     def __init__(self, numHoles, xRange, yRange):
#         Field.__init__(self)
#         self.wormHoles = {}
        
#         for w in range(numHoles):
#             x = random.randint(-xRange, xRange)
#             y = random.randint(-yRange, yRange)
            
#             newX = random.randint(-xRange, xRange)
#             newY = random.randint(-yRange, yRange)
#             newLoc = Location(newX, newY)
#             self.wormHoles[(x, y)] = newLoc

#     def moveDrunk(self, drunk):
#         Field.moveDrunk(self, drunk)
#         x = self.drunks[drunk].getX()
#         y = self.drunks[drunk].getY()
        
#         if (x, y) in self.wormHoles:
#             self.drunks[drunk] = self.wormHoles[(x, y)]

# traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 500)



###############
# Lecture Code
###############
import random
import pylab
random.seed(0)
    
class Location(object):
    def __init__(self, x, y): # Location is immutable type
        """
        x and y are numbers
        """
        self.x, self.y = x, y
        
    def move(self, deltaX, deltaY):
        """
        deltaX and deltaY are numbers
        """
        newX = self.x + deltaX
        newY = self.y + deltaY
        return Location(newX, newY)
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        xDist = (self.x - other.x)**2
        yDist = (self.y - other.y)**2
        return (xDist + yDist)**0.5
    
    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    
    
class Field(object):
    def __init__(self): # Field is mutable
        self.drunks = {}
    
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Duplicate drunk")
        self.drunks[drunk] = loc
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        # Use move method of Location to get new location
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        return self.drunks[drunk]
    
    
class Drunk(object):
    def __init__(self, name = None): # Drunk is immutable
        self.name = name
    
    def __str__(self):
        if self != None:
            return self.name
        return "Anonymous"
    

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
    

class MasochistDrunk(Drunk):
    def takeStep(self):
        # Biased random walk toward north
        stepChoices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
    
def walk(f, d, numSteps):
    """
    Assumes: f a Field, d a Drunk in f and numSteps an int >= 0.
    Moves d numSteps times; returns the distance between the final
    location and the location at the start of the walk.
    """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))
    
    
def simWalks(numSteps, numTrials, dClass):
    """
    Assumes numSteps an int >= 0, numTrials an int > 0, dClass a
    subclass of Drunk. Simulates numTrials walks of numSteps each.
    Returns a list of final distances for each trial.
    """
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances


def drunkTest(walkLengths, numTrials, dClass):
    """
    Assumes walkLengths a sequence of ints >= 0, numTrials an 
    int > 0 and dClass a subclass of Drunk.
    For each number of steps in walkLengths runs simWalks with numTrials
    walk and prints results.

    """
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, "random walk of", numSteps, "steps")
        print(" Mean =", round(sum(distances) / len(distances), 4))
        print(" Max =", max(distances), " Min =", min(distances))
    
# drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)

def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)

# simAll((UsualDrunk, MasochistDrunk), (1000, 10000), 100)

# Plotting

# xVals = [1, 2, 3, 4]
# yVals = [1, 2, 3, 4]
# pylab.plot(xVals, yVals, "b-", label = "first")

# yVals = [1, 7, 3, 5]
# pylab.plot(xVals, yVals, "r--", label = "second")
# pylab.legend()

class StyleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
        
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

    
    
    
    
    
    
    
        
        