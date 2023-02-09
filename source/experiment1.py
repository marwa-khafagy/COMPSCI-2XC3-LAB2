from graph import has_cycle
from graph import Graph
from collections import deque
import random

#TA made this function
def create_random_graph(i,j):
    G = Graph(i) # bc zero indexed

    for _ in range(j):
        add_random_edge(G)

    return G

def add_random_edge(G):

    i = G.number_of_nodes();

    while True:
        #Generate Position
        x = random.randint(0,i-1)
        y = random.randint(0,i-1)

        if not G.are_connected(x,y):
            G.add_edge(x, y)
            break

#
def proportionality_test(const_node_count, max_edge_count, graph_sample_size):
    
    #How many Edges to create? (X axis)
    for e in range(max_edge_count):

        cyclicalGraphCount = 0

        # Generate X Graphs
        for _ in range(graph_sample_size):

            #Generate Random Graph
            sampleGraph = create_random_graph(const_node_count, e);

            #Increment Count
            if has_cycle(sampleGraph):
                cyclicalGraphCount += 1

        #Get Proportion
        cyclicalPercentage = cyclicalGraphCount / graph_sample_size

    # Plot Here
    name = f"Number of Cyclical {const_node_count} Node Graphs out of {graph_sample_size} vs The Amount of Random Edges added to them"


#
def edge_additions_until_cycle_test(node_counts, trials_per_node_count):
    
    for i in node_counts:
        
        #Sum time, average after for data point
        edgeCountSum = 0
        minEdgesAddedForCycle = 0
        maxEdgesAddedForCycle = 0

        for _ in trials_per_node_count:

            testGraph = Graph(i)

            #Have Counts
            countUntilCycle = 0
            maximumPossibleEdgeCount = i*(i-1)/2;

            #Loop Until Cycle Made
            while countUntilCycle < maximumPossibleEdgeCount:
                
                #Add Edge To Graph
                add_random_edge(testGraph)
                countUntilCycle += 1

                #Exit if Cycle was made
                if has_cycle(testGraph):

                    # Good to Know
                    minEdgesAddedForCycle = min(minEdgesAddedForCycle, countUntilCycle)
                    maxEdgesAddedForCycle = min(maxEdgesAddedForCycle, countUntilCycle)

                    #Exit
                    break;

            #Add to Sum
            edgeCountSum += countUntilCycle

        #Get Proportion
        edgeCountAverage = edgeCountSum / trials_per_node_count;
        
        #Add to Data Point

    #Plot Here
    name = f"Number of Edge Additions to Create Cycle in Empty Graph, {trials_per_node_count} Trials"



if (__name__ == "__main__"):
    pass
