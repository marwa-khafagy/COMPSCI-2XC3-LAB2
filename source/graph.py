from collections import deque

# Undirected graph using an adjacency list


class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


# Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


# Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


def has_cycle(G):
    marked = {}
    for node in G.adj:
        marked[node] = False
    for node in G.adj:
        if not marked[node]:
            if has_cycle_util(G, node, marked, -1):
                return True

    return False


def has_cycle_util(G, node, marked, parent):
    marked[node] = True

    for adj_node in G.adj[node]:
        if not marked[adj_node]:
            if has_cycle_util(G, adj_node, marked, node):
                return True
        elif adj_node != parent:
            return True

    return False


def is_connected_util(G, node, marked):
    marked[node] = True
    for adj_node in G.adj[node]:
        if not marked[adj_node]:
            is_connected_util(G, adj_node, marked)
    return marked


def is_connected(G):
    marked = {}

    marked = [False]*len(G.adj)

    marked = is_connected_util(G, 0, marked)

    return all(marked[i] == True for i in range(len(marked)))
