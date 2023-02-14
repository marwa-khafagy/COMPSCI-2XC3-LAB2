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

    #Can't Add Edges between nodes that don't exist
    if (i == 0):
        return False

    while True:
        #Generate Position
        x = random.randint(0,i-1)
        y = random.randint(0,i-1)

        if not G.are_connected(x,y):
            G.add_edge(x, y)
            return True

#
def proportionality_test(const_node_count, max_edge_count, trial_count):
    
    #Plot
    amount = PlotGroup("Average Number of Cyclical Graphs")
    amount.placelineAtFirstY1 = True

    #How many Edges to create? (X axis)
    for e in range(max_edge_count):

        cyclicalGraphCount = 0

        # Generate X Graphs
        for _ in range(trial_count):

            #Generate Random Graph
            sampleGraph = create_random_graph(const_node_count, e);

            #Increment Count
            if has_cycle(sampleGraph):
                cyclicalGraphCount += 1

        #Get Proportion
        cyclicalAverageCount = cyclicalGraphCount / trial_count
        amount.add_point(e, cyclicalAverageCount)

        print(f"Plotted Point ({e},{cyclicalAverageCount}). ({e}/{max_edge_count})")

    # Plot Here
    name = f"Percentage of Cyclical Graphs out of {trial_count} Graphs with Node Count {const_node_count}"
    plot.title(name)

    plot.xlabel("Random Graph Edge Count")
    plot.ylabel("Percentage of Cyclical Graphs")

    amount.plot()

    plot.legend()
    plot.show()

#
def max_proportionality_test(const_node_count, trial_count):

    edgeCount = int((const_node_count*(const_node_count + 1)) / 2)
    proportionality_test(const_node_count, edgeCount, trial_count)

#
def edge_additions_until_cycle_test(node_counts, trials_per_node_count):
    
    edgeCountAverage = PlotGroup("Mean Edge Additions until Cycle", "#359cff")
    minEdgeCountPerNodeCount = PlotGroup("Minimum Edge Additions until Cycle", "#b4daff")
    maxEdgeCountPerNodeCount = PlotGroup("Maximum Edge Additions until Cycle", "#d4b4ff")

    for i in node_counts:
        
        #Sum time, average after for data point
        edgeCountSum = 0
        minEdgesAddedForCycle = None #Never will be more than this
        maxEdgesAddedForCycle = None
        cycleFound = False

        #Repeat Trials
        for _ in range(trials_per_node_count):

            testGraph = Graph(i)

            #Have Counts
            countUntilCycle = 0
            maximumPossibleEdgeCount = i*(i+1)/2;

            #Loop Until Cycle Made
            while countUntilCycle < maximumPossibleEdgeCount:
                
                #Add Edge To Graph; Exit if couldn't
                if not add_random_edge(testGraph):
                    break

                countUntilCycle += 1
                

                #Exit if Cycle was made
                if has_cycle(testGraph):

                    cycleFound = True

                    # Good to Know
                    minEdgesAddedForCycle = smin(minEdgesAddedForCycle, countUntilCycle)
                    maxEdgesAddedForCycle = smax(maxEdgesAddedForCycle, countUntilCycle)

                    #Exit
                    break;

            #Add to Sum
            edgeCountSum += countUntilCycle

        #Don't Plot if There was never a cycle found (e = 0)
        if (cycleFound):
            edgeCountAverage.add_point(i, edgeCountSum / trials_per_node_count);
            minEdgeCountPerNodeCount.add_point(i, minEdgesAddedForCycle) 
            maxEdgeCountPerNodeCount.add_point(i, maxEdgesAddedForCycle)
        
        print(f"Plotted Point ({i},{edgeCountSum / trials_per_node_count}), m:{minEdgesAddedForCycle}, M:{maxEdgesAddedForCycle}.")

        #Add to Data Point

    #Plot Here
    name = f"Number of Edge Additions to Create Cycle in Empty Graph, {trials_per_node_count} Trials"
    plot.title(name)

    plot.xlabel("Graph Node Count")
    plot.ylabel("Edge Additions to creat cycle")

    edgeCountAverage.plot()
    minEdgeCountPerNodeCount.plot()
    maxEdgeCountPerNodeCount.plot()

    plot.legend()
    plot.show()

#
# TESTS
#

if (__name__ == "__main__"):

    #Proportionality For small(ish) graphs
    # max_proportionality_test(5, 1000)
    # max_proportionality_test(10, 1000)
    # max_proportionality_test(30, 1000)

    #At this point the amount of possible graphs become crazy
    # proportionality_test(100, 500, 100)

    
    #Low Rest
    # edge_additions_until_cycle_test(range(5), 1000)

    #Good Basis
    # edge_additions_until_cycle_test(range(100), 1000)

    #Low Trial
    edge_additions_until_cycle_test(range(0, 1000, 10), 10)
