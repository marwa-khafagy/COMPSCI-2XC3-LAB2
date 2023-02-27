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
#  PLOTTING FUNCTIONS
#------------------------------------------------------------------------------------------------
def generate_plot_dict():
    return {'x': [], 'y' : []}

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

def complement(l, max):
    result = []

    for i in range(max):
        if i not in l:
            result += [i]

    return result


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

    mis_mvc = generate_plot_dict()
    g = generate_plot_dict()

    for n in range(0, max_nodes, skip):
        sum = 0
        for _ in range(trail_count):
            G = create_random_graph(n, rand_edge_count(n))
            sum += sum_of_MIS_MVC(G)
            # print("Num of Nodes: ", n, " Sum: ", sum_of_MIS_MVC(G), " Total: ", sum)
        
        mis_mvc['x'].append(n)
        g['x'].append(n)

        mis_mvc['y'].append(sum/trail_count)
        g['y'].append(G.number_of_nodes())
            
        print(f"Plotted Point ({n},{sum/trail_count})")
    
    name = f"Relationship Between Size of MIS and MVC({trail_count} trials)"
    plot.title(name)

    plot.xlabel("Graph size (in vertices)")
    plot.ylabel("Number of Nodes")

    plot.plot(g['x'], g['y'], label="MVC", color='k')
    plot.plot(mis_mvc['x'], mis_mvc['y'], label="Nodes in Graph", color='y', linestyle="dashed")


    plot.legend()
    plot.show()
    
def len_comp_MVC(max_nodes,trials, skip):

    len_of_comp_of_mvc = generate_plot_dict()
    len_of_mvc = generate_plot_dict()
    len_of_mis = generate_plot_dict()

    for n in range(0, max_nodes, skip):

        avg_mis = 0
        avg_mvc = 0

        for _ in range(trials):     
            G = create_random_graph(n, rand_edge_count(n))
            temp = MVC(G)
            if not is_ind_set(complement(temp, G.number_of_nodes()), G): 
                raise Exception("The complement of this MVC is not a MIS")
            temp_mis = len_MIS(G)
            temp_mvc = len(temp)
            avg_mvc += temp_mvc
            avg_mis += temp_mis

        len_of_comp_of_mvc['x'].append(n)
        len_of_mis['x'].append(n)
        len_of_mvc['x'].append(n)

        len_of_comp_of_mvc['y'].append(G.number_of_nodes() - avg_mvc / trials)
        len_of_mis['y'].append(avg_mis / trials)
        len_of_mvc['y'].append(avg_mvc / trials)

        print(f"Plotted Point ({n},{avg_mis / trials})")
    
    name = f"MVC and It's Complement({trials} trials)"
    plot.title(name)

    plot.xlabel("Graph size (in vertices)")
    plot.ylabel("Set Cardinality")

    plot.plot(len_of_mis['x'], len_of_mis['y'], label="MIS", color='k')
    plot.plot(len_of_mvc['x'], len_of_mvc['y'], label="MVC")
    plot.plot(len_of_comp_of_mvc['x'], len_of_comp_of_mvc['y'], label="Complement of MVC", linestyle='dashed', color='y')
   
    plot.legend()
    plot.show()


def len_comp_MIS(max_nodes,trials, skip):

    len_of_comp_of_mis = generate_plot_dict()
    len_of_mvc = generate_plot_dict()
    len_of_mis = generate_plot_dict()

    for n in range(0, max_nodes, skip):

        avg_mis = 0
        avg_mvc = 0

        for _ in range(trials):     
            G = create_random_graph(n, rand_edge_count(n))
            temp = MIS(G)
            if not is_vertex_cover(complement(temp, G.number_of_nodes()), G): 
                raise Exception("The complement of this MVC is not a MIS")
            temp_mis = len(temp)
            temp_mvc = len_MVC(G)
            avg_mvc += temp_mvc
            avg_mis += temp_mis

        len_of_comp_of_mis['x'].append(n)
        len_of_mis['x'].append(n)
        len_of_mvc['x'].append(n)

        len_of_comp_of_mis['y'].append(G.number_of_nodes() - avg_mis / trials)
        len_of_mis['y'].append(avg_mis / trials)
        len_of_mvc['y'].append(avg_mvc / trials)

        print(f"Plotted Point ({n},{avg_mis / trials})")
    
    name = f"MIS and It's Complement({trials} trials)"
    plot.title(name)

    plot.xlabel("Graph size (in vertices)")
    plot.ylabel("Set Cardinality")

    plot.plot(len_of_mis['x'], len_of_mis['y'], label="MIS")
    plot.plot(len_of_mvc['x'], len_of_mvc['y'], label="MVC", color='k')
    plot.plot(len_of_comp_of_mis['x'], len_of_comp_of_mis['y'], label="Complement of MIS", linestyle='dashed', color='y')
   
    plot.legend()
    plot.show()


#------------------------------------------------------------------------------------------------
#  TESTS
#------------------------------------------------------------------------------------------------

print("------------------------------------------------------------------------")
print("Test 1:")
test1 = size_of_MIS_MVC_test(25, 5, 1)
print("Test 1 Done")
print("------------------------------------------------------------------------")

print("Test 2:")
test2 = len_comp_MVC(25,5, 1)
print("Test 2 Done")
print("------------------------------------------------------------------------")

print("Test 3:")
test3 = len_comp_MIS(25,5, 1)
print("Test 3 Done")
print("------------------------------------------------------------------------")