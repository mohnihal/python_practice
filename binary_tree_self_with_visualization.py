"""Pytohn code to create, edit, insert and visualize binary tree"""
import pydot

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def insert_node(self, data):
        
        def insert_in_spot(root, data):
            if root.data == data:
                print(f'Integer {data} already exist in tree')
            if root.data < data:
                if root.right == None:
                    print (f'Integer {data} inserted right of {root.data}')
                    root.right = Node(data)
                else:
                    insert_in_spot(root.right, data)
            elif root.data > data:
                if root.left == None:
                    print (f'Integer {data} inserted left of {root.data}')
                    root.left = Node(data)
                else:
                    insert_in_spot(root.left, data)
        insert_in_spot(self.root, data)
    
    def print_binary_tree(self):
        def loop_through_nodes(root):
            if root is None:
                return 
            else:
                loop_through_nodes(root.left)
                print(root.data)
                loop_through_nodes(root.right)
        
        loop_through_nodes(self.root)


# Function to convert a binary tree to a Graphviz graph
def binary_tree_to_graph(node, graph=None):
    if graph is None:
        graph = pydot.Dot(graph_type='graph')
    if node:
        graph.add_node(pydot.Node(str(node.data)))
        if node.left:
            graph.add_edge(pydot.Edge(str(node.data), str(node.left.data)))
            binary_tree_to_graph(node.left, graph)
        if node.right:
            graph.add_edge(pydot.Edge(str(node.data), str(node.right.data)))
            binary_tree_to_graph(node.right, graph)
    return graph


import random
bt = BinaryTree(14)
for i in random.sample(range(1,40), 20):
    print(f'Insert {i}')
    bt.insert_node(i)

# Convert the binary tree to a Graphviz graph
binary_tree_graph = binary_tree_to_graph(bt.root)

# Save the graph to a file
binary_tree_graph.write_png('binary_tree.png')

## Some pre-requisites
# sudo apt-get update && sudo apt-get upgrade
# sudo apt-get install graphviz
# sudo apt-get install xdg-utils

