from graph import Graph
from collections import deque
import random


#TA hint

# def has_cycle(G):
#     marked = dict([(i, false) for i in G.adj]) # true if dfs traveresed it
#     for i in G.adj:
#         if not marked[i]:
#             if DFSCycleChecker(G, ? ? , marked) == True:
#                 return True
#     return False