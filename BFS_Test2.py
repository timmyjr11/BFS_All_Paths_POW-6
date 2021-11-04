# Python program to print all paths from a source to destination.

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:


    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''





    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False
    # Prints all paths from 's' to 'd'

    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)


# Create a graph given in the above diagram
g = Graph(25)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(3,7)
g.addEdge(6,10)
g.addEdge(6,11)
g.addEdge(10,15)
g.addEdge(4, 7)
g.addEdge(4, 8)
g.addEdge(7, 11)
g.addEdge(7, 12)
g.addEdge(11, 15)
g.addEdge(11, 16)
g.addEdge(15, 19)
g.addEdge(5, 8)
g.addEdge(5,9)
g.addEdge(8, 12)
g.addEdge(8, 13)
g.addEdge(12, 16)
g.addEdge(12, 17)
g.addEdge(16, 19)
g.addEdge(16, 20)
g.addEdge(19, 22)
g.addEdge(9, 13)
g.addEdge(9, 14)
g.addEdge(13, 17)
g.addEdge(13, 18)
g.addEdge(17, 20)
g.addEdge(17, 21)
g.addEdge(20, 22)
g.addEdge(20, 23)
g.addEdge(22, 24)
g.addEdge(14, 18)
g.addEdge(18, 21)
g.addEdge(21, 23)
g.addEdge(23, 24)

s = 0
d = 24
print("Following are all different paths from % d to % d :" % (s, d))
g.printAllPaths(s, d)