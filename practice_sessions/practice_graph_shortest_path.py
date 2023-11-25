'''Graph shortest path using BFS'''
from collections import defaultdict

def findShortestPath(graph,start,goal):
    queue = [[start]]
    explored = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        for neighbour in graph[node]:
            if neighbour not in explored:
                new_path = list(path)
                new_path.append(neighbour)
                if neighbour == goal:
                    print(f'Shortest path found from {start} to {goal}: {new_path}')
                    return
                queue.append(new_path)
        
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
    findShortestPath(graph, 'A', 'G')