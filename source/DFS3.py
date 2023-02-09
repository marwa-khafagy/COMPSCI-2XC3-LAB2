from graph import *
from collections import defaultdict


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(2, 5)
g.add_edge(5, 3)
g.add_edge(3, 4)
g.add_edge(0, 3)
g.add_edge(2, 0)
print(is_connected(g))