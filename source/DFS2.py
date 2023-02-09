from graph import *


def DFS2Helper(G, node, node2, visited, path):
    if node == node2:
        path.append(node)
        return path
    path.append(node)
    visited[node] = True
    for adj_node in G.adj[node]:
        if not visited[adj_node]:
            return DFS2Helper(G, adj_node, node2, visited, path)
    return []


def DFS2(G, node1, node2):
    visited = {}
    path = []

    for node in G.adj:
        visited[node] = False

    return DFS2Helper(G, node1, node2, visited, path)


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(2, 5)
g.add_edge(5, 3)
g.add_edge(3, 4)
g.add_edge(0, 3)
print(DFS2(g, 2, 3))
