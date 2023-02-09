from graph import Graph
from collections import deque
import random

#Breadth First Search (TA added the comments as hints)
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2: #reached our destination
                #return path
                #should we return here or not
                return True
            if not marked[node]: 
                Q.append(node)
                #add node to path
                marked[node] = True
    return False

#TA made this function
def create_random_graph(i,j):
        G = Graph(i) # bc zero indexed
        x = random.randint(0,i-1)
        y = random.randint(0,i-1)
        for _ in range(j):
                while True:
                        if not G.are_connected(x,y):
                                G.add_edge(x, y)
                                break
                        x = random.randint(0,i-1)
                        y = random.randint(0,i-1)
        return G