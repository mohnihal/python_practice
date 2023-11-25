'''Graph Traversal DFS  '''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, v,e):
        self.graph[v].append(e)

    # def BFSUtil(self,v,visited):
    #     visited.add(v)

    #     print (v)
    #     for neighbour in self.graph[v]:
    #         if not neighbour in visited:
    #             self.DFSUtil(neighbour,visited)



    def BFS(self,u):
        print (self.graph)
        visited=[False]*(max(self.graph)+1)
        # self.DFSUtil(u,visited)
        queue = []
        queue.append(u)
        visited[u] = True
        while queue:
            s = queue.pop(0)
            print(s)
            for adjacent in self.graph[s]:
                if not visited[adjacent]:
                    queue.append(adjacent)
                    visited[adjacent] = True



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)