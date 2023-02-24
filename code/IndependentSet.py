from graph import Graph
from experiment1 import create_random_graph, add_random_edge
from plotting import PlotGroup
import random
import matplotlib.pyplot as plot

#------------------------------------------------------------------------------------------------
#  FROM LEC
#------------------------------------------------------------------------------------------------

def is_vertex_cover(L, G):
    for start in G.adj.keys():
        for end in G.adj[start]:
            if start not in L and end not in L:
                return False
    return True

def MVC(G): #minimum vertex cover
    nodes = [i for i in range(G.number_of_nodes())]
    min_cover = nodes

    for i in get_power_set(nodes):
        if is_vertex_cover(i, G) and len(i) < len(min_cover):
            min_cover = i

    return min_cover


#------------------------------------------------------------------------------------------------
#  HELPER FUNCTIONS
#------------------------------------------------------------------------------------------------

def add_to_each(subsets, element):
    my_subsets = subsets.copy()
    for subset in my_subsets:
        subset.append(element)
    return my_subsets

def get_power_set(L):
    if L == []:
        return [[]]
    return get_power_set(L[1:]) + add_to_each(get_power_set(L[1:]), L[0])

def is_ind_set(L, G):
    for start in G.adj.keys():
        for end in G.adj[start]:
            if start in L and end in L:
                return False
    return True

def sum_of_MIS_MVC(G):
    return len_MIS(G) + len_MVC(G)

def len_MIS(G):
    return len(MIS(G))

def len_MVC(G):
    return len(MVC(G))

def rand_edge_count(n):
    max = int((n*(n + 1)) / 2)
    return random.randint(0, max)

#------------------------------------------------------------------------------------------------
#  MIS FUNCTION 
#------------------------------------------------------------------------------------------------

def MIS(G):
    nodes = [i for i in range(G.number_of_nodes())]
    max_set = []

    for i in get_power_set(nodes):
        if is_ind_set(i, G) and len(i) > len(max_set):
            max_set = i
    return max_set


#------------------------------------------------------------------------------------------------
#  TESTING FUNCTIONS
#------------------------------------------------------------------------------------------------

def size_of_MIS_MVC_test(max_nodes,trail_count, skip):

    p = PlotGroup("Sum of MIS and MVC")

    for n in range(0, max_nodes, skip):
        sum = 0
        for _ in range(trail_count):
            G = create_random_graph(n, rand_edge_count(n))
            sum += sum_of_MIS_MVC(G)
            # print("Num of Nodes: ", n, " Sum: ", sum_of_MIS_MVC(G), " Total: ", sum)
        p.add_point(n, sum/trail_count)
        print(f"Plotted Point ({n},{sum/trail_count})")
    
    name = f"Relationship Between Size of MIS and MVC"#({trail_count} trials)"
    plot.title(name)

    plot.xlabel("Graph size (in vertices)")
    plot.ylabel("Sum of MIS and MVC")

    p.plot()

    plot.legend()
    plot.show()

#------------------------------------------------------------------------------------------------
#  TESTS
#------------------------------------------------------------------------------------------------

G1 = Graph(2)
G1.add_edge(1, 0)
G1.add_edge(1, 1)

G2 = Graph(10)
G2.add_edge(0, 1)
G2.add_edge(0, 4)
G2.add_edge(0, 7)
G2.add_edge(1, 2)
G2.add_edge(2, 3)
G2.add_edge(4, 5)
G2.add_edge(5, 6)
G2.add_edge(7, 8)
G2.add_edge(8, 9)

print(MIS(G2))
print(MVC(G2))

print(sum_of_MIS_MVC(G2))


test1 = size_of_MIS_MVC_test(25, 1, 1)
