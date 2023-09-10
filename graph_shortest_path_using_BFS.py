'''Graph shortest path using BFS'''
from collections import defaultdict

def buildGraphFromMatrix(graph_matrix):
    graph = defaultdict(list)
    for pairs in graph_matrix:
        graph[pairs[0]].append(pairs[1])
    return graph


def findShortestPath(graph,start,goal):
    queue = [[start]]
    explored = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                # print ("new_path",new_path)
                queue.append(new_path)

                if neighbor==goal:
                    print ("shortest path from ",goal," is ",new_path)
                    return 
            
            explored.append(node)



if __name__ == "__main__":
     
    # Graph using dictionaries
    graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}
     
    # Function Call
    findShortestPath(graph, 'A', 'D')