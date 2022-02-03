# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
#


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    # TODO
    print("Loading map from file...")
    
    # file = open(map_filename)
    # var = fread(file)
    # print("---------\n\n")
    graph = Digraph()
    
    with open(map_filename, "r") as file:
        
        # count = 0
        for line in file:
            info = line.rstrip("\n")
            word_list = info.split(" ")
            # print(word_list, type(word_list))
            # count += 1
            
            src = Node(str(word_list[0]))
            # print(src, type(src))
            dest = Node(str(word_list[1]))
            
            total_distance = int(word_list[2])
            outdoor_distance = int(word_list[3])
            
            try:
                graph.add_node(src)
            except ValueError:
                # continue
                # print("dup src", src)
                # break
                pass
                
            try:
                graph.add_node(dest)
            except ValueError:
                # print("dup dest", dest)
                pass
            
            edge = WeightedEdge(src, dest, total_distance, outdoor_distance)
            # print(edge)
            graph.add_edge(edge)
            
            # print(src, dest, total_distance, outdoor_distance)
            # print("---------")
            # print(edge)
            # print("--------")
    
    # print("count", count)
    # print("---------\n\n")
    return graph

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out
# print(load_map("test_load_map.txt"))


#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer:
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    # TODO
    # pass

    # path = path + [start]
    path[0] = path[0] + [start]
    
    # printPath(path)
    print("DFS call with:", start)
    # print("Current DFS path:", printPath(path[0]))
    print("Current DFS path:", path)
    print("Best distance:", best_dist)
    print("Shortest path:", best_path)
    print("-------------------\n\n")

    if start == end:
        return path
    else:
        for node_tuple in digraph.get_edges_for_node(start):
            print("node tuple:", node_tuple)
            node = node_tuple[0]
            edge_cost = node_tuple[1]
            
            # path[1] = path[1] + edge_cost
            # if path[1] == None:
            #     path[1] = edge_cost
            # else:
            #     path[1] = path[1] + edge_cost
            
            if node not in path[0]:
                # path[1] = path[1] + edge_cost
                
            # path[1] = path[1] + edge_cost
                if path[1] == None:
                    path[1] = edge_cost
                else:
                    path[1] = path[1] + edge_cost
                
                if best_path == None or best_dist == None or path[1] < best_dist:
                    
                    new_path = get_best_path(digraph, node, end, path, max_dist_outdoors, best_dist, best_path)
                    
                    if new_path != None:
                        best_path = new_path[0]
                        best_dist = new_path[1]
    
    return [best_path, best_dist]


# # Problem 3b: Implement get_best_path
# def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
#                   best_path):
#     """
#     Finds the shortest path between buildings subject to constraints.

#     Parameters:
#         digraph: Digraph instance
#             The graph on which to carry out the search
#         start: string
#             Building number at which to start
#         end: string
#             Building number at which to end
#         path: list composed of [[list of strings], int, int]
#             Represents the current path of nodes being traversed. Contains
#             a list of node names, total distance traveled, and total
#             distance outdoors.
#         max_dist_outdoors: int
#             Maximum distance spent outdoors on a path
#         best_dist: int
#             The smallest distance between the original start and end node
#             for the initial problem that you are trying to solve
#         best_path: list of strings
#             The shortest path found so far between the original start
#             and end node.

#     Returns:
#         A tuple with the shortest-path from start to end, represented by
#         a list of building numbers (in strings), [n_1, n_2, ..., n_k],
#         where there exists an edge from n_i to n_(i+1) in digraph,
#         for all 1 <= i < k and the distance of that path.

#         If there exists no path that satisfies max_total_dist and
#         max_dist_outdoors constraints, then return None.
#     """
#     # TODO
#     # pass

#     path = path + [start]
    
#     # printPath(path)
#     print("DFS call with:", start)
#     print("Current DFS path:", printPath(path))
#     print("Shortest path:", best_path)
#     print("-------------------\n\n")

#     if start == end:
#         return path
#     else:
#         for node_tuple in digraph.get_edges_for_node(start):
#             # print(node)
#             node = node_tuple[0]
#             if node not in path:
#                 if best_path == None or len(path) < len(best_path):
#                     new_path = get_best_path(digraph, node, end, path, max_dist_outdoors, \
#                                              best_dist, best_path)
                    
#                     if new_path != None:
#                         best_path = new_path
    
#     return best_path

# comment: add
def printPath(path):
    
    result = ""
    for i in range(len(path)):
        # if i != (len(path)-1):
        result = result + str(path[i])
        
        if i != (len(path)-1):
            result = result + "->"
    return result


# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    # TODO
    # pass

    # digraph = load_map("test.txt")
    # start = digraph.get_node("0")
    # end = digraph.get_node("5")
    
    # shortest_path = get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path)


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


# if __name__ == "__main__":
#     unittest.main()

# comment: testing
# print(load_map("mit_map.txt"))
# print(load_map("test_load_map.txt"))
# print(load_map("test.txt"))

# path = [1, 2, 3, 2, 7]
# print(printPath(path))

digraph = load_map("test.txt")
# print(digraph)

start = digraph.get_node("0")
# print(start, type(start))
end = digraph.get_node("5")

print("-------------------\n\n")

INF = 1000000000

print(get_best_path(digraph, start, end, [[], None], 100, None, None))
# print(get_best_path(digraph, start, end, [], 100, INF, None))