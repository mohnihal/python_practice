"""Program to find if the said edge is a bridge which means if there are other connections between the 2 nodes."""
from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
    
    def DFS(self, node, visited=[]):
        if not visited:
            visited = [False]*len(self.graph)
        for k in self.graph[node]:
            if not visited[k]:
                visited[k] = True
                self.DFS(k, visited)

    def isConnected(self, node1, node2):
        visited = [False]*len(self.graph)
        self.DFS(node1, visited)
        if visited[node2] == False:
            return False

    def isBridge(self, node1, node2):
        node1_in_node2 = self.graph[node2].index(node1)
        node2_in_node1 = self.graph[node1].index(node2)
        del self.graph[node1][node2_in_node1]
        del self.graph[node2][node1_in_node2]
        if self.isConnected(node1, node2) == False:
            print(f'The said connection between {node1} and {node2} is A BRIDGE')
        else:
            print(f'The said connection between {node1} and {node2} is NOT A BRIDGE')

g = Graph()
# Create a graph given in the
# above diagram
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.isBridge(4, 5)