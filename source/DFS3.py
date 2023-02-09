from graph import *
from collections import defaultdict


def DFS3Helper(G, node, visited, predecessor):
    visited[node] = True
    for adj_node in G.adj[node]:
        if not visited[adj_node]:
            predecessor[adj_node].append(node)
            DFS3Helper(G, adj_node, visited, predecessor)
    return predecessor


def DFS3(G, node1):
    visited = {}
    predecessor = defaultdict(list)

    for node in G.adj:
        visited[node] = False

    return DFS3Helper(G, node1, visited, predecessor)


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(2, 5)
g.add_edge(5, 3)
g.add_edge(3, 4)
g.add_edge(0, 3)
g.add_edge(2, 0)
print(is_connected(g))
