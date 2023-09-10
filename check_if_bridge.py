'''check if given edge is bridge'''
from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list)
        pass
    def addEdge(self,edge1,edge2):
        self.graph[edge1].append(edge2)

    def DFS(self,v,visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i,visited)
            

    def isConnected(self):
        visited = [False]*len(self.graph)
        self.DFS(0,visited)
        if all(visited):
            return True
        else:
            return False

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u) 

    def isBridge(self,u,v):
        indU = self.graph[v].index(u)
        indV = self.graph[u].index(v)

        del self.graph[v][indU]
        del self.graph[u][indV]

        res = self.isConnected()
        self.addEdge(u, v)
        return (res==False)

if __name__ == '__main__':
 
    # Create a graph given in the
    # above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
 
    if g.isBridge(1, 2):
        print("Yes")
    else:
        print("No")