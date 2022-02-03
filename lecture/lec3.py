# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:15:12 2021

@author: jakir
"""

# Book: 12.2

# class Node(object):
#     def __init__(self, name):
#         """
#         Assumes name is a string
#         """
#         self.name = name
    
#     def getName(self):
#         return self.name
    
#     def __str__(self):
#         return self.name
    
    
# class Edge(object):
#     def __init__(self, source, destination):
#         """
#         Assumes source and destination are nodes
#         """
#         self.source = source
#         self.destination = destination
        
#     def getSource(self):
#         return self.source
    
#     def getDestination(self):
#         return self.destination
    
#     def __str__(self):
#         return self.source.getName() + "->" + \
#             self.destination.getName()
    
    
# class WeightedEdge(Edge):
#     def __init__(self, source, destination, weight):
#         """
#         Assumes source and destination are nodes and 
#         weight a number

#         """
#         self.source = source
#         self.destination = destination
#         self.weight = weight
        
#     def getWeight(self):
#         return self.weight
    
#     def __str__(self):
#         return self.source.getName() + "->(" + str(self.weight) + \
#             ")" + self.destination.getName()
            
            
# class Digraph(object):
#     def __init__(self):
#         # nodes is a list of the nodes of the graph
#         nodes = []
#         # edges is a dict mapping each node to a list of 
#         # its children
#         edges = {}
        
#     def addNode(self, node):
#         """
#         Add node to the Digraph
#         node (Node)
#         """
#         if node in self.nodes:
#             raise ValueError("Duplicate node")
#         else:
#             self.nodes.append(node)
#             self.edges[node] = []
    
#     def addEdge(self, edge):
#         """
#         Add edges between two nodes
#         edge (Edge)

#         """
#         source = edge.getSource()
#         destination = edge.getDestination()
        
#         if (source not in self.nodes or destination not in self.nodes):
#             raise ValueError("Node not in graph")
#         else:
#             self.edges[source].append(destination)
    
#     def childrenOf(self, node):
#         """
#         Returns childrens of a node

#         """
#         return self.edges[node]
    
#     def hasNode(self, node):
#         return node in self.nodes
    
#     def __str__(self):
#         result = ""
#         for source in self.nodes:
#             for destination in self.edges[source]:
#                 result = result + source.getName() + "->" + \
#                     destination.getName() + "\n"
        
#         # Ommits final new line
#         return result[:-1]


# class Graph(Digraph):
    
#     def addEdge(self, edge):
#         Digraph.addEdge(self, edge)
#         rev = Edge(edge.getDestination(), edge.getSource())
#         Digraph.addEdge(self, rev)
        

# Slide
# -------

class Node(object):
    
    def __init__(self, name):
        """
        Assumes name is a string

        """
        self.name = name
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    
class Edge(object):
    
    def __init__(self, source, destination):
        """
        Assumes source and destination are nodes

        """
        self.source = source
        self.destination = destination
        
    def getSource(self):
        return self.source
    
    def getDestination(self):
        return self.destination
    
    def __str__(self):
        return self.source + "->" + self.destination


class Digraph(object):
    
    def __init__(self):
        """
        edges is a dict mapping each node to a list of its childrens        

        """
        self.edges = {}

    def addNode(self, node):
        """
        node (Node)

        """
        if node in self.edges:
            raise ValueError("Duplicate node")
        self.edges[node] = []

    def addEdge(self, edge):
        """
        edge (Edge)

        """
        source = edge.getSource()
        destination = edge.getDestination()
        
        if source not in self.edges or destination not in self.edges:
            raise ValueError("node not in graph")
        
        self.edges[source].append(destination)

    def childrenOf(self, node):
        """
        node (Node)
        Return list of childrens of the node

        """
        return self.edges[node]
    
    def hasNode(self, node):
        """
        node (Node)

        """
        return node in self.edges
    
    def getNode(self, name):
        """
        name (str)

        """
        for n in self.edges:
            if n.getName() == name:
                return n
        
        raise NameError(name)
        
    def __str__(self):
        result = ""
        
        for source in self.edges:
            for destination in self.edges[source]:
                result = result + source.getName() + "->" + destination.getName() + "\n"
        
        return result[:-1] # Ommits the final newline


class Graph(Digraph):
    
    def addEdge(self, edge):
        """
        edge (Edge)

        """
        Digraph.addEdge(self, edge)
        reverse = Edge(edge.getSource(), edge.getDestination())
        Digraph.addEdge(self, reverse)
        
        
def buildCityGraph(graphType):
    """
    graphType represents type of the graph (Digraph / Graph)

    """
    g = graphType()   
    for name in ("Boston", "New York", "Providence", "Chicago", "Denver", "Phoenix", "Los Angeles"):
        g.addNode(Node(name))
    
    g.addEdge(Edge(g.getNode("Boston"), g.getNode("Providence")))
    g.addEdge(Edge(g.getNode("Boston"), g.getNode("New York")))
    g.addEdge(Edge(g.getNode("Providence"), g.getNode("Boston")))
    
    g.addEdge(Edge(g.getNode("Providence"), g.getNode("NewYork")))
    g.addEdge(Edge(g.getNode("New York"), g.getNode("Chicago")))
    g.addEdge(Edge(g.getNode("Chicago"), g.getNode("Denver")))
    
    g.addEdge(Edge(g.getNode("Chicago"), g.getNode("Phoenix")))
    g.addEdge(Edge(g.getNode("Denver"), g.getNode("Phoenix")))
    g.addEdge(Edge(g.getNode("Denver"), g.getNode("New York")))
    g.addEdge(Edge(g.getNode("Los Angeles"), g.getNode("Boston")))
    
    return g


# --------------
# DFS
# --------------

def printPath(path):

    """
    Assumes path is a list of nodes
    """    
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
    
        if (i != (len(path)-1)):
            result = result + "->"
        # print(result)
    
    return result


# path = [1, 2, 3, 4, 5]
# print(printPath(path))

def DFS(graph, start, end, path, shortest, toPrint = False):
    """
    Assumes graph is a Digraph; start and end are nodes; path and
    shortest are list of nodes
    Returns a shortest path from start to end in a graph

    """
    path = path + [start]
    
    print("DFS call with:", start.getName())
    if toPrint:
        print("Current DFS path:", printPath(path))
        # print(shortest)
        # print("\n\n")
        if shortest == None:
            print("None")
        else:
            print("Shortest is:", printPath(shortest))
        
        print("\n\n")
    
    if start == end:
        return path
    
    for node in graph.childrenOf(start):
        
        if node not in path: # avoids cycle
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                
                if newPath != None:
                    shortest = newPath
    
    return shortest


def shortestPath(graph, start, end, toPrint = False):
    """
    Assumes graph is a Digraph; start and end are nodes.
    Returns a shortest path from start to end in a graph
    """
    
    return DFS(graph, start, end, [], None, toPrint)


def testSP():
    nodes = []
    
    for name in range(6):
        nodes.append(Node(str(name)))
    
    g = Digraph()
    for node in nodes:
        g.addNode(node)
    
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    g.addEdge(Edge(nodes[2], nodes[4]))

    sp = shortestPath(g, nodes[0], nodes[5], toPrint = True)
    print("Shortest path is", printPath(sp))


testSP()
        
        
        
        
        
        
        
        
        
        
        