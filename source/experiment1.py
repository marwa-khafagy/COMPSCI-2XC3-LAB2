from graph import *
from collections import deque
import random

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