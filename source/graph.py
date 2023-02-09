from collections import deque
from collections import defaultdict

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


#
#
#
#   DFS2 AND BFS2
#
#
#

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

#
#
#

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

#
#
#
#   DFS3 and BFS3
#
#
#

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

#
#
#