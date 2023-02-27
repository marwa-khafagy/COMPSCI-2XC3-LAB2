from collections import deque
from collections import defaultdict
import random

# Undirected graph using an adjacency list


class Graph:

    def __init__(self, n):
        self.adj = {}
        self.nodesWithEdges = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):

        # Memoize
        self.nodesWithEdges[node1] = True

        # Only add self reference once
        if (node1 == node2):
            self.adj[node1].append(node1)
            return

        # Memoize Second
        self.nodesWithEdges[node2] = True

        # Add Otherwise
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)

    def __len__(self):
        return self.number_of_nodes()

    def remove_node(self, node):
        for adj_node in self.adj[node]:
            if node in self.adj[adj_node]:
                self.adj[adj_node].remove(node)
        self.adj[node].clear()


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

    for node in G.nodesWithEdges:
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
    marked = {node1: True}

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


def BFS3(G, node1):

    Q = deque([node1])
    predecessor = {}

    # Mark Nodes
    marked = {node1: True}

    while len(Q) > 0:

        current_node = Q.popleft()

        # Go over all possible nexts
        for node in G.adj[current_node]:

            # Mark if not already
            if not marked.get(node, False):

                # Enqueue
                marked[node] = True
                Q.append(node)

                # Mark my prececessor
                predecessor[node] = current_node

    return predecessor


def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy


def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])


def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True


def MVC(G):
    nodes = [i for i in range(len(G))]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


def highest_degree(G):
    highest = 0
    node = None
    for start in G.adj:
        if len(G.adj[start]) > highest:
            highest = len(G.adj[start])
            node = start
    return node


def get_random_node_not_in_C(G, C):
    node = random.randint(0, len(G)-1)
    while node in C:
        node = random.randint(0, len(G)-1)
    return node


def get_random_edge(G):
    start = random.randint(0, len(G)-1)
    end = random.randint(0, len(G)-1)
    while end not in G.adj[start]:
        start = random.randint(0, len(G)-1)
        end = random.randint(0, len(G)-1)

    return (start, end)


def approx1(G):
    C = set()

    while not is_vertex_cover(G, C):
        node = highest_degree(G)
        C.add(node)
        G.remove_node(node)

    return C


def approx2(G):
    C = set()
    v = -1

    while not is_vertex_cover(G, C):
        v = get_random_node_not_in_C(G, C)
        C.add(v)
    return C


def approx3(G):
    C = set()
    while not is_vertex_cover(G, C):
        edge = get_random_edge(G)
        C.add(edge[0])
        C.add(edge[1])
        G.remove_node(edge[0])
        G.remove_node(edge[1])
    return C


if __name__ == '__main__':
    G = Graph(5)
    print(approx1(G))
