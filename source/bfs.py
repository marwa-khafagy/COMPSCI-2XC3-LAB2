from graph import Graph
from collections import deque
import random

def BFS2(G, node1, node2):
    parent = {}
    parent[node1] = None
    path = []

    Q = deque([node1])
    marked = {node1 : True}

    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        # print("Infinite?")
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            # print("Infinite? in for")
            print(parent)
            if node == node2:
                parent[node] = current_node 
                path.append(node)
                while parent[node] is not None:
                    node = parent[node]
                    path.insert(0, node)
                    if parent[node] == node1:
                        path.insert(0, node1)
                        break
                return path
            
            if not marked[node]: 
                parent[node] = current_node
                Q.append(node)
                marked[node] = True

    return []



g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 6)
print(BFS2(g, 1, 6))

#TA hint

# def has_cycle(G):
#     marked = dict([(i, false) for i in G.adj]) # true if dfs traveresed it
#     for i in G.adj:
#         if not marked[i]:
#             if DFSCycleChecker(G, ? ? , marked) == True:
#                 return True
#     return False