# Haven't tested these functions yet.. 

# Helpers
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

# Actual func. 
def MIS(G):
    nodes = [i for i in range(G.get_size)]
    max_set = []

    for i in get_power_set(nodes):
        if is_ind_set(i, G) and len(i) > len(max_set):
            max_set = i
    return max_set