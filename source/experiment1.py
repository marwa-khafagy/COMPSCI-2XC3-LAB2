from graph import has_cycle, Graph
from plotting import PlotGroup
import matplotlib.pyplot as plot
import random

#
#
def smin(a,b):
    if (a == None):
        return b
    if (b == None):
        return a
    
    return min(a,b)

def smax(a,b):
    if (a == None):
        return b
    if (b == None):
        return a
    
    return max(a,b)
#
#

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
    
    #Plot
    amount = PlotGroup("Average Number of Cyclical Graphs")
    amount.placelineAtFirstY1 = True

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
        cyclicalAverageCount = cyclicalGraphCount / graph_sample_size
        amount.add_point(e, cyclicalAverageCount)

        print(f"Plotted Point ({e},{cyclicalAverageCount}). ({e}/{max_edge_count})")

    # Plot Here
    name = f"Percentage of Cyclical Graphs out of {graph_sample_size} Graphs with Node Count {const_node_count}"
    plot.title(name)

    plot.xlabel("Random Graph Edge Count")
    plot.ylabel("Percentage of Cyclical Graphs")

    amount.plot()

    plot.legend()
    plot.show()


#
def edge_additions_until_cycle_test(node_counts, trials_per_node_count):
    
    edgeCountAverage = PlotGroup("", "#359cff")
    minEdgeCountPerNodeCount = PlotGroup("Minimum Number Found", "#b4daff")
    maxEdgeCountPerNodeCount = PlotGroup("Maximum Number Found", "#d4b4ff")

    for i in node_counts:
        
        #Sum time, average after for data point
        edgeCountSum = 0
        minEdgesAddedForCycle = None #Never will be more than this
        maxEdgesAddedForCycle = None

        #Repeat Trials
        for _ in range(trials_per_node_count):

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
                    minEdgesAddedForCycle = smin(minEdgesAddedForCycle, countUntilCycle)
                    maxEdgesAddedForCycle = smax(maxEdgesAddedForCycle, countUntilCycle)

                    #Exit
                    break;

            #Add to Sum
            edgeCountSum += countUntilCycle

        #Get Proportion
        edgeCountAverage.add_point(i, edgeCountSum / trials_per_node_count);

        if (minEdgeCountPerNodeCount != None):
            minEdgeCountPerNodeCount.add_point(i, minEdgesAddedForCycle)

        if (maxEdgeCountPerNodeCount != None):    
            maxEdgeCountPerNodeCount.add_point(i, maxEdgesAddedForCycle)
        
        print(f"Plotted Point ({i},{edgeCountSum / trials_per_node_count}), m:{minEdgesAddedForCycle}, M:{maxEdgesAddedForCycle}.")

        #Add to Data Point

    #Plot Here
    name = f"Number of Edge Additions to Create Cycle in Empty Graph, {trials_per_node_count} Trials"
    plot.title(name)

    plot.xlabel("Random Graph Edge Count")
    plot.ylabel("Percentage of Cyclical Graphs")

    edgeCountAverage.plot()
    minEdgeCountPerNodeCount.plot()
    maxEdgeCountPerNodeCount.plot()

    plot.legend()
    plot.show()

#
# TESTS
#

if (__name__ == "__main__"):
    
    #proportionality_test(100, 100, 1000)
    edge_additions_until_cycle_test(range(100), 100)
