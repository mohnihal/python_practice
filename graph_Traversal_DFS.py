'''Graph Traversal DFS  '''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, v,e):
        self.graph[v].append(e)

    def DFSUtil(self,v,visited):
        visited.add(v)

        print (v)
        for neighbour in self.graph[v]:
            if not neighbour in visited:
                self.DFSUtil(neighbour,visited)



    def DFS(self,u):
        print (self.graph)
        visited=set()
        self.DFSUtil(u,visited)



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)