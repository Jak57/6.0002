# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

import unittest

#
# A set of data structures to represent graphs
#

class Node(object):
    """Represents a node in the graph"""
    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # This function is necessary so that Nodes can be used as
        # keys in a dictionary, even though Nodes are mutable
        return self.name.__hash__()


class Edge(object):
    """Represents an edge in the dictionary. Includes a source and
    a destination."""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return '{}->{}'.format(self.src, self.dest)


class WeightedEdge(Edge):
    def __init__(self, src, dest, total_distance, outdoor_distance):
        # pass  # TODO
        self.src = src
        self.dest = dest
        self.total_distance = total_distance
        self.outdoor_distance = outdoor_distance

    def get_total_distance(self):
        # pass  # TODO
        return self.total_distance

    def get_outdoor_distance(self):
        # pass  # TODO
        return self.outdoor_distance

    def __str__(self):
        # pass  # TODO
        result = ""
        result = self.src.get_name() + "->" + self.dest.get_name() + " (" \
            + str(self.get_total_distance()) + ", " + str(self.get_outdoor_distance()) + ")"
        
        return result 


class Digraph(object):
    """Represents a directed graph of Node and Edge objects"""
    def __init__(self):
        self.nodes = set([])
        self.edges = {}  # must be a dict of Node -> list of edges
    
    def __str__(self):
        
        result = ""
        # print(self.edges)
        
        # a->b (15, 10)
        # print("---------\n\n")
        for src in self.edges:
            values = self.edges[src]
            
            for edge in values:
                dest = edge[0]
                total_distance = edge[1]
                outdoor_distance = edge[2]
                
                # result = ""
                result += src.get_name() + "->" + dest.get_name() + " ("  \
                    + str(total_distance) + ", " + str(outdoor_distance) + ")" + "\n"
        #         print(result)
        
        # print("-------------\n")
        
        return result[:-1]
        
        # for key in self.edges:
        #     print(key, self.edges[key])
    
    # comment: add
    def get_node(self, name):
        
        # print(self.nodes)
        for n in self.nodes:
            if (n.get_name() == name):
                return n
        raise NameError(name)
    # end comment

    def get_edges_for_node(self, node):
        # print(self.edges[node])
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def add_node(self, node):
        """Adds a Node object to the Digraph. Raises a ValueError if it is
        already in the graph."""
        
        # comment
        # # pass  # TODO
        # if node in self.edges:
        #     # print("-----------Dup\n\n")
        #     # print(node)
        #     # print("-----------\n\n")
        #     raise ValueError("Duplicate node")
        
        # # self.nodes.add(node)
        # self.edges[node] = []
        # end comment
        
        if node not in self.nodes:
            self.nodes.add(node)
            self.edges[node] = []
        else:
            raise ValueError("Duplicate node")
        # print("-----------Dup\n\n")
        # print(node)
        # print("-----------\n\n")
            # raise ValueError("Duplicate node")
        
        # self.nodes.add(node)
        # self.edges[node] = []

    def add_edge(self, edge):
        """Adds an Edge or WeightedEdge instance to the Digraph. Raises a
        ValueError if either of the nodes associated with the edge is not
        in the  graph."""
        # pass  # TODO
        src = edge.get_source()
        dest = edge.get_destination()
        total_distance = edge.get_total_distance()
        outdoor_distance = edge.get_outdoor_distance()
        
        # changing
        if src in self.nodes and dest in self.nodes:
            # print("-----------\n\n")
            # print(src, dest)
            # print("-----------\n\n")
            # raise ValueError("Node not in graph")
        
            self.edges[src].append((dest, total_distance, outdoor_distance))
        else:
            raise ValueError("Node not in graph")

# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.g = Digraph()
        self.na = Node('a')
        self.nb = Node('b')
        self.nc = Node('c')
        self.g.add_node(self.na)
        self.g.add_node(self.nb)
        self.g.add_node(self.nc)
        self.e1 = WeightedEdge(self.na, self.nb, 15, 10)
        self.e2 = WeightedEdge(self.na, self.nc, 14, 6)
        self.e3 = WeightedEdge(self.nb, self.nc, 3, 1)
        self.g.add_edge(self.e1)
        self.g.add_edge(self.e2)
        self.g.add_edge(self.e3)

    def test_weighted_edge_str(self):
        self.assertEqual(str(self.e1), "a->b (15, 10)")
        self.assertEqual(str(self.e2), "a->c (14, 6)")
        self.assertEqual(str(self.e3), "b->c (3, 1)")

    def test_weighted_edge_total_distance(self):
        self.assertEqual(self.e1.get_total_distance(), 15)
        self.assertEqual(self.e2.get_total_distance(), 14)
        self.assertEqual(self.e3.get_total_distance(), 3)

    def test_weighted_edge_outdoor_distance(self):
        self.assertEqual(self.e1.get_outdoor_distance(), 10)
        self.assertEqual(self.e2.get_outdoor_distance(), 6)
        self.assertEqual(self.e3.get_outdoor_distance(), 1)

    def test_add_edge_to_nonexistent_node_raises(self):
        node_not_in_graph = Node('q')
        no_src = WeightedEdge(self.nb, node_not_in_graph, 5, 5)
        no_dest = WeightedEdge(node_not_in_graph, self.na, 5, 5)

        with self.assertRaises(ValueError):
            self.g.add_edge(no_src)
        with self.assertRaises(ValueError):
            self.g.add_edge(no_dest)

    def test_add_existing_node_raises(self):
        with self.assertRaises(ValueError):
            self.g.add_node(self.na)

    def test_graph_str(self):
        expected = "a->b (15, 10)\na->c (14, 6)\nb->c (3, 1)"
        self.assertEqual(str(self.g), expected)


if __name__ == "__main__":
    unittest.main()
